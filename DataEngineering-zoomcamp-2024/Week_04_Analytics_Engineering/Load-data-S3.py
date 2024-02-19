import io
import os
import requests
import pandas as pd
import boto3
from pandas import DataFrame
import pandas as pd
from pyarrow import fs
import pyarrow.parquet as pq
import pyarrow as pa
from dotenv import load_dotenv
"""
Pre-reqs: 
1. `pip install pandas pyarrow boto3`
2. Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in your environment variables or use boto3 configuration method
3. Set your S3 bucket name as BUCKET
"""
load_dotenv()


# services = ['fhv','green','yellow']
init_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'

BUCKET = os.getenv("S3_BUCKET_NAME")
def upload_to_s3(bucket, object_name, local_file):
    """
    Uploads a file to S3 bucket
    """
    s3_client = boto3.client('s3')
    s3_client.upload_file(local_file, bucket, object_name)

def web_to_s3(year, service):
    for i in range(12):
        # sets the month part of the file_name string
        month = f"{i+1:02d}"

        # csv file_name
        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"

        # download it using requests via a pandas df
        request_url = f"{init_url}{service}/{file_name}"
        r = requests.get(request_url)
        open(file_name, 'wb').write(r.content)
        print(f"Local: {file_name}")

        # read it back into a parquet file
        df = pd.read_csv(file_name, compression='gzip')
        parquet_file_name = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(parquet_file_name, engine='pyarrow')
        print(f"Parquet: {parquet_file_name}")

        # upload it to S3 
        upload_to_s3(BUCKET, f"{service}/{parquet_file_name}", parquet_file_name)
        print(f"S3: {service}/{parquet_file_name}")


web_to_s3('2019', 'green')
web_to_s3('2020', 'green')
# web_to_s3('2019', 'yellow')
# web_to_s3('2020', 'yellow')
