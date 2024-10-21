from .sql import SQLConnector, SqliteConnector, SQLConnectorConfig
import importlib


def load_from_mysql(connection_info, query):
    pymysql = importlib.import_module("pymysql")
    pd = importlib.import_module("pandas")

    conn = pymysql.connect(
        host=connection_info["host"],
        user=connection_info["user"],
        password=connection_info["password"],
        database=connection_info["database"],
        port=connection_info["port"],
    )
    return pd.read_sql(query, conn)


def load_from_postgres(connection_info, query):
    psycopg2 = importlib.import_module("psycopg2")
    pd = importlib.import_module("pandas")
    conn = psycopg2.connect(
        host=connection_info["host"],
        user=connection_info["user"],
        password=connection_info["password"],
        dbname=connection_info["database"],
        port=connection_info["port"],
    )
    return pd.read_sql(query, conn)


__all__ = [
    "SQLConnector",
    "SqliteConnector",
    "SQLConnectorConfig",
    "load_from_mysql",
    "load_from_postgres",
]
