"""
The notebook module contains functions to work with notebooks in Fabric Workspaces.

Functions:
 - find_destination_paths: get the destination paths of a notebook
 - find_source_paths: Get the source tables of notebooks
 - get_all_notebooks_using_tables: Get a list of notebooks that uses the specified tables
 - get_cleaned_notebook_content: Get the cleaned content of a notebook
 - get_notebook_content: Get the content of a notebook
 - get_notebook_names: Get the names of the notebooks in a workspace
 - get_source_tables_in_notebooks: Get the source tables of notebooks
 - get_source_paths_in_notebooks: Get the source paths of notebooks
 
"""

import ast
import base64
import json
import re
import sempy.fabric as fabric
import time
from uuid import UUID
from evidi_fabric.fs import get_table_path, get_table_paths, resolve_workspace_id
from evidi_fabric.items import get_item_id


def get_destination_matches(tree, notebook_content: str):
    matches = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call): #without type hints
            if isinstance(node.func, ast.Attribute) and node.func.attr == "forPath":
                try:
                    if isinstance(node.args[1], ast.Name):
                        # input is a variable. Look up its value!
                        matches.append(node.args[1].id)
                    elif isinstance(node.args[1], ast.Constant):
                        matches.append(f"'{node.args[1].s}'")
                except AttributeError:
                    pattern_forPath = r"DeltaTable\.forPath\(spark, (f\".*?\"|f'.*?'|\".*?\"|'.*?')"
                    matches.extend(re.findall(pattern_forPath, notebook_content))

            elif isinstance(node.func, ast.Attribute) and node.func.attr == "save":
                try:
                    keyword = node.func.value.args[0].s
                    value = node.func.value.args[1]
                    if keyword == "path":
                        if isinstance(value, ast.Name):
                            matches.append(value.id)
                        elif isinstance(value, ast.Constant):
                            matches.append(f"'{value.s}'")
                except AttributeError:
                    # Falling back to regex
                    pattern_save = r"\.write\.save\((f\".*?\"|f'.*?'|\".*?\"|'.*?')"
                    matches.extend(re.findall(pattern_save, notebook_content))

        if isinstance(node, ast.Expr): #with type hints
            if isinstance(node.value, ast.Call):
                if isinstance(node.value.func, ast.Attribute):
                    if node.value.func.attr == "forPath":
                        try:
                            if isinstance(node.value.args[1], ast.Name):
                                # input is a variable. Look up its value!
                                matches.append(node.value.args[1].id)
                            elif isinstance(node.value.args[1], ast.Constant):
                                matches.append(f"'{node.value.args[1].s}'")
                        except AttributeError:
                            pattern_forPath = r"DeltaTable\.forPath\(spark, (f\".*?\"|f'.*?'|\".*?\"|'.*?')"
                            matches.extend(re.findall(pattern_forPath, notebook_content))
                    elif node.value.func.attr == "save":
                        try:
                            keyword = node.value.func.value.args[0].s
                            value = node.value.func.value.args[1]
                            if keyword == "path":
                                if isinstance(value, ast.Name):
                                    matches.append(value.id)
                                elif isinstance(value, ast.Constant):
                                    matches.append(f"'{value.s}'")
                        except AttributeError:
                            # Falling back to regex
                            # pattern_save = r"\.write\.save\((.*?)(?:,|\))"
                            pattern_save = r"\.write\.save\((f\".*?\"|f'.*?'|\".*?\"|'.*?')"
                            matches.extend(re.findall(pattern_save, notebook_content))


    matches_unique = list(set(matches))
    return matches_unique


def find_destination_paths(notebook_content: str) -> list[str]:
    # Parse the code to get the AST
    tree = ast.parse(notebook_content)

    # Create a dictionary to store variable assignments
    variables = get_all_variable_assignments_in_notebook(notebook_content)

    matches = get_destination_matches(tree, notebook_content)

    destination_paths = []
    for match in matches:
        try:
            destination_path = _get_path_from_match(match, tree, variables)
            destination_paths.append(destination_path)
        except:
            pass

    if not destination_paths:
        print("No match found")

    return destination_paths


def _find_keyword_arguments_in_get_table_path(node, variables: dict[str, str]):
    """
    Find the keyword arguments in the get_table_path function call
    """
    table_name = None
    lakehouse = None

    for keyword in node.value.keywords:
        if keyword.arg == "table_name":
            if isinstance(keyword.value, ast.Constant):
                table_name = keyword.value.s
            elif isinstance(keyword.value, ast.Name):
                table_name = variables.get(keyword.value.id)
        elif keyword.arg == "lakehouse":
            if isinstance(keyword.value, ast.Constant):
                lakehouse = keyword.value.s
            elif isinstance(keyword.value, ast.Name):
                lakehouse = variables.get(keyword.value.id)
    return table_name, lakehouse


