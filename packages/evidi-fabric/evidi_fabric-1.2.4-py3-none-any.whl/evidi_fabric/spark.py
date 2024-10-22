import logging
from pyspark.conf import SparkConf
from pyspark.sql.session import SparkSession
import sempy.fabric as fabric

logging.getLogger(__name__)


def get_or_create_spark() -> SparkSession:
    """Gets a spark session and returns it unless it already exists.

    This function is used to start a spark session and return it. It is used
    to avoid creating multiple spark sessions. In Databricks, this function
    simply returns the existing spark session.

    Returns:
        SparkSession: Spark session
    """
    logging.info("Getting or creating spark session")

    if fabric.get_workspace_id() == "local":
        conf = SparkConf()
        try:
            jars_packages = ["io.delta:delta-core_2.12:2.0.0"]
            conf.set("spark.jars.packages", ",".join(jars_packages))
        except AttributeError:
            pass

        conf.set("spark.driver.memory", "8g")
        conf.set("spark.driver.maxResultSize", "4g")
        conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
        conf.set("spark.sql.debug.maxToStringFields", "1000")  # to avoid warning
        conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        conf.set("spark.sql.session.timeZone", "UTC")

        spark = SparkSession.builder.config(conf=conf).getOrCreate()
    else:
        spark = SparkSession.builder.getOrCreate()
    return spark


if __name__ == "__main__":
    spark = get_or_create_spark()
    print("Done")
