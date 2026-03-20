"""Application configuration using Pydantic settings."""

from functools import lru_cache

from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    app_name: str = "Platform for Job Research"
    debug: bool = False
    database_url: str = "sqlite+aiosqlite:///./dev.db"
    secret_key: str = "changeme"
    access_token_expire_minutes: int = 60 * 24
    cors_origins: list[AnyHttpUrl] = ["http://localhost", "http://localhost:3000"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
