"""Database setup and SQLAlchemy utilities."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import get_settings

settings = get_settings()

# Use echo=True for debug logging if needed.
engine = create_engine(settings.database_url, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

Base = declarative_base()
