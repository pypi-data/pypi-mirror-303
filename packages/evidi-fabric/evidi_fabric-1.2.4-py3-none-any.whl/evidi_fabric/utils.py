"""
The utils module contains utility functions for working with dataframes and other utilities in Fabric notebooks.

The module contains the following functions:
- add_concatenated_key: Adds a concatenated key to the dataframe
- add_default_scd2_cols: Adds the default SCD2 columns to the source dataframe
- add_unknown_row_to_df: Adds a row with default values for the columns of a dataframe
- generate_unknown_row: Generates a row with default values for the columns of a dataframe
- get_lastest_update: Get the lastest update timestamp from when the delta table was lastly updated
- get_merge_condition: Generates the merge condition for the merge operation in spark
- get_scd2_updates_with_overwrite: Generates the updates for SCD2 type 2 updates with overwrite
- get_scd2_updates: Generates the updates for SCD2 type 2 updates
- replace_invalid_col_names: Replaces illegal characters in columns names with underscore
- replace_null_values: Replaces null values in the specified columns with default values
- replace_too_old_timestamps: Replaces timestamps that are older than a threshold with the threshold timestamp
"""


from datetime import datetime
from decimal import Decimal
from delta.tables import DeltaTable
from evidi_fabric.spark import get_or_create_spark
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, expr, lit, date_format, to_timestamp, concat_ws, when
from pyspark.sql.types import TimestampType
from pyspark.sql import Row
from uuid import UUID
import re

from evidi_fabric.fs import get_table_path


def get_merge_condition(
	cols: list[str],
	dtypes: dict[str, str] | None = None,
	source_alias: str | None = None,
	target_alias: str | None = None,
) -> expr:
	"""
	Generates the merge condition for the merge operation in spark
	:param key_cols: List of columns that are used as keys for the merge operation
	:param dtypes: Dictionary of column names and their data types (can be found using dict(df.dtypes))
	:param source_alias: Alias of the source dataframe
	:param target_alias: Alias of the target dataframe
	:return: The merge condition as a spark expression
	"""
	if (source_alias and not target_alias) or (target_alias and not source_alias):
		raise ValueError("Both source_alias and target_alias must either be specified or empty not a mixture")

	use_alias = source_alias is not None
	if use_alias:
		if dtypes:
			conditions = []
			for col in cols:
				dtype = dtypes[col]
				if dtype == "string":
					conditions.append(f"COALESCE({source_alias}.{col},'') = COALESCE({target_alias}.{col},'')")
				elif dtype == "bigint":
					conditions.append(f"COALESCE({source_alias}.{col},-1) = COALESCE({target_alias}.{col},-1)")
				elif dtype[:7] == "decimal":
					conditions.append(f"COALESCE({source_alias}.{col},-1.0) = COALESCE({target_alias}.{col},-1.0)")
				elif dtype == "timestamp":
					conditions.append(
						f"COALESCE({source_alias}.{col},'1970-01-01 00:00:00') = COALESCE({target_alias}.{col},'1970-01-01 00:00:00')"
					)
				elif dtype == "double":
					conditions.append(f"COALESCE({source_alias}.{col},-1.0) = COALESCE({target_alias}.{col},-1.0)")
				elif dtype == "int":
					conditions.append(f"COALESCE({source_alias}.{col},-1) = COALESCE({target_alias}.{col},-1)")
				elif dtype == "date":
					conditions.append(
						f"COALESCE({source_alias}.{col},'1970-01-01') = COALESCE({target_alias}.{col},'1970-01-01')"
					)
				elif dtype == "boolean":
					conditions.append(f"COALESCE({source_alias}.{col}, false) = COALESCE({target_alias}.{col}, false)")
				else:
					raise ValueError(f"Unsupported data type: {dtype} for column: {col}")

			return expr(" AND ".join(conditions))
		else:
			return expr(" AND ".join([f"{source_alias}.{col} = {target_alias}.{col}" for col in cols]))
	else:
		return expr(" AND ".join(cols))


