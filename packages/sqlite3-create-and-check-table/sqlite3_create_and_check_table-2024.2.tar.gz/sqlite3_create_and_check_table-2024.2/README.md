---
title: README
author: Jan-Michael Rye
---

# Synopsis

A Python package that provides a simple utility function for creating SQLite tables. The function will compare an existing table's SQL statement from the `sqlite_master` table to the one expected for a given SQL table creation statement. If the existing table does not match the expected SQL statement then it can either be dropped an recreated, or a `ValueError` can be raised.

The primary purpose of this function is to facilitate the creation of tables for caching temporary data that can be discarded, such as memoizing calls to remote server APIs.

## Links

[insert: links 2]: #

### GitLab

* [Homepage](https://gitlab.inria.fr/jrye/sqlite3-create_and_check_table)
* [Source](https://gitlab.inria.fr/jrye/sqlite3-create_and_check_table.git)
* [Documentation](https://jrye.gitlabpages.inria.fr/sqlite3-create_and_check_table)
* [Issues](https://gitlab.inria.fr/jrye/sqlite3-create_and_check_table/-/issues)
* [GitLab package registry](https://gitlab.inria.fr/jrye/sqlite3-create_and_check_table/-/packages)

### Other Repositories

* [Python Package Index](https://pypi.org/project/sqlite3-create-and-check-table/)

[/insert: links 2]: #

# Usage

~~~python
import sqlite3
from sqlite3_create_and_check_table import create_and_check_table

sql = "CREATE TABLE test (prim TEXT PRIMARY KEY, int INTEGER, blob BLOB NON NULL)"
conn = sqlite3.connect("/path/to/some/sqlite3/db.sqlite")
with conn as cur:
    # Create the table with the given SQL statement. If a table with the same
    # name exists but differs from what would result from the given SQL table
    # creation statement, it will be dropped and recreated to match the given
    # statement.
    # If drop is set to False then a ValueError will be raised instead.
    create_and_check_table(cur, sql, drop=True)
~~~

The package also provides a row factory function for returning rows in the table as `dict`s as well as an sqlite3 cursor context manager for temporarily setting the the row factory to the provided `dict` factory:

~~~python
import sqlite3
from sqlite3_create_and_check_table import dict_factory, dict_factory_cursor

conn = sqlite3.connect("/path/to/some/sqlite3/db.sqlite")
# Set the row factory within a context and restore the previous row factory when
# leaving the context.
with dict_factory_cursor(conn) as cur:
    # cur.execute(...)

# Set the row factory for all queries.
conn.row_factory = dict_factory
~~~
