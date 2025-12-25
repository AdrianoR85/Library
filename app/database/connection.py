from app.core.config import settings
from typing import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


engine = create_engine(
  settings.database_url, #Must be: postgresql+asyncpg://user:pass@host/db
  echo=True,  # Show SQL queries (remove in production)
  pool_size=10, # maximum number of connections in the pool
  pool_timeout=30, # pool wait timeout in seconds
  max_overflow=20, # Extra connections when needed
  pool_pre_ping=True # Check if connections are alive
)

if not database_exists(engine.url):
    create_database(engine.url)
    print(f"✅ Database {settings.DATABASE_NAME} created.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db() -> AsyncGenerator:
    """Provide a database session to path operations."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


