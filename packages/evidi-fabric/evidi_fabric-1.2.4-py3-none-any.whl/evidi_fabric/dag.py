from evidi_fabric.notebook import (
    get_cleaned_notebook_content,
    find_destination_paths,
    find_source_paths,
    get_notebook_names,
)
from uuid import UUID
import json

def get_dependencies(notebook_names: list[str] = None, workspace: str | UUID | None = None) -> dict[str, list[str]]:
    """
    Get the dependencies of the notebooks in the workspace. This is done by:
    1) Getting the content of all notebooks specified in the notebook_names list.
    2) Finding the source paths of the notebooks.
    3) Finding the destination paths of the notebooks.
    4) Constructing a dictionary where the keys are the notebook names and the values
       are the source paths for all source paths that is a destination path of another notebook.

    Regarding the source and destination paths:
    - There are many ways that you can specify the source and destination paths in a notebook.
      Here, the most common ways are considered, but not all possible ways.
      Therefore, use this function with consideration.
    """

    if not notebook_names:
        notebook_names = get_notebook_names(workspace)

    infos = {}
    for notebook_name in notebook_names:
        notebook_content = get_cleaned_notebook_content(notebook_name=notebook_name, workspace=workspace)
        infos[notebook_name] = {}
        infos[notebook_name]["sources"] = []
        infos[notebook_name]["destination"] = []
        try:
            infos[notebook_name]["sources"] = find_source_paths(notebook_content)
        except SyntaxError:
            print("Syntax error in the notebook. Continuing")
            continue
        except Exception as e:
            print(f"Error in notebook {notebook_name}: {e}\nContinuing")
            pass
        try:
            infos[notebook_name]["destination"] = find_destination_paths(notebook_content)
        except Exception as e:
            print(f"Error in notebook {notebook_name}: {e}\nContinuing")
            pass

    notebooks = infos.keys()
    dependencies = {}
    for notebook in notebooks:
        sources = infos[notebook]["sources"]
        dependencies[notebook] = [
            source_notebook
            for source_notebook in notebooks
            if infos[source_notebook]["destination"] and infos[source_notebook]["destination"][0] in sources
        ]
    return dependencies


def validate_DAG(DAG, DAG_draft:dict[list[dict]] | None = None):
    """
    Compare two DAG dictionaries and highlight differences in activities and dependencies.
    
    Args:
        DAG (dict): The DAG dictionary.
        DAG_draft (dict): The draft DAG dictionary.
    """
    if not DAG_draft:
        print("No draft DAG provided. Comparing with an empty DAG.")
        DAG_draft = get_DAG_draft()
    # Create dictionaries mapping activity names to their details for both DAGs
    activities_current = {activity['name']: activity for activity in DAG.get('activities', [])}
    activities_draft = {activity['name']: activity for activity in DAG_draft.get('activities', [])}

    # Get sets of activity names from both DAGs
    names_current = set(activities_current.keys())
    names_draft = set(activities_draft.keys())

    # Identify activities unique to each DAG
    only_in_current = names_current - names_draft
    only_in_draft = names_draft - names_current

    # Report activities only in DAG_current
    if only_in_current:
        print("Activities only in DAG_current:")
        for name in sorted(only_in_current):
            print(f"  - {name}")
    else:
        print("No activities unique to DAG_current.")

    # Report activities only in DAG_draft
    if only_in_draft:
        print("Activities only in DAG_draft:")
        for name in sorted(only_in_draft):
            print(f"  - {name}")
    else:
        print("No activities unique to DAG_draft.")

    # Compare dependencies for activities present in both DAGs
    common_names = names_current & names_draft
    for name in sorted(common_names):
        deps_current = set(activities_current[name].get('dependencies', []))
        deps_draft = set(activities_draft[name].get('dependencies', []))
        if deps_current != deps_draft:
            print(f"\nDifferences in dependencies for activity '{name}':")
            only_in_deps_current = deps_current - deps_draft
            only_in_deps_draft = deps_draft - deps_current
            if only_in_deps_current:
                print(f"  Dependencies only in DAG_current: {only_in_deps_current}")
            if only_in_deps_draft:
                print(f"  Dependencies only in DAG_draft: {only_in_deps_draft}")

    print("\nComparison complete.")


def get_DAG_draft(
    workspace: str | UUID | None = None, notebook_names: list[str] = None, timeoutPerCellInSeconds: int = 1800
) -> dict[list[dict]]:
    """
    Get a draft of the Directed Acyclic Graph (DAG) of the notebooks in the workspace.

    This function will read the content of the notebooks in a workspace (default current workspace),
    find the dependencies between the notebooks, and from that construct a draft of the DAG.

    Example:
    ```python
    DAG = get_DAG_draft()
    ```
    """

    dependencies = get_dependencies(notebook_names, workspace)

    DAG = {}
    DAG["activities"] = []
    notebooks = list(dependencies.keys())
    notebooks.sort()
    for notebook in notebooks:
        activity = {
            "name": notebook,
            "path": notebook,
            "timeoutPerCellInSeconds": timeoutPerCellInSeconds,  # max timeout for each cell, default to 90 seconds
            "args": {"useRootDefaultLakehouse": True},
        }
        if dependencies[notebook]:
            activity["dependencies"] = dependencies[notebook]
        DAG["activities"].append(activity)
    print(json.dumps(DAG, indent=4))
    return DAG
