from pydantic_settings import BaseSettings

import os


class DbSettings(BaseSettings):
    postgres_host: str
    postgres_port: int
    postgres_db: str
    postgres_user: str
    postgres_password: str

    @property
    def async_connection_string(self):
        user = self.postgres_user
        psswrd = self.postgres_password
        host = self.postgres_host
        port = self.postgres_port
        db = self.postgres_db
        return f"postgresql+asyncpg://{user}:{psswrd}@{host}:{port}/{db}"


class AppSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8888


app_settings: AppSettings = AppSettings()
db_settings: DbSettings = DbSettings()
