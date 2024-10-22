"""
This module contains functions to work with dataverse.

    - get_df_stringmap: Load the stringmap table into a DataFrame
    - string_map: Join the DataFrame with the stringmap table to get the string values for the given columns

Example:
    >>> from evidi_fabric.dataverse import string_map
    >>> df_stringmap = string_map(df, "table_name", ["column1", "column2"])
    """

from pyspark.sql import DataFrame
from pyspark.sql.functions import expr
from uuid import UUID

from evidi_fabric.fs import get_table_path

try:
    spark
except NameError:
    from evidi_fabric.spark import get_or_create_spark

    spark = get_or_create_spark()


def _get_df_stringmap(lakehouse_dataverse: str | UUID | None = None, workspace_dataverse: str | UUID | None = None):
    """
    Load the stringmap table into a DataFrame

    stringmap is a table that contains the string values for the given columns
    and is a standard table in dataverse
    """
    table_path_stringmap = get_table_path(
        table_name="stringmap", lakehouse=lakehouse_dataverse, workspace=workspace_dataverse
    )

    df_stringmap = spark.read.load(table_path_stringmap)
    return df_stringmap


def string_map(
    df: DataFrame,
    table: str,
    encoded_columns: list[str],
    postfix: str = "name",
    langid: int = 1030,
    lakehouse_dataverse: str | UUID | None = None,
    workspace_dataverse: str | UUID | None = None,
):
    """
    Join the DataFrame with the stringmap table to get the string values for the given columns
    Note: Requires that all column names of the original dataframe are unique

    Args:
        df: DataFrame to join
        table: Table name
        encoded_columns: List of column names
        postfix: Suffix to add to the new column names
        langid: Language id
        lakehouse_dataverse: lakehouse where the stringmap table is located
        workspace_dataverse: workspace where the stringmap table is located

    Returns:
        DataFrame: Orginal DataFrame with the mapped values for the given encoded columns
                   The new column names are postfixed with string specified in the 'postfix' variable
    """
    # Load the stringmap table into a DataFrame
    df_stringmap = _get_df_stringmap(lakehouse_dataverse=lakehouse_dataverse, workspace_dataverse=workspace_dataverse)
    df_joined = df.alias("df")
    cols_output_with_alias = [f"df.{col}" for col in df.columns]
    cols_output = df.columns
    for encoded_column in encoded_columns:
        alias = encoded_column
        df_stringmap_filter = df_stringmap.filter(
            f"attributename='{encoded_column}' AND objecttypecode='{table}' AND langid={langid}"
        )
        df_joined = df_joined.join(
            df_stringmap_filter.alias(alias), on=expr(f"df.{encoded_column} = {alias}.attributevalue"), how="left"
        )
        cols_output_with_alias += [f"{alias}.value AS {encoded_column}{postfix}"]
        cols_output += [f"{encoded_column}{postfix}"]
    df_with_alias = df_joined.selectExpr(*cols_output_with_alias)
    df_without_alias = df_with_alias.toDF(*cols_output)
    return df_without_alias
