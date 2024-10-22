import unittest

from postgresql_singleton.config import PostgresConfig
from postgresql_singleton.db import PostgresClient


class TestPostgresClient(unittest.TestCase):

    def setUp(self):
        self.config = PostgresConfig(
            host="localhost",
            user="postgres",
            password="nice123!@#",
            database="kibisis",
            port=5432
        )

    def test_initialize_pool(self):
        PostgresClient.initialize_pool(self.config)
        self.assertIsNotNone(PostgresClient._connection_pool)

    def test_get_connection(self):
        with PostgresClient.get_connection(self.config) as connection:
            self.assertIsNotNone(connection)

    def test_close_all_connections(self):
        PostgresClient.initialize_pool(self.config)
        PostgresClient.close_all_connections()
        self.assertIsNone(PostgresClient._connection_pool)

    def test_sql(self):
        with PostgresClient.get_connection(self.config) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1;")
                result = cursor.fetchone()
                print(result)