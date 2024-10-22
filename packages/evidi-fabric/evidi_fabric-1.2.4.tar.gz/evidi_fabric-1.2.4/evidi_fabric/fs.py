"""
The `fs` module provides functions for file system operations, focusing on managing tables and shortcuts within lakehouses and workspaces. 

This module includes functions for retrieving table paths, resolving workspace and lakehouse names and IDs, and managing shortcuts. The functions facilitate operations such as deleting shortcuts, dropping tables, and replacing tables or shortcuts.

Functions:
- create_shortcut_onelake: Creates a shortcut for a table in a lakehouse.
- delete_shortcut: Deletes a shortcut for a table in a specified lakehouse within a workspace.
- drop_all_tables_and_shortcuts: Drops all tables and shortcuts in the specified lakehouse and workspace, optionally limiting the operation to a specified list of tables.
- drop_table_or_shortcut: Drops the given table if it is a shortcut or an actual table in the specified lakehouse within a workspace.
- get_file_path: Retrieves a fully qualified file path.
- get_all_tables_in_lakehouse: Retrieves all tables in the specified lakehouse and workspace.
- get_all_table_paths_in_lakehouse: Retrieves all table paths in the specified lakehouse and workspace.
- get_lakehouse_from_path: Retrieves the lakehouse name from a path.
- get_lakehouse_tables_info: Retrieves the table names and related info from the lakehouse.
- get_table_from_file_or_folder: Retrieves the table name from a file or folder path.
- get_table_path: Retrieves a fully qualified table path.
- get_table_paths: Retrieves a list of fully qualified table paths.
- get_tables_from_files_or_folders: Retrieves the table names from a list of files or folders.
- is_shortcut: Returns True if the shortcut exists, otherwise False.
- ls: Lists all tables or files in the specified lakehouse and workspace.
- replace_all_tables_or_shortcuts: Replaces all tables or shortcuts from the source lakehouse to the destination lakehouse, with options to exclude specific tables and control the replacement behavior.
- resolve_lakehouse_id: Retrieves the lakehouse ID from the lakehouse name.
- resolve_lakehouse_name: Retrieves the lakehouse name from the lakehouse ID.
- resolve_workspace_id: Retrieves the workspace ID from the workspace name.
- resolve_workspace_name: Retrieves the workspace name from the workspace ID.
- shortcut_not_already_shortcutted_tables: Creates shortcuts for tables that are not already shortcutted.
"""
from datetime import datetime
from notebookutils import mssparkutils
from notebookutils.mssparkutils.handlers.fsHandler import FileInfo
from pyspark.sql import DataFrame
from pyspark.sql.session import SparkSession
from uuid import UUID
import pandas as pd
import requests
import sempy.fabric as fabric
import time

try:
	spark
except NameError:
	from evidi_fabric.spark import get_or_create_spark
	spark = get_or_create_spark()

def _is_valid_uuid(val):
	try:
		UUID(str(val))
		return True
	except ValueError:
		return False


def get_tables_from_files_or_folders(files_or_folders: list[str]):
	"""
	Either all files from bronze is passed from bronze til silver, or only a single file.
	This function will return a list of the table names
	"""
	return [get_table_from_file_or_folder(file_or_folder) for file_or_folder in files_or_folders]


def get_table_from_file_or_folder(file_or_folder: str):
	"""
	Either all files from bronze is passed from bronze til silver, or only a single file.
	This function will return the table name, by assuming the name of the silver table is
	the name of the folder where the file is located.

	This function looks after a "." in the file_or_folder string. If there is a dot, then
	it must be a full path if it's not, then its assumed to point to th

	E.g.
			file_or_folder='table_name/20240101_filname.parquet' -> 'table_name'
			file_or_folder='table_name' -> 'table_name'
			file_or_folder='parent_folder/table_name' -> 'table_name'
			file_or_folder='filename.parquet' -> ValueError #Path must be specified

	"""
	if "." in file_or_folder:
		if "/" in file_or_folder:
			return file_or_folder.split("/")[-2]
		else:
			raise ValueError("At least the relative path must be specified")
	else:
		if "/" in file_or_folder:
			return file_or_folder.split("/")[-1]
		else:
			return file_or_folder


