from pydantic import BaseSettings


class Setting(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    
    database_url: str = "DATABASE_URL"

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Setting(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
