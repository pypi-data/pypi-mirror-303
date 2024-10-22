import json
import sempy.fabric as fabric
import time
from uuid import UUID

from evidi_fabric.fs import resolve_workspace_id

def trigger_data_pipeline(pipeline_name:str, workspace: str | UUID | None = None, wait_for_completion:bool=True) -> None:
    """
    Trigger a data pipeline execution
    """
    workspace_id = resolve_workspace_id(workspace)
    pipeline_id = get_item_id(item_name = pipeline_name, item_type="DataPipeline")
    client = fabric.FabricRestClient()

    print(f"Triggering pipeline execution for pipeline: {pipeline_name}")
    response = client.post(
                f"/v1/workspaces/{workspace_id}/items/{pipeline_id}/jobs/instances?jobType=Pipeline"
            )
    
    if response.status_code == 202:
        print("Pipeline execution triggered successfully")
        if not wait_for_completion:
            return None
        # Output is not ready yet. Waiting for the request to finish
        status = "InProgress"
        while status == "InProgress":
            print("Pipeline execution in progress. Waiting for completion")
            wait_secs = int(response.headers["Retry-After"]) / 40  # End point suggest to wait REDICOUOUSLY long time
            time.sleep(wait_secs)
            response_status = client.get(response.headers["Location"])
            status = json.loads(response_status._content.decode())["status"]
        if status == "Completed":
            print("Pipeline execution completed successfully")
        else:
            raise RuntimeError(f"Pipeline execution failed with status: {status}")
    else:
        raise RuntimeError(f"Pipeline execution failed with status: {response.text}")
    return response


def get_item_id(item_name:str, item_type: str | None = "Notebook", workspace: str | UUID | None = None) -> str:
    """
    Get the id from item name and type
    """
    _validate_item_type(item_type)
    df_notebooks = fabric.list_items(type = item_type, workspace = workspace)
    workspace_id = resolve_workspace_id(workspace)
    notebook_id = df_notebooks.loc[
        ((df_notebooks["Display Name"] == item_name) & (df_notebooks["Workspace Id"] == workspace_id)), "Id"
    ].iloc[0]
    return notebook_id

def _validate_item_type(item_type:str):
    """
    Warns the user if the item type is presumably not valid
    """
    valid_item_types = [
                        'DataPipeline',
                        'Environment'
                        'Lakehouse',
                        'Notebook',
                        'Report',
                        'SemanticModel',
                        'SQLEndpoint',
                        'Warehouse',
                        ]
    
    if item_type not in valid_item_types:
        print(f'Type: {item_type}, is PRESUMABLY not valid. Current known valid types are: {", ".join(valid_item_types)}')