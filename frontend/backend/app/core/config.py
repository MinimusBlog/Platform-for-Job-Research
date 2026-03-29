from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Tramplin"
    SECRET_KEY: str = "your-super-secret-key"  # Позже вынесем в .env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    DATABASE_URL: str = "postgresql+asyncpg://postgres:pass@localhost:5432/tramplin_db"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()