from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from src.db import DBConnector, asyncpg_get_all
from src.db import psycopg_get_all, psycopg_get_all_async
from src.dependencies import get_psycopg_db_connection, get_psycopg_async_db_connection, get_asyncpg_db_connection
from src.models import Person


@asynccontextmanager
async def lifespan(application: FastAPI):
    # Creates database connections when the FastAPI application starts.
    application.state.db_connector = DBConnector()
    await application.state.db_connector.create_asyncpg_pool()
    yield
    # Closes the database connection when the FastAPI application is shut down.
    await application.state.db_connector.end()


app = FastAPI(
    title="FastAPI PostgreSQL Benchmark",
    lifespan=lifespan,
)


@app.get("/", response_class=RedirectResponse)
def root():
    return RedirectResponse("/docs")


@app.get(
    "/psycopg/sync",
    response_model=list[Person],
    summary="Sync request to the database using psycopg",
)
async def endpoint_psycopg_get_all(db=Depends(get_psycopg_db_connection)):
    try:
        return psycopg_get_all(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.get(
    "/psycopg/async",
    response_model=list[Person],
    summary="Async request to the database using psycopg",
)
async def endpoint_psycopg_get_all_async(db=Depends(get_psycopg_async_db_connection)):
    try:
        return await psycopg_get_all_async(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@app.get(
    "/asyncpg/async",
    response_model=list[Person],
    summary="Async request to the database using asyncpg",
)
async def endpoint_asyncpg_get_all_async(db=Depends(get_asyncpg_db_connection)):
    try:
        return await asyncpg_get_all(db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
