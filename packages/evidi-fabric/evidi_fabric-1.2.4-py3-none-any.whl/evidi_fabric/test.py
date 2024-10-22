"""
The `test` module provides functions to test the quality of a semantic model in a lakehouse.

Functions:
    - test_dimensions: Test dimensions for unique keys
    - test_facts: Test facts for NULL values replaced with standard values
    - test_relationships: Test relationships between fact and dimension tables
    - test_semantic_model: Test the quality of a semantic model in a lakehouse
"""

import pandas as pd
from uuid import UUID
from pyspark.sql.functions import col, when, sum, lower
from pyspark.sql import DataFrame
from sempy.fabric import list_relationships, list_partitions

from evidi_fabric.fs import get_table_paths
from evidi_fabric.semanticmodel import get_dimension_keys, get_dimension_tables, get_fact_keys, get_fact_tables, resolve_lakehouse_from_semantic_model
from evidi_fabric.utils import generate_unknown_row

try:
    spark
except NameError:
    from evidi_fabric.spark import get_or_create_spark
    spark = get_or_create_spark()

def test_dimension_duplicate_keys(df: DataFrame, key:str, dimension:str):
    """
    Test if a dimension table has duplicate keys
    """
    unique_count = df.groupBy(key).count().filter(col("count") > 1).count()
    if unique_count > 0:
        duplicated_keys = df.groupBy(key).count().filter(col("count") > 1).select(key).collect()
        print(f"\t[Warning] Table: {dimension}, Test: duplicate_keys, Failed. Duplicate keys found: {duplicated_keys}")

def test_if_null_values(df: DataFrame, table_name:str):
    """
    Test if a table contains NULL values and print the columns with NULL values.
    """
    # Calculate the count of nulls in each column
    null_counts = df.select([
        sum(when(col(c).isNull(), 1).otherwise(0)).alias(c) for c in df.columns
    ])

    # Collect the results into a dictionary
    null_counts_dict = null_counts.collect()[0].asDict()

    # Identify columns that have null values
    null_columns = [column for column, count in null_counts_dict.items() if count > 0]

    # Check if any columns have null values and print them
    if null_columns:
        warn_msg = f"\t[Warning] Table: {table_name}, Test: null_values, Failed. NULL values found in columns: {null_columns} "
        warn_msg += "Consider using the replace_null_values function"
        print(warn_msg)

def test_dimension_unknown_row(df: DataFrame, key: str, dimension: str):
    """
    Test if a dimension table has unknown rows
    """
    unknown_value = generate_unknown_row(df.select(key)).collect()[0][0]

    if isinstance(unknown_value,str):
        unknown_value = unknown_value.lower()
        
    unknown_exists = df.filter(lower(col(key)) == unknown_value).count() > 0
    if not unknown_exists:
        warn_msg = f"\t[Warning] Table: {dimension}, Test: unknown_row, Failed. The unknown value: '{unknown_value}' was not found in the key {key}. "
        warn_msg += "Consider adding an 'Unknown' row to the table using the add_unknown_row_to_df function"
        print(warn_msg)

def test_dimensions(tables: dict[str, str], relationships: pd.DataFrame):
    """
    Test dimensions for unique keys
    """
    print("Starting dimension tests...")
    dimension_tables = get_dimension_tables(relationships)
    for dimension in dimension_tables:
        df = tables[dimension]
        test_if_null_values(df, table_name = dimension)
        keys = get_dimension_keys(dimension, relationships)
        for key in keys:
            if is_many_to_many_dimension(relationships, dimension, key):
                print(f"\t[Warning] Table: {dimension}, Test: many_to_many. The table is part of a many-to-many relationship and hence duplicated keys are allowed.")
            else:
                test_dimension_duplicate_keys(df, key, dimension)
            test_dimension_unknown_row(df, key, dimension)
    print("Dimension tests completed.")

def is_many_to_many_dimension(relationships: pd.DataFrame, dimension: str, key: str) -> bool:
    """
    Check if a dimension table is part of a many-to-many relationship
    """
    unique_multiplicity = relationships.loc[
        (relationships["Datasource Table Name To"] == dimension) &
        (relationships["To Column"] == key), "Multiplicity"
    ].drop_duplicates().to_list()

    "m:m" in unique_multiplicity
    return "m:m" in unique_multiplicity

def test_fact_identical_key(df: DataFrame, key: str, fact: str):
    """
    Test if a key in a fact table is identical
    """
    identical_key_count = df.select(key).count()
    if identical_key_count == 1:
        identical_key_value = df.select(key).collect()[0][0]
        print(f"\t[Warning] Table: {fact}, Test: identical_key, Failed. All {key} are identical and equal to {identical_key_value}.")

