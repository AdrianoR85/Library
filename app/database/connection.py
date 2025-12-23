import psycopg
from psycopg_pool import AsyncConnectionPool
from contextlib import asynccontextmanager
from app.core.config import settings
from typing import AsyncGenerator

connection_pool: AsyncConnectionPool | None = None

async def init_db() -> None:
  """Initialize the database connection pool."""
  global connection_pool
  if connection_pool is None:
    connection_pool = AsyncConnectionPool(
      conninfo=settings.database_url,
      min_size=1,        # Always keep 1 connection ready
      max_size=10,       # Never create more than 10 connections
      timeout=30,        # Wait max 30 seconds for a free connection
      max_idle=300,      # Close connections idle for 5 minutes
      max_lifetime=3600, # Close connections older than 1 hour
      check=AsyncConnectionPool.check_connection,
      open=False
    )
    await connection_pool.open()
  print("✅ Database connection pool initialized.")
  

async def close_db() -> None:
  """Close all connections in the pool."""
  global connection_pool
  if connection_pool:
    await connection_pool.close()
    connection_pool = None
  print("✅ Database connection pool closed.")


@asynccontextmanager
async def get_db_connection() -> AsyncGenerator[psycopg.AsyncConnection, None]:
  """Context manager to get a database connection from the pool."""
  global connection_pool
  if connection_pool is None:
    raise RuntimeError("Connection pool is not initialized. Call init_db() first.")
  
  async with connection_pool.connection() as conn:
    try:
      yield conn
      await conn.commit()
    except Exception as e:
      await conn.rollback()
      raise Exception(f"Database operation failed: {e}")
    

async def get_db() -> AsyncGenerator[psycopg.AsyncConnection, None]:
  """Dependency to get a database connection."""
  async with get_db_connection() as conn:
        yield conn