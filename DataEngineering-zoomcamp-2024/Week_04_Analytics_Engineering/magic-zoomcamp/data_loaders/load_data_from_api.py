import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    #Define Data types
    taxi_dtypes = {
        'VendorID' : pd.Int64Dtype(),
        'passenger_count' : pd.Int64Dtype(),
        'trip_distance' :   float,
        'RatecodeID' : pd.Int64Dtype(),
        'store_and_fwd_flag':str,
        'PULocationID' : pd.Int64Dtype(),
        'DOLocationID' : pd.Int64Dtype(),
        'payment_type' : pd.Int64Dtype(),
        'fare_amount' : float,
        'extra' : float,
        'mta_tax' : float,
        'tip_amount' : float,
        'tolls_amount' : float,
        'improvement_surcharge' : float,
        'total_amount' : float,
        'congestion_surcharge' : float

    }   
    parse_dates =[ 'lpep_pickup_datetime','lpep_dropoff_datetime']
    #Download the data for the three quarters
    df1 = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',compression='gzip',sep=',',low_memory=False,dtype=taxi_dtypes,parse_dates=parse_dates)
    df2 = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',compression='gzip',sep=',',low_memory=False,dtype=taxi_dtypes,parse_dates=parse_dates)
    df3 = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz',compression='gzip',sep=',',low_memory=False,dtype=taxi_dtypes,parse_dates=parse_dates)
    data = [df1,df2,df3]
    final_df = pd.concat(data)
    # response = requests.get(url)

    return final_df#pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