def get_file_path(
	directory: str = None, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None
) -> str:
	"""
	Retrieves a fully qualified file path.
	Note:

	Params:
	 - workspace: Name or id of workspace (e.g. Decide_DK_DEV, 7dae828c-f98e-4e08-aaae-d93b2774c74b, None)
			* If not provided, the current workspace is used
	 - lakehouse: Name or id of the lakehouse (e.g. Decide_DK_Silver, 9be79118-d950-4662-8053-b393d021ab0f, None)
			* If not provided, the current lakehouse is used
	 - directory: Name of the directory (e.g. Bronze)

	Output:
	 - path (e.g. abfss://Decide_DK_DEV@onelake.dfs.fabric.microsoft.com/Decide_DK_Silver.Lakehouse/Files/Bronze/)

	Note: If either workspace name or lakehouse name contains a space, the method will fall back to use the workspace
	and lakehouse ids instead of names.
	"""
	lakehouse_path = get_lakehouse_path(lakehouse, workspace)
	return f"{lakehouse_path}/Files/{directory}"


def get_table_paths(
	table_names: list[str], lakehouse: str | UUID | None = None, workspace: str | UUID | None = None
) -> str:
	"""
	Retrieves a list of fully qualified table paths.

	Params:
	 - table_names: List of table names (e.g. [A__CUSTGROUP, A__CUSTTABLE])
	 - workspace: Name or id of workspace (e.g. Decide_DK_DEV, 7dae828c-f98e-4e08-aaae-d93b2774c74b, None)
			* If not provided, the current workspace is used
	 - lakehouse: Name or id of the lakehouse (e.g. Decide_DK_Silver, 9be79118-d950-4662-8053-b393d021ab0f, None)
			* If not provided, the current lakehouse is used

	Output:
			- paths (e.g. ["abfss://Decide_DK_DEV@onelake.dfs.fabric.microsoft.com/Decide_DK_Silver.Lakehouse/Tables/A__CUSTGROUP/",...]

	Note: If either workspace name or lakehouse name contains a space, the method will fall back to use the workspace
	and lakehouse ids instead of names.
	"""
	lakehouse_path = get_lakehouse_path(lakehouse, workspace)
	return [
		f"{lakehouse_path}/Tables/{table_name}"
		for table_name in table_names
	]

