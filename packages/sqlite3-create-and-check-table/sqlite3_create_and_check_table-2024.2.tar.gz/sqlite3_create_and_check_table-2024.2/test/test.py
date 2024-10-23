#!/usr/bin/env python3
"""Test table creation."""


import sqlite3
import unittest


from sqlite3_create_and_check_table import create_and_check_table, dict_factory_cursor


def get_sqlite_master_sql_statement(cur, table_name):
    """
    Get the SQL creation statement used to create the given table.

    Args:
        cur:
            The SQLite database cursor.

        table_name:
            The database table name.

    Returns:
        The corresponding SQL statement in the sqlite_master table if it exists,
        else None.
    """
    with dict_factory_cursor(cur) as dct_cur:
        info = dct_cur.execute(
            "SELECT * FROM sqlite_master WHERE type=? AND name=?", ("table", table_name)
        ).fetchone()
    if info is None:
        return None
    return info["sql"]


class TestCreateAndCheckTable(unittest.TestCase):
    """
    Test the create_and_check_table function.
    """

    TABLE_NAME = "test"
    SQL1 = "CREATE TABLE test (prim TEXT PRIMARY KEY, int INTEGER, blob BLOB NON NULL)"
    SQL2 = "CREATE TABLE test (prim TEXT PRIMARY KEY, int REAL, blob BLOB NON NULL)"
    TEST_DATA = (
        ("a", 1, b"a1"),
        ("b", 2, b"b2"),
        ("c", 3, b"c3"),
    )

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")

    def _insert_test_data(self, cur):
        """
        Insert test data into table.

        Args:
            cur:
                SQLite database cursor.
        """
        cur.executemany(
            f'INSERT INTO "{self.TABLE_NAME}" VALUES(?, ?, ?)', self.TEST_DATA
        )

    def _check_test_data(self, cur):
        """
        Check that the table contains the test data.

        Args:
            cur:
                SQLite database cursor.
        """
        rows = cur.execute(f'SELECT * FROM "{self.TABLE_NAME}"')
        data = tuple(tuple(row) for row in rows)
        self.assertEqual(self.TEST_DATA, data)

    def _check_empty(self, cur):
        """
        Check that the table is empty.

        Args:
            cur:
                SQLite database cursor.
        """
        rows = cur.execute(f'SELECT * FROM "{self.TABLE_NAME}"')
        self.assertIsNone(rows.fetchone())

    def _check_existing_table(self, cur, expected_sql):
        """
        Utility function to check existing tables.

        Args:
            cur:
                SQLite database cursor.

            expected_sql:
                The expected SQL creation statement in the sqlite_master table.
        """
        self.assertEqual(
            expected_sql, get_sqlite_master_sql_statement(cur, self.TABLE_NAME)
        )

    def test_no_default_table(self):
        """No table exists before a creation statement is executed."""
        with self.conn as cur:
            self.assertIsNone(get_sqlite_master_sql_statement(cur, self.TABLE_NAME))

    def test_create_new_table(self):
        """New tables are created."""
        with self.conn as cur:
            for sql in (self.SQL1, self.SQL2):
                for drop in (True, False):
                    with self.subTest(sql=sql, drop=drop):
                        create_and_check_table(cur, sql, drop=drop)
                        self._check_existing_table(cur, sql)
                        cur.execute(f'DROP TABLE "{self.TABLE_NAME}"')

    def test_do_nothing_if_correct_table_exists(self):
        """Existing table with correct columns is not changed."""
        with self.conn as cur:
            create_and_check_table(cur, self.SQL1)
            self._insert_test_data(cur)
            for drop in (True, False):
                with self.subTest(drop=drop):
                    create_and_check_table(cur, self.SQL1, drop=drop)
                    self._check_test_data(cur)

    def test_drop_existing_table_if_different(self):
        """Existing tables are dropped if different and drop is requested."""
        with self.conn as cur:
            create_and_check_table(cur, self.SQL1)
            self._insert_test_data(cur)
            self._check_test_data(cur)
            create_and_check_table(cur, self.SQL2, drop=True)
            self._check_existing_table(cur, self.SQL2)
            self._check_empty(cur)

    def test_raise_value_error_if_different(self):
        """Existing tables raise value errors if different and drop is not requested."""
        with self.conn as cur:
            create_and_check_table(cur, self.SQL1)
            with self.assertRaises(ValueError):
                create_and_check_table(cur, self.SQL2, drop=False)


if __name__ == "__main__":
    unittest.main()
