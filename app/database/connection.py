import psycopg
from psycopg_pool import AsyncConnectionPool
from contextlib import asynccontextmanager
from app.core.config import settings

connection_pool: AsyncConnectionPool | None = None

async def init_db():
  """Initialize the database connection pool."""
  global connection_pool
  if connection_pool is None:
    connection_pool = AsyncConnectionPool(
      conninfo=settings.database_url,
      min_size=1,
      max_size=10,
      timeout=30,
      max_idle=300,
      max_lifetime=3600,
      open=False
    )
    await connection_pool.open()
  print("✅ Database connection pool initialized.")
  

async def close_db():
  """Close all connections in the pool."""
  global connection_pool
  if connection_pool:
    await connection_pool.close()
    connection_pool = None
  print("✅ Database connection pool closed.")


@asynccontextmanager
async def get_db_connection():
  """Context manager to get a database connection from the pool."""
  global connection_pool
  if connection_pool is None:
    raise Exception("Connection pool is not initialized. Call init_db() first.")
  
  async with connection_pool.connection() as conn:
    try:
      yield conn
      await conn.commit()
    except Exception as e:
      await conn.rollback()
      raise Exception(f"Database operation failed: {e}")
    

async def get_db():
  """Dependency to get a database connection."""
  try:
    async with get_db_connection() as conn:
      yield conn
  except Exception as e:
    raise Exception(f"Failed to get database connection: {e}")