def get_table(table_name: str, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> DataFrame:
	"""
	Retrieves a table from the lakehouse.

	Params:
	 - table_names: List of table names (e.g. [A__CUSTGROUP, A__CUSTTABLE])
	 - workspace: Name or id of workspace (e.g. Decide_DK_DEV, 7dae828c-f98e-4e08-aaae-d93b2774c74b, None)
			* If not provided, the current workspace is used
	 - lakehouse: Name or id of the lakehouse (e.g. Decide_DK_Silver, 9be79118-d950-4662-8053-b393d021ab0f, None)
			* If not provided, the current lakehouse is used

	Output:
		spark dataframe with the table
	"""
	table_path = get_table_path(table_name, lakehouse, workspace)
	return spark.read.load(table_path)


def get_table_path(table_name: str, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> str:
	"""
	Retrieves a fully qualified table path.

	Params:
	 - table_name: Name of the table (e.g. A__CUSTGROUP)
	 - workspace: Name or id of workspace (e.g. Decide_DK_DEV, 7dae828c-f98e-4e08-aaae-d93b2774c74b, None)
			* If not provided, the current workspace is used
	 - lakehouse: Name or id of the lakehouse (e.g. Decide_DK_Silver, 9be79118-d950-4662-8053-b393d021ab0f, None)
			* If not provided, the current lakehouse is used

	Output:
	 - path (e.g. abfss://Decide_DK_DEV@onelake.dfs.fabric.microsoft.com/Decide_DK_Silver.Lakehouse/Tables/A__CUSTGROUP/

	Note: If either workspace name or lakehouse name contains a space, the method will fall back to use the workspace
	and lakehouse ids instead of names.
	"""
	lakehouse_path  = get_lakehouse_path(lakehouse, workspace)
	return f"{lakehouse_path}/Tables/{table_name}"


def get_lakehouse_path(lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> str:
	"""
	Retrieves a fully qualified lakehouse path.

	Params:
	 - lakehouse: Name or id of the lakehouse (e.g. Decide_DK_Silver, 9be79118-d950-4662-8053-b393d021ab0f, None)
			* If not provided, the current lakehouse is used
	 - workspace: Name or id of workspace (e.g. Decide_DK_DEV, 7dae828c-f98e-4e08-aaae-d93b2774c74b, None)
			* If not provided, the current workspace is used

	Output:
	 - path (e.g. abfss://Decide_DK_DEV@onelake.dfs.fabric.microsoft.com/Decide_DK_Silver.Lakehouse)
	 """
	workspace_name = resolve_workspace_name(workspace)
	lakehouse_name = resolve_lakehouse_name(lakehouse, workspace=workspace)
	if " " in workspace_name or " " in lakehouse_name:
		workspace_id = resolve_workspace_id(workspace)
		lakehouse_id = resolve_lakehouse_id(lakehouse, workspace=workspace)
		return f"abfss://{workspace_id}@onelake.dfs.fabric.microsoft.com/{lakehouse_id}"
	return f"abfss://{workspace_name}@onelake.dfs.fabric.microsoft.com/{lakehouse_name}.Lakehouse"


def get_lakehouse_from_path(path: str) -> str:
	"""
	Retrieves the lakehouse name from a path.

	Example:
	path = "abfss://Decide_DK_DEV@onelake.dfs.fabric.microsoft.com/Decide_DK_Bronze.Lakehouse/Files/Bronze/"
	lakehouse = "Decide_DK_Bronze"
	"""
	if "/Files" in path:
		lakehouse = path.split("onelake.dfs.fabric.microsoft.com/")[-1].split("/Files")[0].replace(".Lakehouse", "")
	elif "/Tables" in path:
		lakehouse = path.split("onelake.dfs.fabric.microsoft.com/")[-1].split("/Tables")[0].replace(".Lakehouse", "")
	else:
		raise ValueError("The path is not a valid lakehouse path.")
	return lakehouse


def resolve_workspace_id(workspace: str | UUID | None = None) -> UUID:
	"""
	From the workspace, that can be either the name, guid or None, resolve the workspace id.
	If no workspace is provided, the current workspace is used.
	"""
	if workspace is None:
		workspace_id = fabric.get_workspace_id()
	elif _is_valid_uuid(workspace):
		workspace_id = workspace
	else:
		workspace_id = fabric.resolve_workspace_id(workspace)

	return workspace_id


def resolve_workspace_name(workspace: str | UUID | None = None) -> str:
	"""
	From the workspace, that can be either the name, guid or None, retrieve the workspace name.
	If no workspace id provided, the current workspace is used.
	"""
	if workspace is None:
		workspace_id = resolve_workspace_id()
		workspace_name = fabric.resolve_workspace_name(workspace_id)

	elif not _is_valid_uuid(workspace):
		workspace_name = workspace

	else:
		workspace_id = workspace
		workspace_name = fabric.resolve_workspace_name(workspace_id)

	return workspace_name


def resolve_lakehouse_id(lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> UUID:
	"""
	From the lakehouse name, that can be either the name, guid or None, retrieves the lakehouse id.
	If no lakehouse name is provided, the current lakehouse is used.
	"""
	workspace_name = resolve_workspace_name(workspace)

	if lakehouse is None:
		lakehouse_id = fabric.get_lakehouse_id()

	elif _is_valid_uuid(lakehouse):
		lakehouse_id = lakehouse

	else:
		df_items = fabric.list_items("Lakehouse", workspace=workspace_name)
		df_items = df_items[df_items["Display Name"] == lakehouse]

		try:
			lakehouse_id = df_items["Id"].iloc[0]
		except IndexError:
			raise ValueError(f"Lakehouse: {lakehouse} does not exists in workspace {workspace_name}.")

	return lakehouse_id


def resolve_lakehouse_name(
	lakehouse: str | UUID | None = None, workspace: str | UUID | None = None, check_if_exists: bool = False
) -> str:
	"""
	From the lakehouse, that can be either the name, guid or None, retrieves the lakehouse name.
	If no lakehouse id is provided, the current lakehouse is used.
	"""
	workspace_name = resolve_workspace_name(workspace)

	if lakehouse is None:
		lakehouse_id = resolve_lakehouse_id(workspace, workspace=workspace)
	elif not _is_valid_uuid(lakehouse):
		lakehouse_name = lakehouse
		return lakehouse_name
	else:
		lakehouse_id = lakehouse

	if check_if_exists:
		df_items = fabric.list_items("Lakehouse", workspace=workspace_name)
		df_items = df_items[df_items["Id"] == lakehouse_id]
		try:
			lakehouse_name = df_items["Display Name"].iloc[0]
		except IndexError:
			raise ValueError(f"Lakehouse: {lakehouse} does not exists in workspace {workspace_name}.")

	return lakehouse_name


def get_lakehouse_tables_info(
	spark: SparkSession = None, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None
) -> pd.DataFrame:
	"""
	Retrieves the table names and related infos from the lakehouse.
	Note: the faster method is to use the sempy API. However, due to a presumably temporary
			  pagination error, it is limited to 100 tables.
			  If the number of tables equals to exactly 100, the method falls back to the spark API.
			  This code should be modified (by removing the first part of the if condition) once the issue is resolved.

	If workspace is not provided, the current workspace is used
	If lakehouse is not provided, the current lakehouse is used
	"""

	workspace_id = resolve_workspace_id(workspace)
	workspace_name = resolve_workspace_name(workspace)
	lakehouse_id = resolve_lakehouse_id(lakehouse, workspace=workspace)
	lakehouse_name = resolve_lakehouse_name(lakehouse, workspace=workspace)

	client = fabric.FabricRestClient()
	response = client.get(f"/v1/workspaces/{workspace_id}/lakehouses/{lakehouse_id}/tables")
	table_list = response.json()["data"]
	if len(table_list) == 100:
		warn_msg = "Warning: The sempy API is truncated to show 100 tables."
		warn_msg += "\nFailing back to the spark API to retrieve all tables."
		warn_msg += "\nThis method is significantly slower."
		print(warn_msg)
		if not spark:
			spark = get_or_create_spark()
		tables = spark.catalog.listTables()
		table_paths = get_table_paths(
			[table.name for table in tables], lakehouse=lakehouse_name, workspace=workspace_name
		)
		table_paths_dict = {table_path.rsplit("/")[-1]: table_path for table_path in table_paths}
		table_list_formatted = [
			{
				"Workspace Name": workspace_name,
				"Workspace ID": workspace_id,
				"Lakehouse Name": lakehouse_name,
				"Lakehouse ID": lakehouse_id,
				"Table Name": table.name,
				"Type": table.tableType,
				"Location": table_paths_dict[table.name],
				"Format": None,
				"Is Temporary": table.isTemporary,
				"Description": table.description,
			}
			for table in tables
		]
	else:
		table_list_formatted = [
			{
				"Workspace Name": workspace_name,
				"Workspace ID": workspace_id,
				"Lakehouse Name": lakehouse_name,
				"Lakehouse ID": lakehouse_id,
				"Table Name": table["name"],
				"Type": table["type"],
				"Location": table["location"],
				"Format": table["format"],
				"Is Temporary": None,
				"Description": None,
			}
			for table in table_list
		]

	return pd.DataFrame(table_list_formatted)


def is_shortcut(shortcut_name: str, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None, sub_directory:str="Tables"):
	"""
	Returns True if the shortcut exists, otherwise False.

	Parameters:
	- shortcut_name (str): The name of the shortcut to be deleted.
	- lakehouse (str | UUID | None, optional): The name or UUID of the lakehouse containing the shortcut. Defaults to None.
	- workspace (str | UUID | None, optional): The name or UUID of the workspace containing the lakehouse. Defaults to None.
	- sub_directory (str): The sub-directory to list tables or files from. Must be either "Tables" or at least start with "Files". Defaults to "Tables".

	Returns:
	bool: True if the shortcut exists, otherwise False.

	Example usage:
	is_shortcut(
			shortcut_name="ExampleTable",
			lakehouse="SolvLakehouse",
			workspace="DP_DEV"
	)

	This function performs the following steps:
	1. Resolves the workspace ID from the provided workspace name or UUID.
	2. Resolves the lakehouse ID from the provided lakehouse name or UUID within the specified workspace.
	3. Creates a client instance of the FabricRestClient to communicate with the service.
	4. Sends a GET request to the API endpoint to check if the specified shortcut exists.
	5. Returns True if the shortcut exists, otherwise False.
	"""
	if not (sub_directory == "Tables" or sub_directory.startswith("Files")):
		raise ValueError("The sub_directory must be either 'Tables' or 'Files'.")
	
	workspace_id = resolve_workspace_id(workspace)
	lakehouse_id = resolve_lakehouse_id(lakehouse, workspace=workspace)
	client = fabric.FabricRestClient()

	try:
		response = client.get(f"v1/workspaces/{workspace_id}/items/{lakehouse_id}/shortcuts/{sub_directory}/{shortcut_name}")
		return response.status_code == 200
	except fabric.exceptions.FabricHTTPException:
		# TODO: Below fails even if a table exists, hence the below is commented out
		# err_response = err.response.json()
		# if err_response["errorCode"] == "EntityNotFound":
		#     raise
		return False


def delete_shortcut(shortcut_name: str, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None):
	"""
	Deletes a shortcut for a table in a specified lakehouse within a workspace.

	Parameters:
	- shortcut_name (str): The name of the shortcut to be deleted.
	- lakehouse (str | UUID | None, optional): The name or UUID of the lakehouse containing the shortcut. Defaults to None.
	- workspace (str | UUID | None, optional): The name or UUID of the workspace containing the lakehouse. Defaults to None.

	Returns:
	None

	Example usage:
	delete_shortcut(
			shortcut_name="ExampleTable",
			lakehouse="SolvLakehouse",
			workspace="DP_DEV"
	)

	This function performs the following steps:
	1. Resolves the workspace ID from the provided workspace name or UUID.
	2. Resolves the lakehouse ID from the provided lakehouse name or UUID within the specified workspace.
	3. Creates a client instance of the FabricRestClient to communicate with the service.
	4. Sends a DELETE request to the API endpoint to delete the specified shortcut.
	5. Prints a confirmation message if the deletion is successful, or a warning message if it fails.
	"""

	workspace_id = resolve_workspace_id(workspace)
	lakehouse_id = resolve_lakehouse_id(lakehouse, workspace=workspace)
	client = fabric.FabricRestClient()
	response = client.delete(f"/v1/workspaces/{workspace_id}/items/{lakehouse_id}/shortcuts/Tables/{shortcut_name}")

	if response.status_code == 200:
		print(
			f"The '{shortcut_name}' shortcut in the '{lakehouse}' within the '{workspace}' workspace has been deleted."
		)
	else:
		print(f"WARNING: The '{shortcut_name}' has not been deleted.")


def drop_table_or_shortcut(table_name: str, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None):
	"""
	Drops the given table if it is a shortcut or an actual table in the specified lakehouse within a workspace.
	The source of the table is not affected.

	Parameters:
	- table_name (str): The name of the table or shortcut to be dropped.
	- lakehouse (str | UUID | None, optional): The name or UUID of the lakehouse containing the table. Defaults to None.
	- workspace (str | UUID | None, optional): The name or UUID of the workspace containing the lakehouse. Defaults to None.

	Returns:
	None

	Example usage:
	drop_table_or_shortcut(
			table_name="ExampleTable",
			lakehouse="SolvLakehouse",
			workspace="DP_DEV"
	)

	This function performs the following steps:
	1. Resolves the full path to the table within the lakehouse and workspace.
	2. Resolves the workspace ID from the provided workspace name or UUID.
	3. Resolves the lakehouse ID from the provided lakehouse name or UUID within the specified workspace.
	4. Attempts to retrieve the shortcut information from the REST API.
	5. If the table is found to be a shortcut, it calls `delete_shortcut` to remove it.
	6. If the table is not found as a shortcut, it attempts to remove the actual table from the file system.
	"""
	table_path = get_table_path(table_name, lakehouse, workspace)
	workspace_id = resolve_workspace_id(workspace)
	lakehouse_id = resolve_lakehouse_id(lakehouse, workspace=workspace)

	try:
		# Checks if it is a shortcut and then deletes it
		endpoint = f"v1/workspaces/{workspace_id}/items/{lakehouse_id}/shortcuts/Tables/{table_name}"
		response = fabric.FabricRestClient().get(endpoint)
		if response.status_code == 200:
			delete_shortcut(table_name, lakehouse, workspace)

	except fabric.exceptions.FabricHTTPException as err:
		err_response = err.response.json()
		if err_response["errorCode"] == "EntityNotFound":
			print("Shortcut did not exist -> Trying to Remove table", table_name)
			mssparkutils.fs.rm(table_path, recurse=True)


def drop_all_tables_and_shortcuts(
	lakehouse: str, workspace: str = None, included_tables: list = None, control_time: int = 30
):
	"""
	Drops all tables and shortcuts in the specified lakehouse and workspace,
	optionally limiting the operation to a specified list of tables.

	Parameters:
	- lakehouse (str): The name of the lakehouse containing the tables and shortcuts to be dropped.
	- workspace (str, optional): The name of the workspace containing the lakehouse. Defaults to None.
	- included_tables (list, optional): A list of table names to be included in the drop operation.
																			If None, all tables and shortcuts in the lakehouse will be dropped. Defaults to None.

	Returns:
	None

	Example usage:
	drop_all_tables_and_shortcuts(
			lakehouse="Solv",
			workspace="DP_DEV",
			included_tables=["Organisasjon", "SamRapMedlemstall"]
	)

	This function performs the following steps:
	1. Retrieves the list of tables from the specified lakehouse and workspace.
	2. Filters the tables to include only those that exist in the file system.
	3. If no specific tables are provided in `included_tables`, all existing tables are included.
	4. Iterates over the list of existing tables and drops each table or shortcut that is included in the `included_tables`.
	"""
	# Tables to delete
	if included_tables is None or not included_tables:
		table_names = get_all_tables_in_lakehouse(lakehouse=lakehouse, workspace=workspace)

	start_time = time.time() if included_tables else 0
	for table_name in table_names:
		# Trying to drop either shortcut or table
		drop_table_or_shortcut(table_name = table_name, 
						 	   lakehouse = lakehouse, 
							   workspace = workspace)

	# Some caching/control which does not record the shortcut as deleted
	duration = time.time() - start_time
	if (control_time := 30 - duration) > 0:
		print(f"Waiting to {control_time}s to update new shortcuts")
		time.sleep(control_time)

	return "Success"


def get_all_tables_in_lakehouse(lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> list:
	"""
	Retrieves all tables in the specified lakehouse and workspace.

	Parameters:
	- lakehouse (str | UUID | None, optional): The name or UUID of the lakehouse to list tables from. Defaults to None.
	- workspace (str | UUID | None, optional): The name or UUID of the workspace containing the lakehouse. Defaults to None.

	Returns:
	list: A list of table names.

	Example usage:
	get_all_tables_in_lakehouse(lakehouse="Solv", workspace="DP_DEV")
	"""
	table_infos = ls(lakehouse=lakehouse, workspace=workspace, sub_directory="Tables")
	tables = [table_info.name for table_info in table_infos]
	return tables


def get_all_table_paths_in_lakehouse(lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> list:
	"""
	Retrieves all tables in the specified lakehouse and workspace.

	Parameters:
	- lakehouse (str | UUID | None, optional): The name or UUID of the lakehouse to list tables from. Defaults to None.
	- workspace (str | UUID | None, optional): The name or UUID of the workspace containing the lakehouse. Defaults to None.

	Returns:
	list: A list of table names.

	Example usage:
	get_all_tables_in_lakehouse(lakehouse="Solv", workspace="DP_DEV")
	"""
	table_infos = ls(lakehouse=lakehouse, workspace=workspace, sub_directory="Tables")
	table_paths = [table_info.path for table_info in table_infos]
	return table_paths


def ls(lakehouse: str | UUID | None = None, workspace: str | UUID | None = None, sub_directory:str="Tables") -> list:
	"""
	Lists all tables or files in the specified lakehouse and workspace.

	Parameters:
	- lakehouse (str | UUID | None, optional): The name or UUID of the lakehouse to list tables from. Defaults to None.
	- workspace (str | UUID | None, optional): The name or UUID of the workspace containing the lakehouse. Defaults to None.
	- sub_directory (str): The sub-directory to list tables or files from. Must be either "Tables" or at least start with "Files". Defaults to "Tables".

	Returns:
	list: A list of table infos.

	Example usage:
	ls(lakehouse="Solv", workspace="DP_DEV")
	"""
	_test_sub_directory(sub_directory)
	lakehouse_path = get_lakehouse_path(lakehouse, workspace)
	path = f"{lakehouse_path}/{sub_directory}"
	infos = mssparkutils.fs.ls(path)
	return infos

def _test_sub_directory(sub_directory:str) -> bool:
	"""
	Tests if the sub_directory is either "Tables" or starts with "Files".
	"""
	if not (sub_directory == "Tables" or sub_directory.startswith("Files")):
		raise ValueError("The sub_directory must be either 'Tables' or starts with 'Files'.")


def get_newest_file_in_directory(sub_directory:str, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None, date_format:str="%Y%m%dT%H%M%S%f") -> FileInfo:
	"""
	Retrieves the most recent file from a specified sub-directory based on its name's timestamp.

	Args:
		sub_directory (str): The path to the sub-directory within the lakehouse.
		lakehouse (str | UUID | None, optional): The identifier of the lakehouse to search in. Defaults to None.
		workspace (str | UUID | None, optional): The identifier of the workspace to search in. Defaults to None.
		date_format (str, optional): The format of the date and time in the file names, used to parse and identify the newest file. 
									 Defaults to "%Y%m%dT%H%M%S%f".

	Example usage:
		sub_directory = 'Files/capacity_dk/0240830T144400000_Capacity_DK_DEMO.csv'
		get_newest_file_in_directory(sub_directory, lakehouse="Solv", workspace="DP_DEV")
		>> FileInfo(name='20240830T144400000_Capacity_DK_DEMO.csv', path='abfss://...', size=12345, is_dir=False, last_modified=datetime.datetime(2024, 8, 30, 14, 44))

	Returns:
		FileInfo: The information of the newest file in the sub-directory based on the timestamp in the file name.

	Raises:
		ValueError: If the sub_directory is invalid or the date_format does not match the date string in file names.
	"""
	_test_sub_directory(sub_directory)
	file_infos = ls(lakehouse = lakehouse, workspace = workspace, sub_directory = sub_directory)
	return max(file_infos, key=lambda file_info: datetime.strptime(file_info.name.split("/")[-1].split("_")[0], date_format))


def replace_all_tables_or_shortcuts(
	src_lakehouse: str | UUID,
	src_workspace: str | UUID | None = None,
	dst_lakehouse: str | UUID | None = None,
	dst_workspace: str | UUID | None = None,
	included_tables: list[str] = None,
	only_replace: bool = False,
):
	"""
	Replaces all tables or shortcuts from the source lakehouse to the destination lakehouse,
	with options to exclude specific tables and control the replacement behavior.

	Parameters:
	- src_lakehouse (str): The name of the source lakehouse.
	- src_workspace (str, optional): The name of the source workspace. Defaults to None.
	- dst_lakehouse (str, optional): The name of the destination lakehouse. Defaults to None.
	- dst_workspace (str, optional): The name of the destination workspace. Defaults to None.
	- included_tables (list, optional): A list of table names to include from replacement. If None is set, all tables are included.
	- only_replace (bool, optional): If True, only replace tables that exist in the destination lakehouse.
									 If False, re-load all tables from the source lakehouse. Defaults to False.

	Example usage:
	replace_all_tables_or_shortcuts(
					src_lakehouse="Solv",
					src_workspace="DP_DEV",
					dst_lakehouse="Solv",
					dst_workspace="DP_DEV_EO",
					included_tables=["Organisasjon", "SamRapMedlemstall"]
	)

	The function performs the following steps:
	1. Retrieves the list of tables from the destination lakehouse.
	2. Filters the tables to only include those that exist in the file system.
	3. Drops the relevant table or shortcut in the destination lakehouse.
	4. Introduces a delay to ensure control time for updating new shortcuts.
	5. Depending on the `only_replace` flag, either reloads all tables from the source lakehouse or
	   replaces only those that were present in the destination lakehouse.
	6. Creates shortcuts in the destination lakehouse pointing to the source lakehouse tables.
	"""

	# Tables to delete
	dst_table_names = get_all_tables_in_lakehouse(lakehouse=dst_lakehouse, workspace=dst_workspace)

	if dst_table_names:
		if included_tables:
			dst_table_names = [
				table_name for table_name in dst_table_names if table_name in included_tables
			]
		if dst_table_names:
			drop_all_tables_and_shortcuts(included_tables = dst_table_names, 
										  lakehouse = dst_lakehouse,
										  workspace = dst_workspace)

	# Do not do a full load from source, but only replace the tables based on names that were present
	if only_replace:
		src_table_names = dst_table_names
	else:
		src_table_names = get_all_tables_in_lakehouse(lakehouse=src_lakehouse, workspace=src_workspace)
		if included_tables:
			src_table_names = [
				table_name for table_name in src_table_names if table_name in included_tables
				]

	for table_name in src_table_names:
		# Re-setting the shortcuts aka tables to shortcut to
		create_shortcut_onelake(table_name, src_lakehouse, src_workspace, dst_lakehouse, dst_workspace)



def create_shortcut_onelake(
	table_name: str,
	src_lakehouse: str | UUID,
	src_workspace: str | UUID,
	dst_lakehouse: str | UUID,
	dst_workspace: str | UUID,
	shortcut_name: str = None,
):
	"""
	Creates a shortcut for a table in a lakehouse.

	Parameters
	----------
	table_name : str
			The name of the table.
	src_lakehouse : str or UUID
			The name or id of the source lakehouse.
	src_workspace : str or UUID
			The name or id of the source workspace.
	dst_lakehouse : str or UUID
			The name or id of the destination lakehouse.
	dst_workspace : str or UUID
			The name or id of the destination workspace.
	shortcut_name : str, default=None
			The name of the shortcut. If not provided, the table name is used.
	"""
	if shortcut_name is None:
		shortcut_name = table_name

	src_workspace_id = resolve_workspace_id(src_workspace)
	src_lakehouse_id = resolve_lakehouse_id(src_lakehouse, src_workspace)
	src_workspace_name = resolve_workspace_name(src_workspace)
	dst_workspace_id = resolve_workspace_id(dst_workspace)
	dst_workspace_name = resolve_workspace_name(dst_workspace)
	dst_lakehouse_id = resolve_lakehouse_id(dst_lakehouse, dst_workspace)

	client = fabric.FabricRestClient()
	table_path = "Tables/" + table_name

	request_body = {
		"path": "Tables",
		"name": shortcut_name.replace(" ", ""),
		"target": {
			"oneLake": {
				"workspaceId": src_workspace_id,
				"itemId": src_lakehouse_id,
				"path": table_path,
			}
		},
	}

	try:
		response = client.post(
			f"/v1/workspaces/{dst_workspace_id}/items/{dst_lakehouse_id}/shortcuts",
			json=request_body,
		)
		if response.status_code == 201:
			print(
				f"The shortcut '{shortcut_name}' was created in the '{dst_lakehouse}' lakehouse within the '{dst_workspace_name}' workspace. It is based on the '{table_name}' table in the '{src_lakehouse}' lakehouse within the '{src_workspace_name}' workspace."
			)
		else:
			print(response.status_code)
	except Exception as e:
		raise ValueError(f"Failed to create a shortcut for the '{table_name}' table.") from e
	
def shortcut_not_already_shortcutted_tables(src_lakehouse: str | UUID, src_workspace: str | UUID | None = None, dst_lakehouse: str | UUID | None = None, dst_workspace: str | UUID | None = None) -> None:
	"""
	Creates shortcuts for all tables in the source lakehouse that are not already present in the destination lakehouse.
	
	Parameters:
	- src_lakehouse (str | UUID): The name or id of the source lakehouse.
	- src_workspace (str | UUID | None, optional): The name or id of the source workspace. Defaults to None.
	- dst_lakehouse (str | UUID | None, optional): The name or id of the destination lakehouse. Defaults to None.
	- dst_workspace (str | UUID | None, optional): The name or id of the destination workspace. Defaults to None.
	
	Returns:
	None

	Example usage:
	shortcut_not_already_shortcutted_tables(
		src_lakehouse="Silver",
		src_workspace="DEV",
		dst_lakehouse="Silver",
		dst_workspace="TEST")
	"""
	src_tables = get_all_tables_in_lakehouse(workspace=src_workspace, lakehouse=src_lakehouse)
	dst_tables = get_all_tables_in_lakehouse(workspace=dst_workspace, lakehouse=dst_lakehouse)
	missing_tables = list(set(src_tables)-set(dst_tables))
	if missing_tables:
		replace_all_tables_or_shortcuts(
						   src_lakehouse=src_lakehouse,
						   src_workspace=src_workspace,
						   dst_lakehouse=dst_lakehouse,
						   dst_workspace=dst_workspace, 
						   included_tables = missing_tables
						)
	else:
		print("All tables are already shortcutted")


def list_lakehouses(workspace: str | None = None) -> pd.DataFrame:
	"""
	Shows the lakehouses within a workspace.

	Parameters
	----------
	workspace : str, default=None
		The Fabric workspace name.
		Defaults to None which resolves to the workspace of the attached lakehouse
		or if no lakehouse attached, resolves to the workspace of the notebook.

	Returns
	-------
	pandas.DataFrame
		A pandas dataframe showing the lakehouses within a workspace.
	"""

	df = pd.DataFrame(
		columns=[
			"Lakehouse Name",
			"Lakehouse ID",
			"Description",
			"OneLake Tables Path",
			"OneLake Files Path",
			"SQL Endpoint Connection String",
			"SQL Endpoint ID",
			"SQL Endpoint Provisioning Status",
		]
	)

	workspace_id = resolve_workspace_id(workspace)

	client = fabric.FabricRestClient()
	response = client.get(f"/v1/workspaces/{workspace_id}/lakehouses")

	if response.status_code != 200:
		raise fabric.exceptions.FabricHTTPException(response)

	responses = pagination(client, response)

	for r in responses:
		for v in r.get("value", []):
			prop = v.get("properties", {})
			sqlEPProp = prop.get("sqlEndpointProperties", {})

			new_data = {
				"Lakehouse Name": v.get("displayName"),
				"Lakehouse ID": v.get("id"),
				"Description": v.get("description"),
				"OneLake Tables Path": prop.get("oneLakeTablesPath"),
				"OneLake Files Path": prop.get("oneLakeFilesPath"),
				"SQL Endpoint Connection String": sqlEPProp.get("connectionString"),
				"SQL Endpoint ID": sqlEPProp.get("id"),
				"SQL Endpoint Provisioning Status": sqlEPProp.get("provisioningStatus"),
			}
			df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)

	return df

def pagination(client: fabric.FabricRestClient, response:requests.models.Response) -> list:
	"""
	Handles pagination for the responses from the Fabric API.
	
	Parameters
	----------
	client : fabric.FabricRestClient
		The Fabric REST client.
	
	response : requests.models.Response
	
	Returns
	-------
	list
		A list of responses.
	"""

	responses = []
	response_json = response.json()
	responses.append(response_json)

	# Check for pagination
	continuation_token = response_json.get("continuationToken")
	continuation_uri = response_json.get("continuationUri")

	# Loop to handle pagination
	while continuation_token is not None:
		response = client.get(continuation_uri)
		response_json = response.json()
		responses.append(response_json)

		# Update the continuation token and URI for the next iteration
		continuation_token = response_json.get("continuationToken")
		continuation_uri = response_json.get("continuationUri")

	return responses