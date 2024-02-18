
from pyarrow import fs
import pyarrow as pa
import pandas as pd
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# os.environ['']
bucket_name = 'magetaxi-project'
project_id = 'verdant-current-393'
table_name = "green_taxi_data"
root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data(data, *args, **kwargs):
    try:
        table = pa.Table.from_pandas(data)

        s3 = fs.S3FileSystem(
        allow_bucket_creation=True)
        pq.write_to_dataset(
            table,
            root_path=root_path,
            filesystem=s3,
            existing_data_behavior="overwrite_or_ignore"
        )

        print("Data exported successfully.")
    except Exception as e:
        print(f"Error exporting data: {e}")


