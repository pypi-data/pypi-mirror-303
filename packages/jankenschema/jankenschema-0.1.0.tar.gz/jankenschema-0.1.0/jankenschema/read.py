import sqlite3

from .db_column import DbColumn


SQL_TABLE_LIST = """
   SELECT name FROM sqlite_master
   WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;
"""


def get_tables(cursor: sqlite3.Cursor):
    """Get a list of tables in the database"""
    cursor.execute(SQL_TABLE_LIST)
    return cursor.fetchall()


SQL_TABLE_INFO = "PRAGMA table_info(%s)"


def get_columns(cursor: sqlite3.Cursor, table: str) -> list[DbColumn]:
    """Get a list of columns for a table in the database"""
    cursor.execute(SQL_TABLE_INFO % table)
    return [DbColumn(row) for row in cursor.fetchall()]


def get_schemas(cursor: sqlite3.Cursor) -> dict[str, list[DbColumn]]:
    """Get a dictionary of tables and their columns in the database"""
    tables = get_tables(cursor)
    schemas = {}
    for (table_name,) in tables:
        columns = get_columns(cursor, table_name)
        schemas[table_name] = columns
    return schemas
