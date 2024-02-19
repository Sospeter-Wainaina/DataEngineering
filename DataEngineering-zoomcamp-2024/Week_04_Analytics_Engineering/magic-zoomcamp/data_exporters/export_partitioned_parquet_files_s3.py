from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from pandas import DataFrame
import pandas as pd
from pyarrow import fs
import pyarrow.parquet as pq
import pyarrow as pa
# import py
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a S3 bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#s3
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev'

    bucket_name = 'magetaxi-project'
    project_id = 'verdant-393218'
    table_name = "green_taxi_data"
    root_path = f"{bucket_name}/{table_name}"

    try:
        df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime'], format='%Y-%m-%d')
        df['lpep_pickup_date'] = df['lpep_pickup_date'].dt.date  # Truncate to days
        table = pa.Table.from_pandas(df)

        s3 = fs.S3FileSystem(
        allow_bucket_creation=True)
        pq.write_to_dataset(
            table,
            root_path=root_path,
            partition_cols=['lpep_pickup_date'],
            filesystem=s3,
            existing_data_behavior="overwrite_or_ignore"
        )
        

        print("Data exported successfully.")
    except Exception as e:
        print(f"Error exporting data: {e}")
