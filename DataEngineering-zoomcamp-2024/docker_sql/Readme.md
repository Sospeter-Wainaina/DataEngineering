# Docker and PostgreSQL for Data Engineers

## Table of Contents

1. [Docker](#docker)
   - [What is Docker?](#what-is-docker)
   - [Why Docker?](#why-docker)
   - [Installing Docker](#installing-docker)
2. [Why Data Engineers Should Care About Docker](#why-data-engineers-should-care-about-docker)
3. [Running PostgreSQL Locally with Docker](#running-postgresql-locally-with-docker)
4. [Putting Data for Testing to Local PostgreSQL with Python](#putting-data-for-testing-to-local-postgresql-with-python)
5. [Packaging the Script in Docker](#packaging-the-script-in-docker)
6. [Running PostgreSQL and the Script in One Network](#running-postgresql-and-the-script-in-one-network)
7. [Docker Compose and Running pgAdmin and PostgreSQL Together](#docker-compose-and-running-pgadmin-and-postgresql-together)
8. [SQL: Group By, Joins, Window Function, Union](#sql-group-by-joins-window-function-union)

---

## Docker

### What is Docker?

Docker allows you to encapsulate an application and its dependencies into a container, providing a consistent and isolated environment. A container includes the operating system, system-level libraries, and the application itself. Docker containers can run on any host machine, regardless of its underlying operating system.

### Why Docker?

- **Isolation:** Containers are isolated from the host machine environment, preventing conflicts between different applications and dependencies.
- **Portability:** Docker containers can run consistently across different environments, making it easy to deploy applications.
- **Scalability:** Multiple containers can run on a single host without conflict, enabling efficient resource utilization.
- **Consistency:** Docker ensures that the application behaves the same way in development, testing, and production environments.

### Installing Docker

Install Docker by following the instructions provided in the official documentation: [Docker Installation](https://docs.docker.com/get-docker/).

---

## Why Data Engineers Should Care About Docker

1. **Setting up Locally for Experiments:** Docker simplifies the setup of environments for testing and experimentation.
2. **Integration Tests and CI/CD:** Docker containers can be used for running integration tests and facilitating continuous integration and deployment pipelines.
3. **Batch Jobs, Spark, and Serverless:** Docker is valuable in various data engineering scenarios, including running batch jobs, managing Spark clusters, and deploying serverless functions.

---

## Running PostgreSQL Locally with Docker

For practicing SQL, we'll use PostgreSQL, a powerful and versatile database.

To run PostgreSQL locally with Docker, use the following command:

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v "./ny-taxi-volume:/var/lib/postgresql/data" \
  --network=pg-network \
  --name pg-database \
  -p 5433:5432 \
  postgres:14
```

For this case I mapped 5433 to 5432 in the container to avoid conflicts with my localy installed postgres db which uses the same port

The pgcli is a CLI and its not really convenient when it comes to running commands and seeing the tables. for that we are going to use a web based GUI where we can run our queries and see how the data looks like. To pull the image and run it we will go to the following link.

[PgAdmin4 Installation](https://www.pgadmin.org/download/).

To pull and run the docker image containing the pgadmin4:

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pg-admin \
  dpage/pgadmin4
```

So when we try connecting to the pgadmin4 via `localhost:8080` We can now connect. To connect to the postgres database which is in another different container we will need to put them in the same network so that they can be able to communicate to do that we willuse the following command to create a network:

```
docker network create pg-network
```

so what we need to do next is to convert our notebook into a script so that we can run it from our terminal. The way we can do that is by using the `nbconvert` see below:

`jupyter nbconvert --to script [NOTEBOOK].ipynb`

It will need some cleaning and we need to add some code so that we can pass some arguments when executing our script such as :
_ user
_ password
_ host
_ port
_ dbname
_ tablename \* url
That can be made possible through a module in python known as argparse
You can find documentation in the following link: [argparse](https://docs.python.org/3/library/argparse.html).

After that now we will pass arguments to our script like so:

```
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-07.csv.gz"
python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5433 \
    --dbname=ny_taxi \
    --tbname=yellow_taxi_data \
    --url=${URL}
```

And it will populate data in our postgres database

Now next we are going to dockerize everything instead of running it in our localhost and the way we are going to do that is by altering our docker file and write instructions that will install any libraries and create any directories that our code might require. Then we will build it and run our image.

To create our image we will run this cli command in our terminal:
bash

```
docker build -t taxi_ingest:v001 .
```

We will then run and assign it a terminal ans we want it to be interactive:

```
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-07.csv.gz"
docker run -it taxi_ingest:v001 \
    --network=pg-network
    --user=root \
    --password=root \
    --host=localhost \
    --port=5433 \
    --dbname=ny_taxi \
    --tbname=yellow_taxi_data \
    --url=${URL}
```
