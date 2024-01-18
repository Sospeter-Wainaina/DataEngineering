
import pandas as pd
from sqlalchemy import create_engine

import argparse

def main():
    df = pd.read_csv("my_taxi_postgres_data/yellow_tripdata_2021-01.csv")
    #converting the -tpep_pickup_datetime & tpep_dropoff_datetime to timestamp
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

    #creating a connection to the database
    engine = create_engine('postgresql://root:root@localhost:5433/ny_taxi')
    engine.connect()

    #inserting the data into the database
    #create an iterator to insert data in chunks
    df_iter = pd.read_csv('my_taxi_postgres_data/yellow_tripdata_2021-01.csv',iterator=True,chunksize=100000)
 
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
        df.to_sql(name='yellow_taxi_data',con=engine,if_exists='append')
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
parser.add_argument('user',help='Username for Postgres')
parser.add_argument('pass',help='Password for Postgres')
parser.add_argument('host',help='Host for Postgres')
parser.add_argument('port',help='port for Postgres')
parser.add_argument('dbname',help='Database name for Postgres')
parser.add_argument('tbname',help='table name for Postgres')
parser.add_argument('csvpath',help='csv file path for Postgres')


args = parser.parse_args()
print(args.accumulate(args.integers))

