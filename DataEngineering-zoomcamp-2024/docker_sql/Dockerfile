FROM python:3.10

RUN apt-get install curl
RUN pip install sqlalchemy psycopg2 pandas requests


WORKDIR /app
RUN mkdir /app/my_taxi_postgres_data


COPY ingest_data.py /app/ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]