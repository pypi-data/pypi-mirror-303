"""
The FO module contains functions to work with Finance and Operations data.

Functions: 
 - translate_enums: Broadcast join the DataFrame with the EnumValues table to translate the enums to their labels
"""


from pyspark.sql import DataFrame
from pyspark.sql.functions import broadcast, col
from pyspark.sql.utils import AnalysisException
from uuid import UUID

from evidi_fabric.fs import get_table, get_table_path

def translate_enums(df:DataFrame, table_name:str, cols:list[str] = [], postfix:str = "_txt", table_name_enum:str = 'EnumValues', lakehouse_enum:str | UUID = 'Silver', workspace_enum:str | UUID = None) -> DataFrame:
    """
    Boarcast join the DataFrame with the EnumValues table to translate the enums to their labels.

    Args:
        df: DataFrame
        table_name: Name of the F&O table
        columns: List of enum column names to be translated
        table_name_enum: Name of the EnumValues table
        lakehouse_enum: lakehouse where the EnumValues table is located
        workspace_enum: workspace where the EnumValues table is located
        postfix: Postfix to add to the translated columns

    Returns:
        df where the specified enums columns have been translated and stored in a column postfixed with '_txt'
    """

    #Import mapping dataframe
    df_enum_mapping = _get_enum_table_mapping(df, table_name, table_name_enum, lakehouse_enum, workspace_enum)

    if not cols:
        cols = _get_all_enums_in_table(df_enum_mapping)

    _validate_enum_mapping(df_enum_mapping, cols)
    cols_new = _get_output_columns(df, cols, postfix)

    df_translated = df
    df_enum_mapping.cache()
    for column in cols:
        enum_mapping = df_enum_mapping.filter(col("FieldName")==column)\
                                      .selectExpr(f"EnumValueInt AS {column}",
                                                  f"EnumValueLabel AS {column}{postfix}")
        df_translated = df_translated.join(broadcast(enum_mapping), on=column, how="left")

    df = df_translated.select(*cols_new)
    return df

def _get_output_columns(df:DataFrame, cols:list[str], postfix:str) -> list[str]:
    """
    Get the output columns in correct order
    """
    cols_org = df.columns
    cols_new = []
    for column in cols_org:
        cols_new.append(column)
        if column in cols:
            cols_new.append(f"{column}{postfix}")
    return cols_new

def _get_all_enums_in_table(df_enum_mapping:DataFrame) -> list[str]:
    """
    Get all the enum columns in the table
    """
    return list(df_enum_mapping.select("FieldName").distinct().rdd.flatMap(lambda x: x).collect())

def _validate_enum_mapping(df_enum_mapping:DataFrame, cols:list[str]) -> None:
    """
    Validate that the EnumValues table contains the specified columns
    """
    enum_cols = _get_all_enums_in_table(df_enum_mapping)
    non_existing_cols = [column for column in cols if column not in enum_cols]
    if non_existing_cols:
        raise ValueError(f"Column(s) {'', ''.join(non_existing_cols)} not found in EnumValues table. Consider adding the column(s) to the EnumValues table.")


def _get_enum_table_mapping(df:DataFrame, table_name:str, table_name_enum:str, lakehouse_enum:str | UUID, workspace_enum:str | UUID) -> DataFrame:
    """
    Get the EnumValues table
    """
    try:
        df_enum_mapping = get_table(table_name = table_name_enum, lakehouse = lakehouse_enum)\
                         .filter(col("TableName")==table_name)
    except AnalysisException as e:
        error_message = str(e)
        if "PATH_NOT_FOUND" in error_message:
            path_enum_mapping = get_table_path(table_name_enum, lakehouse_enum, workspace_enum)
            err_msg = f"Path: {path_enum_mapping} does not exist."
            err_msg += "\nTo setup the translate_enums correctly, navigate to this notebook and read the instructions: https://app.fabric.microsoft.com/groups/52f0ede9-fab6-43a7-9b27-d72df7962491/synapsenotebooks/611cf53a-ca74-4d3d-9eeb-85210a36528b?experience=data-engineering "
            raise FileNotFoundError(err_msg)
        else:
            raise e
    return df_enum_mapping