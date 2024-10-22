from delta import DeltaTable


def latest_version(delta_table: DeltaTable) -> float:
    """
    Get the latest version of a Delta Table

    Args:
    delta_table: DeltaTable object

    Returns:
    float: The latest version of the Delta Table
    """
    version = delta_table.history().agg(max("version")).collect()[0][0]
    return version