def _find_positional_arguments_in_get_table_path(
    node, variables: dict[str, str], lakehouse: str = None, table_name: str = None
) -> tuple[str, str]:
    """
    Find the positional arguments in the get_table_path function call
    """

    if not table_name:
        try:
            # Looking up variable values
            table_name = variables.get(node.value.args[0].id)
        except AttributeError:
            # No variables, assuming string values
            table_name = node.value.args[0].value
        except IndexError:
            raise IndexError("No table name found")

    if not lakehouse:
        try:
            # Looking up variable values
            lakehouse = variables.get(node.value.args[1].id)
        except AttributeError:
            # No variables, assuming string values
            lakehouse = node.value.args[1].value

    return table_name, lakehouse


def _extract_path_from_get_table_path(node, variables: dict[str, str]) -> str:
    """
    Evaluate the get_table_path function call and extract the table path
    """

    # Check for keyword arguments
    table_name, lakehouse = _find_keyword_arguments_in_get_table_path(node, variables)

    # Check for positional arguments if keyword arguments are not found
    if not table_name or not lakehouse:
        table_name, lakehouse = _find_positional_arguments_in_get_table_path(node, variables, lakehouse, table_name)

    path = get_table_path(table_name=table_name, lakehouse=lakehouse)

    return path


def _get_args_from_f_string(parameter_value: str) -> list[str]:
    """
    Get the arguments from an f-string
    """
    n_arguments = len(parameter_value.split("{")) - 1
    args = []
    for i in range(n_arguments):
        arg = parameter_value.split("{")[i + 1].split("}")[0]
        args.append(arg)
    return args


def _get_args_from_string(string: str) -> list[str]:
    """
    Get the arguments from a string
    """
    args = string.split(".")
    return args


def _get_path_from_string(string: str) -> str:
    """
    Get the source path from a string
    """
    is_path: str = "abfss" == string[:4]
    if is_path:
        path = string
    else:
        args = _get_args_from_string(string)
        lakehouse = args[0]
        table_name = args[1]
        path = get_table_path(table_name=table_name, lakehouse=lakehouse)
    return path


def _convert_f_string_to_lakehouse_table_format(fstring: str, variables: dict[str, str]) -> str:
    """
    The goal of this function is to convert any f-string path to a f"{lakehouse}.{table_name}" format
    """
    if "mssparkutils.lakehouse.get" in fstring:
        args = _get_args_from_f_string(fstring)
        lakehouse = args[0].split("(")[1].split(")")[0]
        if _is_string(lakehouse):
            lakehouse = lakehouse.strip("'\"")
        else:
            lakehouse = _get_variable_assignment(lakehouse, variables)

            # table_name must be a part of the string
        if len(args) == 1:
            table_name = fstring.split("Tables/")[-1]
        else:
            table_name = args[1]
            if _is_string(table_name):
                table_name = table_name.strip("'\"")
            else:
                table_name = _get_variable_assignment(table_name, variables)
        return f"{lakehouse}.{table_name}"

    args = _get_args_from_f_string(fstring)
    fstring = fstring[1:].strip("'\"").replace("'''", "").replace('"""', "")
    for arg in args:
        value = _get_variable_assignment(arg, variables)
        fstring = fstring.replace(f"{{{arg}}}", value)
    return fstring


def _get_path_from_f_string(parameter_value: str, variables: dict[str, str]) -> str:
    """
    Get the source path from an f-string
    """
    string = _convert_f_string_to_lakehouse_table_format(parameter_value, variables)
    path = _get_path_from_string(string)
    return path


def _get_variable_assignment(variable: str, variables: dict[str, str]) -> str:
    """
    Get variable assignment from a variable
    """
    try:
        return [value for key, value in variables.items() if key == variable][0]
    except IndexError:
        raise IndexError(f"Variable {variable} is not assigned")


