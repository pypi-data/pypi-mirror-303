"""
The `sql` module provides helper functions for working with SQL tables in Microsoft Fabric 
This module includes functions for creating temporary views for all underlying SQL tables in a SQL query. 
This is particularly useful when working with large datasets or complex queries.

 - find_all_tables_in_sql: Finds all source tables used in a SQL query.
 - create_sql_views_from_sql: Creates a temporary view for each table in a SQL query.

Here's an example of how to use this module:

```python
from evidi_fabric.sql import create_sql_views_from_sql
sql = "SELECT sales_amount FROM transactions"
lakehouse = "Decide_DK_Silver"
create_sql_views_from_sql(sql=sql, lakehouse=lakehouse)
"""

import re
from uuid import UUID
from evidi_fabric.fs import get_table_path

try:
    spark
except NameError:
    from evidi_fabric.spark import get_or_create_spark

    spark = get_or_create_spark()


def find_all_tables_in_sql(sql_query: str) -> list[str]:
    """
    From any sql_query, returns a list of all dependent tables.

    e.g.
    sql_query="SELECT * FROM A" -> ["A"]
    sql_query="WITH CTE (SELECT * FROM A)\n SELECT * FROM CTE" -> ["A","CTE"]
    sql_query="WITH CTE (SELECT * FROM A)\n SELECT * FROM CTE INNER JOIN B ON A.key = B.key" -> ["A","CTE","B"]

    """
    pattern = re.compile(r"\b(?:FROM|JOIN)\s+([a-zA-Z_]\w*)\b", re.IGNORECASE)
    matches = pattern.findall(sql_query)
    return matches


def create_sql_views_from_sql(sql: str, lakehouse: str | UUID | None = None) -> None:
    """
    When reading a table from an sql query, i.e. spark.sql(table_sql),
    you cannot reference the absolute path to the source.

    To overcome this, this function
    1) finds all source tables used in the sql_query,
    2) finds their absolute paths
    3) create a temporary view of the data

    This view can then be accessed from sql, but refere to the table name
    without specifying the schema

    Example:
        table_sql = "SELECT sales_amount FROM transactions"
        lakehouse = "Decide_DK_Silver"

    then a view is created called transactions,
    so that spark.sql(table_sql) can be executed pointing to the
    absolute path of transactions
    """
    table_names = find_all_tables_in_sql(sql)
    for table_name in table_names:
        table_path = get_table_path(table_name=table_name, lakehouse=lakehouse)
        df_temp = spark.read.load(table_path)
        df_temp.createOrReplaceTempView(table_name)


if __name__ == "__main__":
    table_sql = "WITH CTE (SELECT * FROM A)\n SELECT * FROM CTE INNER JOIN B ON A.key"
    tables = find_all_tables_in_sql(table_sql)
    print(tables)

    sql = "SELECT sales_amount FROM transactions"
    lakehouse = "Decide_DK_Silver"
    create_sql_views_from_sql(sql, lakehouse)
