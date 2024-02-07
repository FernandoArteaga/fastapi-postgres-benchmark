# -*- coding: utf-8 -*-
import asyncpg
import psycopg
import psycopg_pool
from psycopg.rows import class_row
from src.config import config
from src.models import Person

db_config = config.database
conn_string = f"postgresql://{db_config.username}:{db_config.pwd}@{db_config.host}:{db_config.port}/{db_config.name}"


QUERY_GET_ALL = "SELECT name, age FROM users"


class DBConnector:
    def __init__(self):
        self.asyncpg_pool = None
        self.psyco_async_pool: psycopg_pool.AsyncConnectionPool = psycopg_pool.AsyncConnectionPool(conn_string)
        self.psyco_pool: psycopg_pool.ConnectionPool = psycopg_pool.ConnectionPool(conn_string)

    async def create_asyncpg_pool(self):
        self.asyncpg_pool: asyncpg.Pool = await asyncpg.create_pool(conn_string)
        
    async def end(self):
        self.psyco_pool.close()
        await self.psyco_async_pool.close()
        await self.asyncpg_pool.close()


def psycopg_get_all(conn: psycopg.Connection):
    cur = conn.cursor(row_factory=class_row(Person))
    rows = cur.execute(QUERY_GET_ALL)
    return rows.fetchall()


async def psycopg_get_all_async(conn: psycopg.AsyncConnection):
    cur = conn.cursor(row_factory=class_row(Person))
    rows = await cur.execute(QUERY_GET_ALL)
    return await rows.fetchall()


async def asyncpg_get_all(conn: asyncpg.Connection):
    async with conn.transaction():
        rows = await conn.fetch(QUERY_GET_ALL)
        return [Person(**row) for row in rows]