def get_all_variable_assignments_in_notebook(notebook_content: str):
    """
    Get all variables in a notebook
    """
    tree = ast.parse(notebook_content)
    variables = {}

    # Find variable assignments
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if isinstance(node.targets[0], ast.Name):
                variable_name = node.targets[0].id
                if isinstance(node.value, ast.Constant):
                    variable_value = node.value.value
                    variables[variable_name] = variable_value
                elif isinstance(node.value, ast.Name):
                    variable_value = variables.get(node.value.id)
                    if variable_value:
                        variables[variable_name] = variable_value
                elif isinstance(node.value, ast.JoinedStr):
                    fstring = "f'"
                    for value in node.value.values:
                        if isinstance(value, ast.FormattedValue):
                            variable_value = value.value.id
                            fstring += f"{{{variable_value}}}"
                        elif isinstance(value, ast.Constant):
                            fstring += value.value
                    fstring += "'"
                    variables[variable_name] = fstring
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                variable_name = node.target.id
                if isinstance(node.value, ast.Constant):
                    variable_value = node.value.value
                    variables[variable_name] = variable_value
                elif isinstance(node.value, ast.Name):
                    variable_value = variables.get(node.value.id)
                    if variable_value:
                        variables[variable_name] = variable_value
                elif isinstance(node.value, ast.JoinedStr):
                    fstring = "f'"
                    for value in node.value.values:
                        if isinstance(value, ast.FormattedValue):
                            variable_value = value.value.id
                            fstring += f"{{{variable_value}}}"
                        elif isinstance(value, ast.Constant):
                            fstring += value.value
                    fstring += "'"
                    variables[variable_name] = fstring
            
                

    return variables


def _is_string(value: str) -> bool:
    """
    Check if a value is a string
    """
    return "'" in value or '"' in value


def _is_f_string(value: str) -> bool:
    """
    Check if a value is an f-string
    """
    return value[:2] == "f'" or value[:2] == 'f"'


def _get_path_from_match(match: str, tree: ast.AST, variables: dict[str, str]) -> str:
    """
    Get the source path from a match. Match can be a f-string, string or a variable,
    basically whatever the designated function was called with
    """
    parameter_value = match.strip()
    if _is_string(parameter_value):
        if _is_f_string(parameter_value):
            path = _get_path_from_f_string(parameter_value, variables)
        else:
            # If it's a string, then it must be a path!
            path = parameter_value.strip("'\"")
        return path
    try:
        # Check if the variable is assigned using an assignment
        value = _get_variable_assignment(variable=parameter_value, variables=variables)
        if _is_f_string(value):
            path = _get_path_from_f_string(value, variables)
        elif _is_string(value):
            path = _get_path_from_string(value)
        else:
            raise NotImplementedError("Not implemented yet")
        return path

    except IndexError:
        path = _get_path_from_parameter_value_using_evidi_fabric_functions(tree, parameter_value, variables)
        return path

    

def _get_path_from_parameter_value_using_evidi_fabric_functions(tree: ast.AST, parameter_value: str, variables: dict[str, str]) -> str:
    """
    Get the path from the get_table, get_table_path or get_file_path functions
    
    Args:
        tree: The AST of the notebook
        variables: The dictionary of variable assignments
        parameter_value: The variable name
        
    Returns:
        str: The path
    """
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == parameter_value
        ):
            # Check if the variable is assigned using get_table_path or get_file_path
            if (
                isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id in ["get_table_path", "get_file_path"]
            ):
                path = _extract_path_from_get_table_path(node, variables)
                return path
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == parameter_value
        ):
            # Check if the variable is assigned using get_table_path or get_file_path
            if (
                isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id in ["get_table_path", "get_file_path"]
            ):
                path = _extract_path_from_get_table_path(node, variables)
                return path
    raise IndexError(f"Variable {parameter_value} is not assigned")



def get_source_matches(tree, notebook_content: str):
    matches = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr in ["load", "table"]:
                try:
                    if isinstance(node.args[0], ast.Name):
                        # input is a variable. Look up its value!
                        matches.append(node.args[0].id)
                    elif isinstance(node.args[0], ast.Constant):
                        matches.append(f"'{node.args[0].s}'")
                except AttributeError:
                    source_pattern = r"spark\.read(?:\.format\(.delta.\))?\.(?:load|table)\((.*)\)"
                    matches.extend(re.findall(source_pattern, notebook_content))

    matches_unique = list(set(matches))
    return matches_unique


def find_source_paths(notebook_content: str):
    # Parse the code to get the AST
    tree = ast.parse(notebook_content)

    # Create a dictionary to store variable assignments
    variables = get_all_variable_assignments_in_notebook(notebook_content)

    # Search for all occurrences of the source_pattern in the code
    matches = get_source_matches(tree, notebook_content)

    source_paths = []
    for match in matches:
        try:
            source_path = _get_path_from_match(match, tree, variables)
            source_paths.append(source_path)
        except:
            pass

    source_paths.extend(_get_path_from_get_table(tree, variables))

    if not source_paths:
        print("No match found")

    return source_paths

