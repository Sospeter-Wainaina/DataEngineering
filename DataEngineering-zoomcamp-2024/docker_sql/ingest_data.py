import pandas as pd
from sqlalchemy import create_engine
import os
import argparse
import requests
import shutil
import gzip

def download_extract(url, path, new_filename):
    response = requests.get(url)
    if response.status_code == 200:
        full_path = os.path.join(path, new_filename)
        with open(full_path, "wb") as f:
            f.write(response.content)
        extract_folder = os.path.join(path, "extract_folder")
        os.makedirs(extract_folder, exist_ok=True)
        # Extract the CSV file from the .gz archive
        csv_filename = "file.csv"
        csv_path = os.path.join(extract_folder, csv_filename)
        with gzip.open(full_path, 'rb') as f_in, open(csv_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        return csv_path
    else:
        print(f"Failed to download {url}. Status code: {response.status_code}")
        return None

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.dbname
    tbname = params.tbname
    url = params.url

    # Download and extract the data
    csv_file = download_extract(url, "./my_taxi_postgres_data", "yellow_tripdata_2021-07.csv.gz")

    if csv_file:
        # Loading the decompressed CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        # converting the -tpep_pickup_datetime & tpep_dropoff_datetime to timestamp
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

        # creating a connection to the database
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
        engine.connect()

        # inserting the data into the database
        # create an iterator to insert data in chunks
        df_iter = pd.read_csv(csv_file, iterator=True, chunksize=100000)

        # just like generators we can use the next function to view what record/s will be inserted next
        df = next(df_iter)

        # converting the -tpep_pickup_datetime & tpep_dropoff_datetime to timestamp
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        from time import time

        while True:
            try:
                t0 = time()
                df = next(df_iter)
                df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
                df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
                df.to_sql(name=tbname, con=engine, if_exists='append')
                t1 = time()
                t2 = t1 - t0
            except StopIteration:
                break
        print("Last Chunk of data inserted")
        print(f"Whole process took {t2} amount of time")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres.')
    parser.add_argument('--user', help='Username for Postgres')
    parser.add_argument('--password', help='Password for Postgres')
    parser.add_argument('--host', help='Host for Postgres')
    parser.add_argument('--port', help='port for Postgres')
    parser.add_argument('--dbname', help='Database name for Postgres')
    parser.add_argument('--tbname', help='table name for Postgres')
    parser.add_argument('--url', help='data url')
    args = parser.parse_args()

    main(args)
