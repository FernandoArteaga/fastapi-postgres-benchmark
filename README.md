# FastAPI PostgreSQL Benchmark

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

Benchmark the responsiveness of a FastAPI when reading data from a Postgres DB using an async vs sync implementation.

## Setup

### Workspace

* [Python 3.12](https://www.python.org/downloads/release/python-3121/)

### Project dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment variables

Copy the placeholder file `.env.example` as `.env` and configure the variables inside as needed

```bash
cp .env.example .env
```

Description:

| Variable name | Default value                | Description                                    |
|---------------|------------------------------|------------------------------------------------|
| API_HOST      | `7755`                       | The API host                                   |
| DB_HOST       | `127.0.0.1`                  | The database host                              |
| DB_PORT       | `5432`                       | The database port                              |
| DB_USERNAME   | `postgres`                   | The username to authenticate with the database |
| DB_PASSWORD   | `secret`                     | The user's password                            |
| DB_NAME       | `fastapi-postgres-benchmark` | The database name                              |

### Database

Start the database using the provided docker-compose file

```bash
make start
```

Create the database and the table for running the benchmarks

```bash
make seed
```

### Run the API

Start the FastAPI application

```bash
python src/main.py
```

## Benchmarks

_Note: Benchmark are executed locally using the [wrk](https://github.com/wg/wrk?tab=readme-ov-file) tool_

We'll read all the users (250) from the DB using different implementations the DB connector.

### psycopg sync connector

Parameters:

* Endpoint: /psycopg/sync
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/sync`

Results:

| Thread Stats | Avg      | Stdev    | Max    | +/- Stdev |
|--------------|----------|----------|--------|-----------|
| Latency      | 748.75ms | 205.02ms | 1.04s  | 67.27%    |
| Req/Sec      | 28.07    | 18.80    | 150.00 | 76.28%    |

- 38006 requests in 2.00m, 236.68MB read
- Socket errors: connect 158, read 122, write 0, timeout 0
- Requests/sec: 316.47
- Transfer/sec: 1.97MB

### psycopg async connector

Parameters:

* Endpoint: /psycopg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/async`

Results:

| Thread Stats | Avg      | Stdev  | Max      | +/- Stdev |
|--------------|----------|--------|----------|-----------|
| Latency      | 163.90ms | 7.67ms | 279.98ms | 89.62%    |
| Req/Sec      | 121.35   | 36.60  | 230.00   | 64.66%    |

- 174168 requests in 2.00m, 1.06GB read
- Socket errors: connect 158, read 102, write 0, timeout 0
- Requests/sec: 1450.35
- Transfer/sec: 9.03MB

### asyncpg async connector

Parameters:

* Endpoint: /asyncpg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/asyncpg/async`

Results:

| Thread Stats | Avg      | Stdev   | Max    | +/- Stdev |
|--------------|----------|---------|--------|-----------|
| Latency      | 155.66ms | 88.66ms | 1.23s  | 74.67%    |
| Req/Sec      | 128.67   | 59.72   | 333.00 | 65.48%    |

- 184649 requests in 2.00m, 1.12GB read
- Socket errors: connect 158, read 106, write 0, timeout 0
- Requests/sec: 1537.50
- Transfer/sec: 9.57MB