def _get_path_from_get_table(tree: ast.AST, variables: dict[str, str]) -> str:
    """
    Get the path from the get_table, get_table_path or get_file_path functions
    
    Args:
        tree: The AST of the notebook
        variables: The dictionary of variable assignments
        parameter_value: The variable name
        
    Returns:
        str: The path
    """
    paths = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and isinstance(node.targets[0], ast.Name)
        ):
            # Check if the variable is assigned using get_table_path or get_file_path
            if (
                isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id in ["get_table"]
            ):
                paths.append(_extract_path_from_get_table_path(node, variables))
                continue
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
        ):
            # Check if the variable is assigned using get_table_path or get_file_path
            if (
                isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id in ["get_table"]
            ):
                paths.append(_extract_path_from_get_table_path(node, variables))
    return paths


def get_path_from_get_table(tree: ast.AST, variables: dict[str, str]):
    paths = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if node.value.func.id == "get_table":
                paths.extend(_extract_path_from_get_table_path(node, variables))


def get_notebook_content(notebook_name: str, workspace: str | UUID | None = None):
    """
    Retrieving the content from a notebook from its id.
    Note: If workspace is not specified, the current workspace is used
    """
    client = fabric.FabricRestClient()
    workspace_id = resolve_workspace_id(workspace)
    notebook_id = get_item_id(item_name = notebook_name, 
                              item_type = "Notebook",
                              workspace = workspace)
    response = client.post(f"/v1/workspaces/{workspace_id}/items/{notebook_id}/getDefinition")
    if response.status_code == 202:
        # Output is not ready yet. Waiting for the request to finish
        status = "Running"
        while status == "Running":
            wait_secs = int(response.headers["Retry-After"]) / 40  # End point suggest to wait REDICOUOUSLY long time
            time.sleep(wait_secs)
            response_status = client.get(response.headers["location"])
            status = json.loads(response_status._content.decode())["status"]
        response = client.get(response_status.headers["Location"])
    payload_encoded = json.loads(response.content)["definition"]["parts"][0]["payload"]
    notebook_content = base64.b64decode(payload_encoded).decode()
    return notebook_content


# from evidi_fabric.security import get_azure_token

# class TokenProvider():
#     def __init__(self):
#         self.token = get_azure_token()

#     def token_provider(self):
#         return self.token

# def run_notebook(notebook_name: str, workspace: str | UUID | None = None, token: str | None = None):
#     """
#     Run a notebook on demand
#     """
#     # if not token:
    
#     client = fabric.FabricRestClient(TokenProvider)
#     workspace_id = resolve_workspace_id(workspace)
#     notebook_id = get_item_id(item_name = notebook_name, 
#                               item_type = "Notebook",
#                               workspace = workspace)

#     response = client.post(f"/v1/workspaces/{workspace_id}/items/{notebook_id}/jobs/instances?jobType=RunNotebook")
#     # POST https://api.fabric.microsoft.com/v1/workspaces/{{WORKSPACE_ID}}/items/{{ARTIFACT_ID}}/jobs/instances?jobType=RunNotebook

#     {
#         "executionData": {
#             "parameters": {
#                 "parameterName": {
#                     "value": "new value",
#                     "type": "string"
#                 }
#             },
#             "configuration": {
#                 "conf": {
#                     "spark.conf1": "value"
#                 },
#                 "environment": {
#                     "id": "<environment_id>",
#                     "name": "<environment_name>"
#                 },
#                 "defaultLakehouse": {
#                     "name": "<lakehouse-name>",
#                     "id": "<lakehouse-id>",
#                     "workspaceId": "<(optional) workspace-id-that-contains-the-lakehouse>"
#                 },
#                 "useStarterPool": false,
#                 "useWorkspacePool": "<workspace-pool-name>"
#             }
#         }
#     }


def get_cleaned_notebook_content(notebook_name: str, workspace: str | UUID | None = None):
    """
    Retrieving the cleaned content from a notebook from its id.
    Note: If workspace is not specified, the current workspace is used
    """
    notebook_content = get_notebook_content(notebook_name, workspace)
    notebook_content_cleaned = clean_notebook_content(notebook_content)
    return notebook_content_cleaned


def clean_notebook_content(notebook_content: str) -> str:
    """
    Clean the notebook content from the cell magic commands
    """
    lines = notebook_content.split("\n")
    # Filter out lines that start with '%'
    filtered_lines = [line for line in lines if not line.strip().startswith("%") and not line.strip().startswith("#")]

    # Replace !pip install with pass (if in try, except block) else remove
    filtered_lines = ["    pass" if line[:16] == "    !pip install" else line for line in filtered_lines]
    filtered_lines = ["\tpass" if line[:13] == "\t!pip install" else line for line in filtered_lines]
    filtered_lines = [line for line in filtered_lines if not line.strip()[:12] == "!pip install"]
    # Join the filtered lines back into a single string
    cleaned_notebook_content = "\n".join(filtered_lines)
    return cleaned_notebook_content


