from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.hooks.base import BaseHook
import psycopg2
import impala.dbapi as impaladb


class ImpalaToPostgresUpsertOperator(BaseOperator):

    @apply_defaults
    def __init__(self, impala_conn_id, postgres_conn_id, query, table, primary_key, batch_size=1000, *args, **kwargs):
        super(ImpalaToPostgresUpsertOperator, self).__init__(*args, **kwargs)
        self.impala_conn_id = impala_conn_id
        self.postgres_conn_id = postgres_conn_id
        self.query = query
        self.table = table
        self.primary_key = primary_key
        self.batch_size = batch_size

    def get_columns(self, cursor):
        return [desc[0] for desc in cursor.description]

    def generate_upsert_query(self, columns):
        """根据列名自动生成 UPSERT SQL 语句"""
        col_str = ', '.join(columns)
        placeholders = ', '.join(['%s'] * len(columns))


        update_str = ', '.join([f"{col} = EXCLUDED.{col}" for col in columns if col != self.primary_key])

        upsert_query = f"""
            INSERT INTO {self.table} ({col_str}) 
            VALUES ({placeholders})
            ON CONFLICT ({self.primary_key}) 
            DO UPDATE SET {update_str}
        """
        return upsert_query

    def execute(self, context):

        impala_conn = BaseHook.get_connection(self.impala_conn_id)
        impala_host = impala_conn.host
        impala_port = impala_conn.port
        impala_user = impala_conn.login
        impala_password = impala_conn.password
        impala_database = impala_conn.schema


        self.log.info(f"Connecting to Impala at {impala_host}:{impala_port}")
        impala_conn = impaladb.connect(
            host=impala_host,
            port=impala_port,
            user=impala_user,
            password=impala_password,
            database=impala_database,
            auth_mechanism="LDAP",
            use_http_transport=True,
            http_path="cliservice",
            use_ssl=True,
        )
        impala_cursor = impala_conn.cursor()

        impala_cursor.execute(self.query)
        columns = self.get_columns(impala_cursor)
        upsert_query = self.generate_upsert_query(columns)
        rows = impala_cursor.fetchmany(self.batch_size)


        pg_conn = BaseHook.get_connection(self.postgres_conn_id)
        pg_host = pg_conn.host
        pg_port = pg_conn.port
        pg_user = pg_conn.login
        pg_password = pg_conn.password
        pg_database = pg_conn.schema


        self.log.info(f"Connecting to PostgreSQL at {pg_host}:{pg_port}")
        pg_conn = psycopg2.connect(
            dbname=pg_database,
            user=pg_user,
            password=pg_password,
            host=pg_host,
            port=pg_port
        )
        pg_cursor = pg_conn.cursor()


        while rows:
            self.log.info(f"Upserting {len(rows)} rows into PostgreSQL")
            self.log.info(f"upsert_query: {upsert_query}")
            self.log.info(f"rows: {rows}")
            pg_cursor.executemany(upsert_query, rows)
            pg_conn.commit()
            rows = impala_cursor.fetchmany(self.batch_size)
        impala_cursor.close()
        impala_conn.close()
        pg_cursor.close()
        pg_conn.close()
        self.log.info("Data synchronization with UPSERT complete")