def _get_df_rows_to_be_overwritten(
	df_source: DataFrame, df_target: DataFrame, overwrite_cols: list[str], ids: list[str]
) -> DataFrame:
	select_expr = [f"source.{col}" for col in overwrite_cols] + [
		f"target.{col}" for col in df_target.columns if col not in overwrite_cols
	]
	where_clause = " OR ".join([f"source.{col} != target.{col}" for col in overwrite_cols])

	dtypes = dict(df_target.dtypes)
	merge_condition = get_merge_condition(cols=ids, dtypes=dtypes, source_alias="source", target_alias="target")
	df_rows_to_be_overwritten = (
		df_target.alias("target")
		.join(df_source.alias("source"), on=merge_condition, how="left")
		.filter(where_clause)
		.selectExpr(*select_expr)
	)
	return df_rows_to_be_overwritten


def add_concatenated_key(df: DataFrame, cols: list[str], key_col_name: str) -> DataFrame:
	"""
	Adds a concatenated key to the dataframe
	:param df: The dataframe
	:param cols: The columns that are to be concatenated
	:param key_col_name: The name of the new key column
	:return: The dataframe with the new key column
	"""
	select_cols = [key_col_name] + [c for c in df.columns if c != key_col_name]

	# Process columns, casting TimestampType to string with full timestamp format
	processed_cols = [
		date_format(col(c), "yyyyMMdd'T'HHmmssSSS").alias(c)
		if df.schema[c].dataType == TimestampType()
		else col(c).cast("string")
		for c in cols
	]

	# Add the concatenated key column
	df = df.withColumn(key_col_name, concat_ws("#", *processed_cols)).select(*select_cols)

	return df


def _validate_input(
	df: DataFrame, ids_tracked: list[str], cols_to_drop: list[str] = [], overwrite_cols: list[str] = []
) -> None:
	"""
	Validates the input dataframe
	:param df: The dataframe
	:param cols: The columns that are to be validated
	"""
	if cols_to_drop is None:
		cols_to_drop = []

	if overwrite_cols is None:
		overwrite_cols = []

	cols = df.columns

	illegal_cols_to_drop = [col for col in cols_to_drop if col in ids_tracked]
	if illegal_cols_to_drop:
		raise ValueError(
			f"The columns: {illegal_cols_to_drop} cannot be dropped as they are part of the tracked columns or ids columns"
		)

	reserved_col_names = ["valid_from" "valid_to" "valid_from_date_key" "valid_to_date_key" "IsDeleted"]

	illegal_cols = [col for col in reserved_col_names if col in cols]
	if illegal_cols:
		illegal_cols_str = ", ".join(illegal_cols)
		raise ValueError(f"The columns: {illegal_cols_str} are reserved and cannot be used in the dataframe")

	if any([col for col in overwrite_cols if col in ids_tracked]):
		impossible_cols = [col for col in overwrite_cols if col in ids_tracked]
		impossible_cols_str = ", ".join(impossible_cols)
		raise ValueError(f"The columns: {impossible_cols_str} cannot be tracked and overwritten at the same time!")


