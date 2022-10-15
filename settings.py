from pydantic import BaseSettings


class Setting(BaseSettings):
    sever_host: str = '127.0.0.1'
    sever_port: int = 8000
    database_url: str = "postgresql://postgres:qwerty@localhost/blog"

    jwt_secret: str
    jwt_algorithm: str = 'HS256'


settings = Setting(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
