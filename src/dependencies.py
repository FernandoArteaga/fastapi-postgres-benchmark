from asyncpg import Pool
from psycopg_pool import AsyncConnectionPool, ConnectionPool

from fastapi.requests import Request


def get_psycopg_db_connection(request: Request):
    """
    Returns a psycopg DB connection from the DB connection pool.
    """
    pool: ConnectionPool = request.app.state.db_connector.psyco_pool
    with pool.connection(None) as conn:
        yield conn


async def get_psycopg_async_db_connection(request: Request):
    """
    Returns a psycopg DB connection from the DB connection pool.
    """
    pool: AsyncConnectionPool = request.app.state.db_connector.psyco_async_pool
    async with pool.connection(None) as conn:
        yield conn


async def get_asyncpg_db_connection(request: Request):
    """
    Returns an asyncpg DB connection from the DB connection pool.
    """
    pool: Pool = request.app.state.db_connector.asyncpg_pool
    async with pool.acquire() as conn:
        yield conn
