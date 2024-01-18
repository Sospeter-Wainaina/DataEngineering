import pandas as pd
from sqlalchemy import create_engine
import os
import argparse
import requests
import gzip
from io import BytesIO

def download_and_decompress(url, target_file):
    response = requests.get(url)
    with gzip.GzipFile(fileobj=BytesIO(response.content), mode='rb') as f_in:
        with open(target_file, 'wb') as f_out:
            f_out.write(f_in.read())

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.dbname
    tbname = params.tbname
    url = params.url

    # downloading and decompressing the data
    compressed_file = 'yellow_tripdata_2021-07.csv.gz'
    csv_file = 'yellow_tripdata_2021-07.csv'
    download_and_decompress(url, compressed_file)

    # loading the decompressed CSV file into a DataFrame

    df = pd.read_csv(csv_file)
    #converting the -tpep_pickup_datetime & tpep_dropoff_datetime to timestamp
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

    #creating a connection to the database
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    engine.connect()

    #inserting the data into the database
    #create an iterator to insert data in chunks
    df_iter = pd.read_csv(csv_file,iterator=True,chunksize=100000)
 
    #just like generators we can use the next function to view what record/s will be inserted next
    df = next(df_iter)

    #converting the -tpep_pickup_datetime & tpep_dropoff_datetime to timestamp
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    from time import time

    while True:
        try:        
            t0 = time()
            df = next(df_iter)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.to_sql(name=tbname,con=engine,if_exists='append')
            t1 = time()
            t2 = t1-t0
        except StopIteration:
            break
    print("Last Chunk of data inserted")
    print(f"Whole process took {t2} amount of time")
        
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres.')

#user, 
# password, 
# host, 
# port, 
# database name,
# table name, 
# csv file path

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres.')
    parser.add_argument('--user',help='Username for Postgres')
    parser.add_argument('--password',help='Password for Postgres')
    parser.add_argument('--host',help='Host for Postgres')
    parser.add_argument('--port',help='port for Postgres')
    parser.add_argument('--dbname',help='Database name for Postgres')
    parser.add_argument('--tbname',help='table name for Postgres')
    parser.add_argument('--url',help='data url')
    args = parser.parse_args()

    main(args)