def get_scd2_updates(
	df_source: DataFrame,
	df_target: DataFrame,
	ids: list[str],
	tracked_cols: list[str],
	key_col_name: str = None,
	is_current_col: str = "is_current",
	current_datetime: datetime = datetime.now(),
	cols_to_drop: list[str] = [],
) -> DataFrame:
	"""
	Generates the updates for SCD2 type 2 updates
	:param df_source: The source dataframe
	:param df_target: The target dataframe
	:param ids: The columns that are used as keys for the merge operation
	:param tracked_cols: The columns that are tracked for changes
	:param is_current_col: The column that specifies if a row is the current row
	:param current_datetime: The current datetime
	:return: The updated and new rows in a dataframe
	"""
	keys = ids + tracked_cols + ["valid_from"]
	ids_tracked = ids + tracked_cols

	_validate_input(df_source, ids_tracked, cols_to_drop)

	df_source = add_default_scd2_cols(df_source, key_col_name, keys, current_datetime, is_current_col)
	df_target_current = df_target.filter(
		(col(is_current_col) == True) & (col("IsDeleted") == False)
	)  # Only update current rows

	dtypes = dict(df_source.dtypes)
	merge_condition_ids_tracked = get_merge_condition(
		cols=ids_tracked, dtypes=dtypes, source_alias="source", target_alias="target"
	)
	df_new_and_updated_rows = (
		df_source.alias("source")
		.join(df_target_current.alias("target"), on=merge_condition_ids_tracked, how="left_anti")
		.selectExpr("source.*")
	)

	# Get old rows from gold, which is getting changed
	merge_condition_ids = get_merge_condition(cols=ids, dtypes=dtypes, source_alias="source", target_alias="target")
	df_existing_rows_target = (
		df_target_current.alias("target")
		.join(df_new_and_updated_rows.alias("source"), on=merge_condition_ids, how="inner")
		.selectExpr("target.*")
		.withColumn(is_current_col, lit(False))
		.withColumn("valid_to", lit(current_datetime))
		.withColumn("valid_to_date_key", date_format(lit(current_datetime), "yyyyMMdd"))
	)

	df_deleted_rows = (
		df_target.alias("target")
		.filter(col("IsDeleted") == False)  # Only deletes that have not already been deleted
		.join(df_source.alias("source"), on=merge_condition_ids, how="left_anti")
		.selectExpr("target.*")
		.withColumn(is_current_col, lit(False))
		.withColumn("valid_to", lit(current_datetime))
		.withColumn("valid_to_date_key", date_format(lit(current_datetime), "yyyyMMdd"))
		.withColumn("IsDeleted", lit(True))
	)

	if key_col_name:
		df_new_and_updated_rows = add_concatenated_key(df_new_and_updated_rows, keys, key_col_name)
	df_scd2 = df_existing_rows_target.unionByName(df_new_and_updated_rows, allowMissingColumns=True).unionByName(
		df_deleted_rows, allowMissingColumns=True
	)

	df_scd2 = df_scd2.drop(*cols_to_drop) if cols_to_drop else df_scd2
	merge_condition = get_merge_condition(cols=ids_tracked, dtypes=dtypes, source_alias="source", target_alias="target")
	return df_scd2, merge_condition


def _update_df_scd2_with_overwritten_rows(
	df_source: DataFrame,
	df_target: DataFrame,
	df_scd2: DataFrame,
	ids: list[str],
	tracked_cols: list[str],
	overwrite_cols: list[str],
) -> DataFrame:
	"""
	Updates the SCD2 dataframe with the rows that are to be overwritten. It does so be first updating the existing df_scd2 with the new values and then adding the rows from the target that currently are not a part of df_scd2
	:parmamdf_source: The source dataframe
	:param df_target: The target dataframe
	:param df_scd2: The SCD2 dataframe
	:param ids: The columns that are used as keys for the merge operation
	:param overwrite_cols: The columns that are to be overwritten
	:return: The updated SCD2 dataframe
	"""
	keys = ids + tracked_cols + ["valid_from"]
	cols = df_scd2.columns
	select_expr = [f"source.{col}" for col in overwrite_cols] + [
		f"scd2.{col}" for col in df_scd2.columns if col not in overwrite_cols
	]

	dtypes = dict(df_scd2.dtypes)

	df_rows_to_be_overwritten = _get_df_rows_to_be_overwritten(df_source, df_target, overwrite_cols, ids)

	merge_condition_keys = get_merge_condition(cols=keys, dtypes=dtypes, source_alias="scd2", target_alias="overwrite")
	merge_condition_ids = get_merge_condition(cols=ids, dtypes=dtypes, source_alias="scd2", target_alias="source")
	df_scd2_updated = (
		df_scd2.alias("scd2")
		.join(
			df_source.alias("source"),  # source will always have the latest data
			on=merge_condition_ids,
			how="inner",
		)
		.selectExpr(select_expr)
		.unionByName(
			df_rows_to_be_overwritten.alias("overwrite")
			.join(
				df_scd2.alias("scd2"),
				on=merge_condition_keys,
				how="leftanti",
			)
			.selectExpr("overwrite.*"),
			allowMissingColumns=True,
		)
		.unionByName(df_scd2.filter(col("IsDeleted") == True), allowMissingColumns=True)
		.select(*cols)
	)

	merge_condition = get_merge_condition(cols=keys, dtypes=dtypes, source_alias="source", target_alias="target")
	return df_scd2_updated, merge_condition


