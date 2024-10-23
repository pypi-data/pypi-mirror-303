#!/usr/bin/env python3
"""
Helper functions for ensuring that SQL tables are created with the expected
columns.
"""

import contextlib
import logging
import sqlite3


LOGGER = logging.getLogger(__name__)


def dict_factory(cursor, row):
    """
    Row factory for dicts.

    Args:
        cursor:
            The database cursor.

        row:
            The row data.

    Returns:
        A dict with the row data.
    """
    dct = {}
    for i, col in enumerate(cursor.description):
        dct[col[0]] = row[i]
    return dct


@contextlib.contextmanager
def dict_factory_cursor(cursor):
    """
    Conext manager for temporarily using a dict row factory.

    Args:
        cursor:
            The database cursor.

    Returns:
        A cursor with the row factory temporary set to dict_factory. When the
        context exits, the cursor's previous row factory will be restored.
    """
    prev_row_factory = cursor.row_factory
    try:
        cursor.row_factory = dict_factory
        yield cursor
    finally:
        cursor.row_factory = prev_row_factory


def get_name_and_expected_create_table_sql(create_table_sql):
    """
    Create a table in temporary in-memory database using the given SQL statement
    and get the table's name and sql statement from the resulting sqlite_master
    table.

    Args:
        create_table_sql:
            An SQL statement to create a table.

    Returns:
        The name of the created table and the resulting SQL statement in the
        sqlite_master table.
    """
    conn = sqlite3.connect(":memory:")
    conn.row_factory = dict_factory
    with conn as cur:
        cur.execute(create_table_sql)
        info = cur.execute(
            "SELECT * FROM sqlite_master WHERE type=?", ("table",)
        ).fetchone()
        return info["name"], info["sql"]


def create_and_check_table(cur, create_table_sql, drop=False):
    """
    Ensure that a table is created according to the given table creation SQL statement.

    Args:
        cur:
            An SQLite database cursor.

        create_table_sql:
            An SQL statement to create a table.

        drop:
            If True, drop existing tables that do not match the given table
            creation statement, else raise ValueError on mismatch.

    Raises:
        ValueError:
            A table with the same name exists but does not match the given SQL
            creation statement, i.e. the columns do not match.
    """
    LOGGER.debug("Received SQL creation statement: %s", repr(create_table_sql))
    name, expected_sql = get_name_and_expected_create_table_sql(create_table_sql)
    LOGGER.debug(
        "Expected equivalent SQL creation statement in sqlite_master table: %s",
        repr(expected_sql),
    )

    with dict_factory_cursor(cur) as dct_cur:
        existing_info = dct_cur.execute(
            "SELECT * FROM sqlite_master WHERE type=? AND name=?", ("table", name)
        ).fetchone()

    # The table does not exist and will be created according to the given statement.
    if existing_info is None:
        LOGGER.info("Creating new table %s.", name)
        cur.execute(create_table_sql)
        return
    # The table already exists. Check that the creation statements are equivalent.
    LOGGER.debug("Table %s already exists.", name)
    existing_sql = existing_info["sql"]
    if existing_sql != expected_sql:
        LOGGER.debug(
            "SQL creation statement of existint table %s does not match: %s",
            name,
            existing_sql,
        )
        if drop:
            LOGGER.info(
                "Dropping existing table %s due to mismatched SQL creation statements.",
                name,
            )
            cur.execute(f'DROP TABLE "{name}"')
            LOGGER.info("Creating table %s.", name)
            cur.execute(create_table_sql)
            return
        raise ValueError(
            f'An existing table named "{name}" was created with a non-equivalent SQL statement: '
            f"{existing_info['sql']}"
        )
    LOGGER.debug(
        "Existing table %s is equivalent to the given SQL creation statement.", name
    )