def get_source_tables_in_notebooks(notebook_names: list[str] | None = None, workspace: str | UUID | None = None) -> list[str]:
    """
    Get the source tables of all the notebooks. If no notebook names are provided, all the notebooks in the workspace are used
    
    Args:
        notebook_names: The names of the notebooks to get the source tables from
        workspace: The workspace to get the notebooks from
        
    Returns:
        dict: A list source tables used in the notebooks"""
    infos = get_source_paths_in_notebooks(notebook_names = notebook_names, workspace = workspace)
    sources = list(set([elem.rsplit('/')[-1] for notebook in infos.keys() for elem in infos[notebook]]))
    sources.sort()
    return sources

def get_source_paths_in_notebooks(notebook_names: list[str] | None = None, workspace: str | UUID | None = None) -> dict[dict[str, list[str]]]:
    """
    Get the source paths of all the notebooks in a workspace
    
    Args:
        notebook_names: The names of the notebooks to get the source paths from
        workspace: The workspace to get the notebooks from
        
    Returns:
        dict: A dictionary with the notebook names as keys and the source paths as values"""
    if not notebook_names:
        notebook_names = get_notebook_names(workspace)

    infos = {}
    for notebook_name in notebook_names:
        notebook_content = get_cleaned_notebook_content(notebook_name=notebook_name, workspace=workspace)
        infos[notebook_name] = {}
        try:
            infos[notebook_name] = find_source_paths(notebook_content)
        except SyntaxError:
            print("Syntax error in the notebook. Continuing")
            continue
        except Exception as e:
            print(f"Error in notebook {notebook_name}: {e}\nContinuing")
            pass
    return infos

def get_all_notebooks_using_tables(table_names: str, notebook_names:list[str] | None = None, lakehouse: str | UUID | None = None, workspace: str | UUID | None = None) -> list[str]:
    """
    Get a list of notebooks that uses the specified tables.
    If no notebook names are provided, all the notebooks in the workspace are used

    Args:
        table_names: The names of the tables to search for
        notebook_names: The names of the notebooks to search in
        lakehouse: The lakehouse to search in
        workspace: The workspace to search in

    Returns:
        list: A list of notebooks that uses the specified tables
    """
    if not notebook_names:
        notebook_names = get_notebook_names(workspace)

    infos = get_source_paths_in_notebooks(notebook_names = notebook_names, workspace = workspace)
    notebooks = infos.keys()
    sources = get_table_paths(table_names, lakehouse = lakehouse)
    notebooks_uses_sources = [notebook for notebook in notebooks if any(source in sources for source in infos[notebook])]
    return notebooks_uses_sources

def get_notebook_names(workspace: str | UUID | None = None) -> list[str]:
    """
    Get the names of the notebooks in a workspace
    """
    df_notebooks = fabric.list_items("Notebook")
    workspace_id = resolve_workspace_id(workspace)
    notebook_names = df_notebooks.loc[df_notebooks["Workspace Id"] == workspace_id, "Display Name"].to_list()
    notebook_names.sort()
    return notebook_names


if __name__ == "__main__":
    notebook_content = """
lakehouse_bronze:str = "Bronze"
source_directory:str = "Ekonomirapport Söderhamn Nära - Elnät"
lakehouse_silver:str = "Silver"
destination_table_name:str = "MayorGroup" 
source_table_name:str = "MayorGroup2"

df_raw2 = get_table("MayorGroup2", lakehouse_bronze)
df_raw3 = get_table(source_table_name, "Bronze3")

path=get_file_path(directory=f'{source_directory}/MayorGroup.xlsx', lakehouse=lakehouse_bronze)
df_raw = spark.read.load(path)



destination_table_path:str=get_table_path(table_name=destination_table_name, lakehouse=lakehouse_silver)

df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .option("path", destination_table_path) \
    .save()
"""
    # run_notebook("trigger - capacity", workspace="76925c30-d2ba-4852-b72e-926b22d434ad")
    notebook_content_cleaned = clean_notebook_content(notebook_content)
    source_paths = find_source_paths(notebook_content_cleaned)
    destination_paths = find_destination_paths(notebook_content_cleaned)
    print(f"Source paths: {source_paths}")
    print("stop")