def add_default_scd2_cols(
	df: DataFrame,
	key_col_name: str = None,
	key_cols: list[str] = None,
	current_datetime: datetime = datetime.now(),
	is_current_col: str = "is_current",
) -> DataFrame:
	"""
	Adds the default SCD2 columns to the source dataframe
	:param df_source: The source dataframe
	:param current_datetime: The current datetime
	:param is_current_col: The column that specifies if a row is the current row
	:return: The source dataframe with the default SCD2 columns added
	"""

	org_cols = df.columns
	df = (
		df.withColumn(is_current_col, lit(True))
		.withColumn("valid_from", lit(current_datetime))
		.withColumn("valid_to", to_timestamp(lit("9999-12-31")))
		.withColumn("valid_from_date_key", date_format(lit(current_datetime), "yyyyMMdd"))
		.withColumn("valid_to_date_key", lit("99991231"))
		.withColumn("IsDeleted", lit(False))
	)

	if key_col_name is None:
		select_cols = org_cols + [
			is_current_col,
			"valid_from",
			"valid_to",
			"valid_from_date_key",
			"valid_to_date_key",
			"IsDeleted",
		]

	else:
		if key_cols is None:
			raise ValueError("key_cols must be provided when key_col_name is specified.")

		select_cols = (
			[key_col_name]
			+ org_cols
			+ [is_current_col, "valid_from", "valid_to", "valid_from_date_key", "valid_to_date_key", "IsDeleted"]
		)
		df = add_concatenated_key(df, key_cols, key_col_name)

	df = df.select(*select_cols)
	return df


def get_scd2_updates_with_overwrite(
	df_source: DataFrame,
	df_target: DataFrame,
	ids: list[str],
	tracked_cols: list[str],
	key_col_name: str = None,
	overwrite_cols: list[str] | None = None,
	is_current_col: str = "is_current",
	current_datetime: datetime = datetime.now(),
	cols_to_drop: list[str] = [],
) -> DataFrame:
	"""
	Generates the updates for SCD2 type 2 updates
	:param df_source: The source dataframe
	:param df_target: The target dataframe
	:param ids: The columns that are used as keys for the merge operation
	:param tracked_cols: The columns that are tracked for changes
	:param overwrite_cols: The columns that are to be overwritten
	:param is_current_col: The column that specifies if a row is the current row
	:param current_datetime: The current datetime
	:return: The updated and new rows in a dataframe

	Example of usage:
	df, merge_condition = get_scd2_updates_with_overwrite(df_source = df_salessilver,
																																																					  df_target = df_gold,
																																																					  ids = ["opportunityid"],
																																																					  tracked_cols = ["sales_status"],
																																																					  overwrite_cols = ["salesname", "salesnumber"],
																																																					  current_datetime=current_datetime)
	"""
	ids_tracked = ids + tracked_cols
	_validate_input(df_source, ids_tracked, cols_to_drop, overwrite_cols)

	df_scd2, merge_condition = get_scd2_updates(
		df_source, df_target, ids, tracked_cols, key_col_name, is_current_col, current_datetime
	)
	if overwrite_cols:
		df_scd2, merge_condition = _update_df_scd2_with_overwritten_rows(
			df_source, df_target, df_scd2, ids, tracked_cols, overwrite_cols
		)

	df_scd2 = df_scd2.drop(*cols_to_drop) if cols_to_drop else df_scd2
	return df_scd2, merge_condition


