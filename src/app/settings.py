"""Настройки подключения"""
import os
from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv())

class Setting(BaseSettings):# pylint: disable=too-few-public-methods``
    """Базовые настройки"""
    server_host: str = '0.0.0.0'
    server_port: int = 8000

    database_url: str = os.getenv("DATABASE_URL")

    jwt_secret: str = os.getenv("JWT_SECRET")
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


setting = Setting(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
