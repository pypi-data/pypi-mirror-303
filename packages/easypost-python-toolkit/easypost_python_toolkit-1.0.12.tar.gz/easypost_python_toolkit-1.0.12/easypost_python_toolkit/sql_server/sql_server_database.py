"""
This module provides a class, SQLServerDatabase, for interacting with a SQL Server database using the pyodbc library.
The class supports various database operations such as executing queries and fetching results.

Classes:
    SQLServerDatabase: Encapsulates methods for connecting to a SQL Server database and performing various queries.

The SQLServerDatabase class includes the following methods:
    - fetch_all: Executes a query and returns all results.
    - fetch_one: Executes a query and returns the first result.
    - fetch_value: Executes a query and returns the first value of the first result.
    - execute_query: Executes a query and commits if specified.
    - execute_many: Executes a query for multiple sets of parameters and commits if specified.
    - _execute: General method to handle database actions.
    - _get_connection: Creates and returns a new database connection using the current environment variable.

Usage:
    To use this module, create an instance of SQLServerDatabase with the environment variable name holding the
    connection string. Then, call the provided methods to interact with the database.
"""

import os
import pyodbc


class SQLServerDatabase:

    def __init__(self, connection_string_env_var: str):
        self.connection_string_env_var = connection_string_env_var

    def fetch_all(self, query: str, params: tuple = (), return_dict: bool = True):
        """Executes a query and returns all results."""
        return self._execute(lambda cursor, q, p: cursor.execute(q, p).fetchall(), query, params, return_dict)

    def fetch_one(self, query: str, params: tuple = (), return_dict: bool = True):
        """Executes a query and returns the first result."""
        return self._execute(lambda cursor, q, p: cursor.execute(q, p).fetchone(), query, params, return_dict, True)

    def fetch_value(self, query: str, params: tuple = ()):
        """Executes a query and returns the first value of the first result."""
        return self._execute(lambda cursor, q, p: cursor.execute(q, p).fetchval(), query, params)

    def execute_query(self, query: str, params: tuple = ()):
        """Executes a query and commits if specified."""
        return self._execute(lambda cursor, q, p: cursor.execute(q, p), query, params)

    def execute_many(self, query: str, params: tuple = ()):
        """Executes a query for multiple sets of parameters and commits if specified."""
        return self._execute(lambda cursor, q, p: cursor.executemany(q, p), query, params)

    def _execute(self, action, query: str, params: tuple = (), return_dict: bool = False, single_row: bool = False):
        """General method to handle database actions."""
        try:
            with self._get_connection() as connection:
                cursor = connection.cursor()
                # cursor.fast_executemany = True
                result = action(cursor, query, params)
                if return_dict and result:
                    columns = [col[0] for col in cursor.description]
                    if single_row:
                        return dict(zip(columns, result)) if result else None
                    return [dict(zip(columns, row)) for row in result]
                return result
        except Exception:
            raise

    def _get_connection(self):
        """Creates and returns a new database connection using the current environment variable."""
        try:
            connection_string = os.getenv(self.connection_string_env_var)
            if connection_string is None:
                raise ValueError(
                    f"No connection string found in environment variable '{self.connection_string_env_var}'")
            return pyodbc.connect(connection_string)
        except Exception:
            raise
