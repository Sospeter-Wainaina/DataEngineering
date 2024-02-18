import io
import pandas as pd
import boto3

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader

def load_data_from_s3(*args, **kwargs):
    """
    Template for loading data from S3 bucket using AWS Boto3 library
    """
    bucket_name = 'magetaxi-project'
    key = 'yellow_tripdata_2021-01.csv'

    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=key)
    body = obj['Body'].read()

    return pd.read_csv(io.BytesIO(body), sep=',')

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'