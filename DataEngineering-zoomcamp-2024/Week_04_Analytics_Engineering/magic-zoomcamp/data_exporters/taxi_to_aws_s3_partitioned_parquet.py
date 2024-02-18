from pyarrow import fs
import pyarrow as pa
import pandas as pd
import pyarrow.parquet as pq
import awswrangler as wr
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# os.environ['']
bucket_name = 'magetaxi-project'
project_id = 'verdant-current-393218'
table_name = "nyc_taxi_data"
root_path = f"{bucket_name}/{table_name}"
# import pyarrow
# print(hasattr(pa, 'S3FileSystem'))  # Should print True if S3FileSystem is available

@data_exporter
def export_data(data, *args, **kwargs):
    try:
        data['tpep_pickup_date'] = pd.to_datetime(data['tpep_pickup_datetime'], format='%Y-%m-%d')
        data['tpep_pickup_date'] = data['tpep_pickup_date'].dt.date  # Truncate to days
        table = pa.Table.from_pandas(data)

        s3 = fs.S3FileSystem(access_key = 'AKIAYS2NUASAAJQO6BNX',
        secret_key='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',
        allow_bucket_creation=True)
        pq.write_to_dataset(
            table,
            root_path=root_path,
            partition_cols=['tpep_pickup_date'],
            filesystem=s3,
            existing_data_behavior="overwrite_or_ignore"
        )

        print("Data exported successfully.")
    except Exception as e:
        print(f"Error exporting data: {e}")