def replace_null_values(
	df: DataFrame,
	cols: list[str] = None,
	default_int: int = -1,
	default_bigint: int = -1,
	default_str: str = "Unknown",
	default_datetime: datetime = datetime(1901, 1, 1).strftime(
		"%Y-%m-%d %H:%M:%S"
	),  # STILL INTERPRETED AS DATETIME IN SPARK
	default_date: datetime = datetime(1901, 1, 1).strftime(
		"%Y-%m-%d"
	),  # STILL INTERPRETED AS DATE IN SPARK
	default_decimal: float = 0.0,
	default_timestamp: datetime = datetime(1901, 1, 1).strftime(
		"%Y-%m-%d %H:%M:%S"
	),  # STILL INTERPRETED AS DATETIME IN SPARK
	default_double: float = 0.0,
	default_boolean: bool = False,
):
	"""
	Replaces null values in the specified columns with default values
	"""
	dtypes = dict(df.dtypes)
	default_values = {}

	if cols is None:
		cols = df.columns

	for column in cols:
		try:
			dtype = dtypes[column]
		except KeyError:
			raise ValueError(f"Column: {column} not found in dataframe")

		if dtype == "string":
			default_values[column] = default_str
		elif dtype == "int":
			default_values[column] = default_int
		elif dtype == "bigint":
			default_values[column] = default_bigint
		elif dtype == "datetime":
			default_values[column] = default_datetime
		elif dtype == "date":
			default_values[column] = default_date
		elif dtype[:7] == "decimal":
			default_values[column] = default_decimal
		elif dtype == "timestamp":
			default_values[column] = default_timestamp
		elif dtype[:7] == "double":
			default_values[column] = default_double
		elif dtype == "boolean":
			default_values[column] = default_boolean
		else:
			raise ValueError(f"Unsupported data type: {dtype} for column: {column}")

	return df.fillna(default_values)

def generate_unknown_row(
	df: DataFrame,
	default_int: int = -1,
	default_bigint: int = -1,
	default_str: str = "Unknown",
	default_datetime: datetime = datetime(1901, 1, 1),
	default_decimal: Decimal = Decimal('0.0'),
	default_timestamp: datetime = datetime(1901, 1, 1),
	default_double: float = 0.0,
	default_boolean: bool = False,
) -> DataFrame:
	"""
	Generates a row with default values for the columns of a dataframe
	"""
	spark = get_or_create_spark()
	dtypes = dict(df.dtypes)
	unknown_row = {}
	cols = df.columns
	for column in cols:
		dtype = dtypes[column]
		if dtype == "string":
			unknown_row[column] = default_str
		elif dtype == "int":
			unknown_row[column] = default_int
		elif dtype == "bigint":
			unknown_row[column] = default_bigint
		elif dtype == "datetime" or dtype == "date":
			unknown_row[column] = default_datetime
		elif dtype[:7] == "decimal":
			unknown_row[column] = default_decimal
		elif dtype == "timestamp":
			unknown_row[column] = default_timestamp
		elif dtype[:7] == "double":
			unknown_row[column] = default_double
		elif dtype == "boolean":
			unknown_row[column] = default_boolean
		else:
			raise ValueError(f"Unsupported data type: {dtype} for column: {column}")

	unknown_row = Row(**unknown_row)
	df_extra = spark.createDataFrame([unknown_row], df.schema)
	return df_extra

def replace_too_old_timestamps(df:DataFrame, columns:list | None = None, threshold_timestamp_str: str = "1900-01-01") -> DataFrame:
	"""
	Replaces timestamps that are older than a threshold with the threshold timestamp
	
	:param df: The dataframe
	:param columns: The columns that are to be replaced
	:param threshold_timestamp_str: The threshold timestamp as a string
	:return: The dataframe with the timestamps replaced

	Author: Torben Nyvang Jakobsen
	"""

	if columns is None:
		columns = df.columns

	threshold_timestamp = to_timestamp(lit(threshold_timestamp_str))
	
	# Iterate over all columns and apply the transformation if the column is of TimestampType
	for col_name, col_type in df.dtypes:
		if col_type == "timestamp":
			df = df.withColumn(
				col_name,
				when(col(col_name) < threshold_timestamp, threshold_timestamp)
				 .otherwise(col(col_name))
			)
	return df


def add_unknown_row_to_df(
	df: DataFrame,
	default_int: int = -1,
	default_bigint: int = -1,
	default_str: str = "Unknown",
	default_datetime: datetime = datetime(1901, 1, 1),
	default_decimal: Decimal = Decimal('0.0'),
	default_timestamp: datetime = datetime(1901, 1, 1),
	default_double: float  = 0.0,
	default_boolean: bool = False,
) -> DataFrame:
	"""
	Adds a row with default values for the columns of a dataframe
	"""
	df_unknown_row = generate_unknown_row(
		df,
		default_int=default_int,
		default_bigint=default_bigint,
		default_str=default_str,
		default_datetime=default_datetime,
		default_decimal=default_decimal,
		default_timestamp=default_timestamp,
		default_double=default_double,
		default_boolean=default_boolean,
	)
	df = df_unknown_row.unionByName(df)
	return df

