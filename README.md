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

<!-- TOC -->
* [Benchmarks](#benchmarks)
  * [Read **50** users from the DB](#read-50-users-from-the-db)
    * [🥉 psycopg sync connector](#-psycopg-sync-connector)
    * [🥈 psycopg async connector](#-psycopg-async-connector)
    * [🥇 asyncpg async connector](#-asyncpg-async-connector)
  * [Read **250** users from the DB](#read-250-users-from-the-db)
    * [🥉 psycopg sync connector](#-psycopg-sync-connector-1)
    * [🥈 psycopg async connector](#-psycopg-async-connector-1)
    * [🥇 asyncpg async connector](#-asyncpg-async-connector-1)
  * [Read **1000** users from the DB](#read-1000-users-from-the-db)
    * [🥉 psycopg sync connector](#-psycopg-sync-connector-2)
    * [🥇 psycopg async connector](#-psycopg-async-connector-2)
    * [🥈 asyncpg async connector](#-asyncpg-async-connector-2)
  * [Read **5000** users from the DB](#read-5000-users-from-the-db)
    * [🥉 psycopg sync connector](#-psycopg-sync-connector-3)
    * [🥇 psycopg async connector](#-psycopg-async-connector-3)
    * [🥈 asyncpg async connector](#-asyncpg-async-connector-3)
<!-- TOC -->

### Read **50** users from the DB

#### 🥉 psycopg sync connector

Parameters:

* Endpoint: /psycopg/sync
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/sync`

Results:

| Thread Stats | Avg      | Stdev    | Max      | +/- Stdev |
|--------------|----------|----------|----------|-----------|
| Latency      | 304.00ms | 247.62ms | 967.04ms | 76.47%    |
| Req/Sec      | 80.18    | 74.86    | 333.00   | 76.60%    |

- 93656 requests in 2.00m, 126.21MB read
- Socket errors: connect 158, read 112, write 0, timeout 0
- Requests/sec: 779.80
- Transfer/sec: 1.05MB

#### 🥈 psycopg async connector

Parameters:

* Endpoint: /psycopg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/async`

Results:

| Thread Stats | Avg     | Stdev  | Max      | +/- Stdev |
|--------------|---------|--------|----------|-----------|
| Latency      | 88.11ms | 8.72ms | 216.74ms | 90.14%    |
| Req/Sec      | 225.99  | 83.09  | 484.00   | 69.62%    |

- 324102 requests in 2.00m, 436.74MB read
- Socket errors: connect 158, read 106, write 0, timeout 0
- Requests/sec: 2698.62
- Transfer/sec: 3.64MB

#### 🥇 asyncpg async connector

Parameters:

* Endpoint: /asyncpg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/asyncpg/async`

Results:

| Thread Stats | Avg     | Stdev   | Max      | +/- Stdev |
|--------------|---------|---------|----------|-----------|
| Latency      | 74.26ms | 41.51ms | 612.29ms | 74.61%    |
| Req/Sec      | 269.64  | 91.41   | 565.00   | 62.15%    |

- 386681 requests in 2.00m, 521.07MB read
- Socket errors: connect 158, read 106, write 0, timeout 0
- Requests/sec: 3219.51
- Transfer/sec: 4.34MB

### Read **250** users from the DB

#### 🥉 psycopg sync connector

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

#### 🥈 psycopg async connector

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

#### 🥇 asyncpg async connector

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

### Read **1000** users from the DB

#### 🥉 psycopg sync connector

Parameters:

* Endpoint: /psycopg/sync
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/sync`

Results:

| Thread Stats | Avg      | Stdev   | Max    | +/- Stdev |
|--------------|----------|---------|--------|-----------|
| Latency      | 925.00ms | 73.91ms | 1.22s  | 72.15%    |
| Req/Sec      | 28.07    | 18.80   | 150.00 | 76.28%    |

- 30764 requests in 2.00m, 755.09MB read
- Socket errors: connect 158, read 124, write 0, timeout 0
- Requests/sec: 256.15
- Transfer/sec: 6.29MB

#### 🥇 psycopg async connector

Parameters:

* Endpoint: /psycopg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/async`

Results:

| Thread Stats | Avg      | Stdev   | Max      | +/- Stdev |
|--------------|----------|---------|----------|-----------|
| Latency      | 517.43ms | 35.68ms | 705.28ms | 74.58%    |
| Req/Sec      | 46.16    | 33.04   | 161.00   | 60.40%    |

- 55102 requests in 2.00m, 1.32GB read
- Socket errors: connect 158, read 98, write 0, timeout 0
- Requests/sec: 458.79
- Transfer/sec: 11.26MB

#### 🥈 asyncpg async connector

Parameters:

* Endpoint: /asyncpg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/asyncpg/async`

Results:

| Thread Stats | Avg      | Stdev    | Max    | +/- Stdev |
|--------------|----------|----------|--------|-----------|
| Latency      | 516.99ms | 277.76ms | 2.00s  | 73.42%    |
| Req/Sec      | 39.04    | 21.50    | 150.00 | 75.20%    |

- 55070 requests in 2.00m, 1.32GB read
- Socket errors: connect 158, read 103, write 0, timeout 27
- Requests/sec: 458.63
- Transfer/sec: 11.26MB

### Read **5000** users from the DB

#### 🥉 psycopg sync connector

Parameters:

* Endpoint: /psycopg/sync
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/sync`

Results:

| Thread Stats | Avg   | Stdev    | Max   | +/- Stdev |
|--------------|-------|----------|-------|-----------|
| Latency      | 1.05s | 534.39ms | 1.97s | 60.14%    |
| Req/Sec      | 8.01  | 5.95     | 50.00 | 79.42%    |

- 8716 requests in 2.00m, 1.04GB read
- Socket errors: connect 158, read 133, write 0, timeout 8578
- Requests/sec: 72.57
- Transfer/sec: 8.87MB

#### 🥇 psycopg async connector

Parameters:

* Endpoint: /psycopg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/psycopg/async`

Results:

| Thread Stats | Avg   | Stdev    | Max   | +/- Stdev |
|--------------|-------|----------|-------|-----------|
| Latency      | 1.08s | 575.88ms | 2.00s | 57.81%    |
| Req/Sec      | 11.19 | 6.59     | 50.00 | 60.92%    |

- 13263 requests in 2.00m, 1.58GB read
- Socket errors: 158, read 104, write 0, timeout 13026
- Requests/sec: 110.44
- Transfer/sec: 13.50MB

#### 🥈 asyncpg async connector

Parameters:

* Endpoint: /asyncpg/async
* Threads: 12
* Connections: 400 (total number of HTTP connections to keep open with each thread handling `N = connections/threads`)
* Duration: 2m
* CLI command: `wrk -t12 -c400 -d2m http://localhost:7755/asyncpg/async`

Results:

| Thread Stats | Avg      | Stdev    | Max   | +/- Stdev |
|--------------|----------|----------|-------|-----------|
| Latency      | 212.79ms | 344.99ms | 1.95s | 91.28%    |
| Req/Sec      | 11.42    | 8.74     | 80.00 | 82.07%    |

- 11376 requests in 2.00m, 1.36GB read
- Socket errors: connect 158, read 109, write 0, timeout 9851
- Requests/sec: 94.74
- Transfer/sec: 11.58MB
