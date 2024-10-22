# PostgreSQL Singleton Client

A simple PostgreSQL connection pool manager using Singleton pattern.

## Overview

This package provides a PostgreSQL connection pool manager implemented using the Singleton pattern. It allows efficient management of database connections by reusing a single connection pool across multiple parts of your application.

## Features

- Implements the Singleton pattern for PostgreSQL connection pool management.
- Uses `psycopg2` for PostgreSQL connections.
- Simple connection management using a context manager.
- Connection pooling for improved performance and resource management.

## Installation

You can install this package via pip:

```bash
pip install postgresql_singleton
```

## Usage
### Step 1: Create a PostgreSQL configuration
First, you need to define the PostgreSQL connection configuration using the PostgresConfig class.

from postgresql_client.config import PostgresConfig

```python 
    pg_config = PostgresConfig(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database",
    port=5432
)
```

### Step 2: Use the PostgreSQL connection pool
You can use the PostgresClient class to manage your PostgreSQL connections. The class provides a context manager to acquire and release connections efficiently.
```pycon
from postgresql_client.client import PostgresClient

# Initialize the connection pool (this should be done once)
PostgresClient.initialize_pool(pg_config)

# Use the connection pool in a context manager
with PostgresClient.get_connection(pg_config) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        print(result)

# Close all connections when the application is shutting down
PostgresClient.close_all_connections()
```