def test_facts(tables: dict[str, str], relationships: pd.DataFrame):
    """
    Test facts for NULL values replaced with standard values
    """
    print("\n\nStarting fact tests...")
    fact_tables = get_fact_tables(relationships)
    for fact in fact_tables:
        df = tables[fact]
        test_if_null_values(df, table_name = fact)

        keys = get_fact_keys(fact, relationships)
        for key in keys:
            test_fact_identical_key(df, key, fact)
    print("Fact tests completed.")


def test_relationship_missing_dim_keys(fact_df: DataFrame, dim_df: DataFrame, fact_key: str, dim_key: str, fact_table: str, dim_table: str):
    """
    Test if a kay value exists in the fact table but not in the dimension table
    """
    missing_keys_df = fact_df.join(dim_df, fact_df[fact_key] == dim_df[dim_key], "leftanti")
    missing_keys_count = missing_keys_df.count()
    if missing_keys_count > 0:
        missing_keys_summary = (
            missing_keys_df
            .groupBy(fact_key)
            .count()
            .orderBy(fact_key)
        )
        missing_keys_values = [f"{row[fact_key]} (count: {row['count']})" for row in missing_keys_summary.collect()]
        print(f"\t[Warning] {fact_table}.{fact_key} has values not found in {dim_table}.{dim_key}. Missing values found: {missing_keys_values}")

def test_relationships(tables: dict[str, str], relationships: pd.DataFrame):
    """
    Test relationships between fact and dimension tables
    """
    print("\n\nStarting relationship tests...")
    # Iterate over the relationships and test each relationship
    for _, row in relationships.iterrows():
        fact_table = row["Datasource Table Name From"]
        fact_key = row["From Column"]
        dim_table = row["Datasource Table Name To"]
        dim_key = row["To Column"]
        fact_df = tables[fact_table]
        dim_df = tables[dim_table]
        test_relationship_missing_dim_keys(fact_df, dim_df, fact_key, dim_key, fact_table, dim_table)
    print("Relationship tests completed.")

def test_semantic_model(semantic_model: str, workspace: str | UUID | None = None):
    print("Fetching relationships from semantic model...")
    relationships = list_relationships(dataset=semantic_model, workspace=workspace)
    partitions = list_partitions(dataset=semantic_model, workspace=workspace)
    partitions.rename(columns={"Query": "Datasource Table Name"}, inplace=True)
    
    # If Mode is not DirectLake or Import, raise a warning
    modes = partitions["Mode"].drop_duplicates().to_list()
    not_supported_modes = [mode for mode in modes if mode not in ["DirectLake", "Import"]]
    if not_supported_modes:
        not_support_table_names = partitions[partitions["Mode"].isin(not_supported_modes)]["Table Name"].to_list()
        print("\t[Warning] tables with unsupported modes found: ", not_support_table_names)
        print("Only tables with mode DirectLake or Import are supported, but the above mentioned tables uses the following modes: ", not_supported_modes)
        print("Ignoring these tables for testing.")

    partitions = partitions[partitions["Mode"].isin(["DirectLake","Import"])]
    relationships = relationships.merge(partitions.add_suffix(" From"), how="left", left_on="From Table", right_on="Table Name From")
    relationships = relationships.merge(partitions.add_suffix(" To"), how="left", left_on="To Table", right_on="Table Name To")

    lakehouse = resolve_lakehouse_from_semantic_model(semantic_model, workspace)
    
    print("Relationships fetched successfully.")
    
    table_names = _get_unique_datasource_table_names_from_relationships(relationships)
    print("Fetching table paths...")
    table_paths = get_table_paths(table_names=table_names, lakehouse=lakehouse)
    print("Table paths fetched successfully.")
    table_paths_info = {path.rsplit('/')[-1]: path for path in table_paths}
   
    # Load all tables into Spark dataframes
    tables = {}
    print("Loading tables into Spark DataFrames...")
    for table_name, path in table_paths_info.items():
        tables[table_name] = spark.read.load(path)
    print("Tables loaded successfully.")

    # Run the tests
    print("\n\n\nRunning tests...")
    test_dimensions(tables, relationships)
    test_facts(tables, relationships)
    test_relationships(tables, relationships)
    print("All tests completed.")


def _get_unique_datasource_table_names_from_relationships(relationships: pd.DataFrame) -> list[str]:
    """
    Extract unique table names from the relationships dictionary
    """
    unique_tables = list(set(relationships["Datasource Table Name From"].unique().tolist() + relationships["Datasource Table Name To"].unique().tolist()))
    unique_tables.sort()
    return unique_tables

if __name__ == "__main__":
    df = spark.createDataFrame(
        [
            ("1", "Anders", "001", "Lukket"),
            ("2", "must be overwritten", "002", "Åben"),
            ("3", "Claus", "003", "Lukket"),
        ],
        ["opportunity_id", "salesname_o", "salesnumber_o", "sales_status_t"],
    )
    test_dimension_unknown_row(df, key="opportunity_id", dimension="table_name")
    print("Test passed.")