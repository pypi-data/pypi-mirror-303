"""
The `semanticmodel` module provides functions to work with semantic models in Evidi Fabric.

Functions:
    - get_dimension_tables: Get all dimension tables from the relationships dictionary
    - get_fact_tables: Get all fact tables from the relationships dictionary
    - get_fact_keys: Get all keys of a fact table
    - get_dimension_keys: Get all keys of a dimension table
"""


import base64
import json
import pandas as pd
import re
import time
from uuid import UUID
from sempy.fabric import FabricRestClient
from evidi_fabric.fs import resolve_workspace_id, list_lakehouses
from evidi_fabric.items import get_item_id

def get_dimension_tables(relationships: pd.DataFrame) -> list[str]:
    """
    Get all dimension tables from the relationships dictionary
    """
    dimension_tables = list(set(relationships["Datasource Table Name To"].to_list()))
    dimension_tables.sort()
    return dimension_tables

def get_fact_tables(relationships: pd.DataFrame) -> list[str]:
    """
    Get all fact tables from the relationships dictionary
    """
    fact_tables = list(set(relationships["Datasource Table Name From"].to_list()))
    fact_tables.sort()
    return fact_tables

def get_fact_keys(fact: str, relationships: pd.DataFrame) -> list[str]:
    """
    Get all keys of a fact table
    """
    keys = relationships[relationships["Datasource Table Name From"] == fact]["From Column"].to_list()
    keys.sort()
    return keys

def get_dimension_keys(dimension: str, relationships: pd.DataFrame) -> str:
    """
    Get all keys of a dimension table
    """
    keys = list(set(relationships[relationships["Datasource Table Name To"] == dimension]["To Column"].to_list()))
    keys.sort()
    return keys

def resolve_lakehouse_from_semantic_model(semantic_model: str, workspace: str | UUID | None = None) -> str:
    """
    Resolve the lakehouse from a semantic model
    
    Args:
        semantic_model: Name of the semantic model
        workspace: Name or UUID of the workspace where the semantic model is located (optional)
    
    Returns:
        Name of the lakehouse"""

    sql_endpoint_id = get_direct_lake_sql_endpoint_id_from_semantic_model(semantic_model = semantic_model, 
                                                      workspace = workspace)
    lakehouses_info = list_lakehouses(workspace)

    lakehouse = lakehouses_info.loc[lakehouses_info["SQL Endpoint ID"]==sql_endpoint_id, "Lakehouse Name"].iloc[0]

    return lakehouse


def get_direct_lake_sql_endpoint_id_from_semantic_model(semantic_model: str, workspace: str | UUID | None = None) -> UUID:
    """
    Obtains the SQL Endpoint ID of the semantic model.

    Parameters
    ----------
    dataset : str
        The name of the semantic model.
    workspace : str, default=None
        The Fabric workspace name.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    uuid.UUID
        The ID of SQL Endpoint.
    """
    workspace_id = resolve_workspace_id(workspace)
    semantic_model_id = get_item_id(item_name=semantic_model, item_type='SemanticModel', workspace=workspace_id)
    client = FabricRestClient()
    response = client.post(
                f"/v1/workspaces/{workspace_id}/semanticModels/{semantic_model_id}/getDefinition",
            )
    if response.status_code == 202:
        # Output is not ready yet. Waiting for the request to finish
        status = "Running"
        while status == "Running":
            wait_secs = int(response.headers["Retry-After"]) / 40  # End point suggest to wait REDICOUOUSLY long time
            time.sleep(wait_secs)
            response_status = client.get(response.headers["location"])
            status = json.loads(response_status._content.decode())["status"]
        response = client.get(response_status.headers["Location"])
    parts = json.loads(response.content)["definition"]["parts"]
    expressions_encoded = [part["payload"] for part in parts if "definition/expressions.tmdl" == part["path"]][0]
    expressions = base64.b64decode(expressions_encoded).decode()
    match = re.search(r'Sql\.Database\(".*?",\s*"(.*?)"\)', expressions)
    if match:
        sql_endpoint_id = match.group(1)
        return sql_endpoint_id
    else:
        raise ValueError(f"SQL Endpoint ID not found in the semantic model: {semantic_model}")
