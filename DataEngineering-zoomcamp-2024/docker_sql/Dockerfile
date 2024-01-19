FROM python:3.10

RUN apt-get install curl
RUN pip install sqlalchemy psycopg2 pandas

WORKDIR /app

COPY ingest_data.py /app/ingest_data.py

ENTRYPOINT ["python", "pipeline.py"]