# -*- coding: utf-8 -*-
import os
import sys
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class APIConfig:
    port = int(os.getenv("API_PORT", 7755)) or 7755


@dataclass(frozen=True)
class DatabaseConfig:
    host = os.getenv("DB_HOST") or sys.exit("Environment variable DB_HOST is required")
    port = os.getenv("DB_PORT", 5432)
    username = os.getenv("DB_USERNAME") or sys.exit(
        "Environment variable DB_USERNAME is required"
    )
    pwd = os.getenv("DB_PASSWORD") or sys.exit(
        "Environment variable DB_PASSWORD is required"
    )
    name = os.getenv("DB_NAME", "circuits-service")
    ssl = os.getenv("DB_SSL_MODE", "disable")


@dataclass(frozen=True)
class Config:
    api = APIConfig()
    database = DatabaseConfig()


config = Config()
