import psycopg2
from psycopg2 import pool
from contextlib import contextmanager
from .config import PostgresConfig


class PostgresClient:
    _connection_pool = None

    @classmethod
    def initialize_pool(cls, pg_config: PostgresConfig):
        """PostgreSQL 연결 풀을 초기화하는 메서드."""
        if cls._connection_pool is None:
            cls._connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 20,  # 최소 및 최대 연결 수
                user=pg_config.user,
                password=pg_config.password,
                host=pg_config.host,
                port=pg_config.port,
                database=pg_config.database
            )
            print("PostgreSQL 연결 풀이 초기화되었습니다.")
        else:
            print("PostgreSQL 연결 풀은 이미 초기화되어 있습니다.")

    @classmethod
    @contextmanager
    def get_connection(cls, pg_config: PostgresConfig):
        """PostgreSQL 연결을 가져오고 자동으로 반환하는 컨텍스트 매니저."""
        if cls._connection_pool is None:
            cls.initialize_pool(pg_config)

        connection = cls._connection_pool.getconn()
        try:
            print("PostgreSQL 연결이 반환되었습니다.")
            yield connection
        finally:
            cls._connection_pool.putconn(connection)
            print("PostgreSQL 연결이 풀로 반환되었습니다.")

    @classmethod
    def close_all_connections(cls):
        """모든 PostgreSQL 연결을 닫는 메서드."""
        if cls._connection_pool:
            cls._connection_pool.closeall()
            cls._connection_pool = None
            print("모든 PostgreSQL 연결이 닫혔습니다.")