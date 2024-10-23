import logging
import re
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.hooks.base import BaseHook
from impala.dbapi import connect
import psycopg2

class ImpalaToPostgresSyncOperator(BaseOperator):
    @apply_defaults
    def __init__(self,
                 impala_conn_id: str,
                 postgres_conn_id: str,
                 impala_query: str,
                 table: str,
                 mode: str = 'upsert',  # insert, upsert, insert_overwrite
                 batch_size: int = 1000,
                 primary_keys: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.impala_conn_id = impala_conn_id
        self.postgres_conn_id = postgres_conn_id
        self.impala_query = impala_query
        self.table = table
        self.mode = mode
        self.batch_size = batch_size
        self.primary_keys = primary_keys if primary_keys else []

    def get_impala_connection(self):
        logging.info(f"Connecting to Impala using connection id: {self.impala_conn_id}")
        conn = BaseHook.get_connection(self.impala_conn_id)
        impala_conn = connect(
            host=conn.host,
            port=conn.port,
            user=conn.login,
            password=conn.password,
            auth_mechanism="LDAP",
            use_http_transport=True,
            http_path="cliservice",
            use_ssl=True,
        )
        logging.info("Successfully connected to Impala")
        return impala_conn

    def get_postgres_connection(self):
        logging.info(f"Connecting to PostgreSQL using connection id: {self.postgres_conn_id}")
        conn = BaseHook.get_connection(self.postgres_conn_id)
        pg_conn = psycopg2.connect(
            host=conn.host,
            port=conn.port,
            user=conn.login,
            password=conn.password,
            dbname=conn.schema
        )
        logging.info("Successfully connected to PostgreSQL")
        return pg_conn

    def extract_columns(self, impala_cursor, sql_query: str):
        """Extracts column names from the SELECT query. If SELECT * is used, fetches column names from Impala schema"""
        logging.info("Extracting columns from the Impala query")
        pattern = r'SELECT\s+(.*?)\s+FROM'
        match = re.search(pattern, sql_query, re.IGNORECASE)
        if match:
            columns_str = match.group(1)
            if columns_str.strip() == '*':
                # Handle SELECT * case
                logging.info(f"Query uses SELECT *, fetching column names for table: {self.table}")
                impala_cursor.execute(f"DESCRIBE {self.table}")
                columns = [desc[0] for desc in impala_cursor.description]
            else:
                columns = [col.strip() for col in columns_str.split(',')]
            logging.info(f"Extracted columns: {columns}")
            return columns
        else:
            raise ValueError("Failed to extract columns from the query")

    def generate_insert_query(self, columns):
        column_list = ', '.join(columns)
        value_list = ', '.join(['%s'] * len(columns))
        insert_query = f"INSERT INTO {self.table} ({column_list}) VALUES ({value_list})"
        logging.info(f"Generated insert query: {insert_query}")
        return insert_query

    def generate_upsert_query(self, columns):
        column_list = ', '.join(columns)
        value_list = ', '.join(['%s'] * len(columns))
        primary_key_list = ', '.join(self.primary_keys)
        update_list = ', '.join([f"{col} = EXCLUDED.{col}" for col in columns if col not in self.primary_keys])
        upsert_query = (f"INSERT INTO {self.table} ({column_list}) VALUES ({value_list}) "
                        f"ON CONFLICT ({primary_key_list}) DO UPDATE SET {update_list}")
        logging.info(f"Generated upsert query: {upsert_query}")
        return upsert_query

    def execute(self, context):
        # Connect to Impala
        impala_conn = self.get_impala_connection()
        impala_cursor = impala_conn.cursor()

        logging.info(f"Executing Impala query: {self.impala_query}")
        # Execute Impala query
        impala_cursor.execute(self.impala_query)

        # Extract columns
        columns = self.extract_columns(impala_cursor, self.impala_query)

        # Generate SQL based on mode
        if self.mode == 'insert':
            logging.info("Mode is 'insert'")
            insert_query = self.generate_insert_query(columns)
        elif self.mode == 'upsert':
            logging.info("Mode is 'upsert'")
            if not self.primary_keys:
                raise ValueError("Upsert mode requires a primary_key")
            insert_query = self.generate_upsert_query(columns)
        elif self.mode == 'insert_overwrite':
            logging.info("Mode is 'insert_overwrite'")
            insert_query = f"TRUNCATE {self.table}; {self.generate_insert_query(columns)}"
        else:
            raise ValueError(f"Unsupported mode: {self.mode}")

        # Connect to PostgreSQL
        postgres_conn = self.get_postgres_connection()
        pg_cursor = postgres_conn.cursor()

        logging.info(f"Starting batch synchronization with batch size: {self.batch_size}")
        # Batch synchronization
        total_rows = 0
        while True:
            rows = impala_cursor.fetchmany(self.batch_size)
            if not rows:
                break
            pg_cursor.executemany(insert_query, rows)
            postgres_conn.commit()
            total_rows += len(rows)
            logging.info(f"Inserted/updated {len(rows)} rows, total rows processed: {total_rows}")

        logging.info(f"Completed synchronization, total rows inserted/updated: {total_rows}")

        # Close connections
        pg_cursor.close()
        postgres_conn.close()
        impala_cursor.close()
        impala_conn.close()
        logging.info("All connections closed successfully")