def replace_invalid_col_names(df:DataFrame, pattern:str=r"[-',.;:{}()<>\n\t=/° ]") -> DataFrame:
	"""
	Replaces illegal characters in columns names with underscore.

	Args:
		- df (DataFrame): The input DataFrame with potentially invalid column names.
		- pattern: regex expression determine illegal characters

	Returns:
		- DataFrame: A new DataFrame with invalid characters replaced by underscores.

	Examples:
		- df_rename = replace_invalid_col_names(df)
	"""

	renamer={col:re.sub(pattern, "_", col) for col in df.columns if re.sub(pattern, "_", col)!=col}
	for org_name in renamer.keys():
		if org_name in df.columns:
			df=df.withColumnRenamed(org_name, renamer[org_name])
	return df

def get_lastest_update(table_name:str, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> datetime:
	"""
	Get the lastest update timestamp from when the delta table was lastly updated
	
	:param 
		table_name: The name of the table
		lakehouse: The name of the lakehouse
		workspace: The name of the workspace
	
	:return: The last update timestamp as a datetime in utc timezone"""
	path = get_table_path(table_name, lakehouse=lakehouse, workspace=workspace)
	delta_table = DeltaTable.forPath(spark, path)
	history_df = delta_table.history(1)
	lastest_update_row = history_df.select("timestamp").collect()
	lastest_update_utc = lastest_update_row[0]["timestamp"]
	return lastest_update_utc

if __name__ == "__main__":
	from datetime import timedelta

	spark = get_or_create_spark()
	ids = ["opportunity_id"]
	tracked_cols = ["sales_status_t"]
	overwrite_cols = ["salesname_o", "salesnumber_o"]
	key_col_name = None  # "opportunity_key"
	current_datetime = datetime.now()
	df_source = spark.createDataFrame(
		[
			("1", "Anders", "001", "Lukket"),
			("2", "must be overwritten", "002", "Åben"),
			("3", "Claus", "003", "Lukket"),
		],
		["opportunity_id", "salesname_o", "salesnumber_o", "sales_status_t"],
	)

	df_target = spark.createDataFrame(
		[("1", "Anders", "001", "Åben"), ("2", "Bent", "002", "Åben")],
		["opportunity_id", "salesname_o", "salesnumber_o", "sales_status_t"],
	)
	id_cols = ids  # + tracked_cols
	key_cols = ids + tracked_cols + ["valid_from"]
	df_target = add_default_scd2_cols(
		df_target,
		key_col_name,
		key_cols,
		current_datetime=datetime.now() - timedelta(days=1),
		is_current_col="is_current",
	)

	# Sealing Scenario
	ids = ["opportunityid"]
	tracked_cols = ["sales_status"]
	overwrite_cols = ["salesname", "salesnumber", "current_status"]
	key_col_name = "opportunity_key"

	df = spark.createDataFrame([(1, datetime(2024, 1, 1), 1), (2, None, 1)], ["row", "valid_from", "row"])
	df = add_unknown_row_to_df(df)
	df = replace_null_values(df)

	df_source = spark.createDataFrame(
		[("173ee108-8351-44b4-a5ca-3f6dfa254bf5", "23-427 test navn", "23-427", "Super tabt", "Super tabt")],
		["opportunityid", "salesname", "salesnumber", "sales_status", "current_status"],
	)

	from pyspark.sql.types import StructType, StructField, StringType, BooleanType, TimestampType, IntegerType

	schema = StructType(
		[
			StructField("opportunity_key", StringType(), True),
			StructField("opportunityid", StringType(), True),
			StructField("salesname", StringType(), True),
			StructField("salesnumber", StringType(), True),
			StructField("sales_status", StringType(), True),
			StructField("current_status", StringType(), True),
			StructField("is_current", BooleanType(), True),
			StructField("valid_from", TimestampType(), True),
			StructField("valid_to", TimestampType(), True),
			StructField("valid_from_date_key", IntegerType(), True),
			StructField("valid_to_date_key", IntegerType(), True),
			StructField("IsDeleted", BooleanType(), True),
		]
	)

	df_target = spark.createDataFrame(
		[
			(
				"173ee108-8351-44b4-a5ca-3f6dfa254bf5#Åben#20240620T113018709",
				"173ee108-8351-44b4-a5ca-3f6dfa254bf5",
				"23-427 Wrap around salatost",
				"23-427",
				"Åben",
				"Åben",
				False,
				datetime(2024, 6, 20, 15, 30, 18, 709000),
				datetime(2024, 6, 26, 14, 3, 21, 816000),
				20240620,
				20240626,
				False,
			),
			(
				"173ee108-8351-44b4-a5ca-3f6dfa254bf5#Super vundet#20240626T100321816",
				"173ee108-8351-44b4-a5ca-3f6dfa254bf5",
				"23-427 Wrap around salatost",
				"23-427",
				"Super vundet",
				"Åben",
				False,
				datetime(2024, 6, 26, 14, 3, 21, 816000),
				datetime(2024, 6, 26, 18, 3, 40, 88000),
				20240626,
				20240626,
				False,
			),
			(
				"173ee108-8351-44b4-a5ca-3f6dfa254bf5#Åben#20240626T140340088",
				"173ee108-8351-44b4-a5ca-3f6dfa254bf5",
				"23-427 Wrap around salatost",
				"23-427",
				"Åben",
				"Åben",
				True,
				datetime(2024, 6, 26, 18, 3, 40, 88000),
				datetime(9999, 12, 31, 23, 4, 0, 0),
				20240626,
				99991231,
				False,
			),
		],
		[
			"opportunity_key",
			"opportunityid",
			"salesname",
			"salesnumber",
			"sales_status",
			"current_status",
			"is_current",
			"valid_from",
			"valid_to",
			"valid_from_date_key",
			"valid_to_date_key",
			"IsDeleted",
		],
	)

	# df_delete = spark.createDataFrame(
	#     [
	#         (
	#             # "3#Lukket#2024061908T2808802",
	#             "3",
	#             "Claus",
	#             "003",
	#             "Lukket",
	#             False,
	#             datetime(2024, 6, 18, 10, 28, 8, 802416),
	#             datetime(2024, 6, 19, 10, 28, 8, 802416),
	#             "20240618",
	#             "20240619",
	#             True,
	#         )
	#     ],
	#     [
	#         # "opportunity_key",
	#         "opportunity_id",
	#         "salesname_o",
	#         "salesnumber_o",
	#         "sales_status_t",
	#         "is_current",
	#         "valid_from",
	#         "valid_to",
	#         "valid_from_date_key",
	#         "valid_to_date_key",
	#         "IsDeleted",
	#     ],
	# )

	# df_target = df_target.unionByName(df_delete)

	select_cols = [key_col_name] + [col for col in df_target.columns]

	# df_target = add_concatenated_key(df_target, key_cols, key_col_name)
	cols_to_drop = []  # ["opportunity_id"]
	df_target = df_target.drop(*cols_to_drop)

	print("target")
	print(df_target.sort("valid_from").show())

	print("source")
	print(df_source.show())

	key_col_name = None

	df_scd2, merge_condition = get_scd2_updates(
		df_source=df_source,
		df_target=df_target,
		ids=ids,
		tracked_cols=tracked_cols,
		key_col_name=key_col_name,  # key_col_name,
		is_current_col="is_current",
		current_datetime=current_datetime,
		cols_to_drop=cols_to_drop,
	)

	# print(df_scd2.show())
	df_scd2_wo, merge_condition_wo = get_scd2_updates_with_overwrite(
		df_source=df_source,
		df_target=df_target,
		ids=ids,
		tracked_cols=tracked_cols,
		key_col_name=key_col_name,
		overwrite_cols=overwrite_cols,
		is_current_col="is_current",
		current_datetime=current_datetime,
		cols_to_drop=cols_to_drop,
	)

	print("df_scd2 with overwrite")
	print(df_scd2_wo.sort("valid_from").show())
	print("hertil!")