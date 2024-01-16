FROM python:3.10

RUN pip install pandas

WORKDIR /app

COPY pipeline.py /app/pipeline.py

ENTRYPOINT ["python", "pipeline.py"]