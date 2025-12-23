from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  """ Application configuration settings loaded from environment variables."""
  # Database settings
  DATABASE_HOST: str = "localhost"
  DATABASE_PORT: int = 5432
  DATABASE_NAME: str = "library_db"
  DATABASE_USER: str = "postgres"
  DATABASE_PASSWORD: str = "password"
  # Security settings
  SECRET_KEY: str = "your-secret-key-change-in-production"
  ALGORITHM: str = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
  # Application settings 
  APP_NAME: str = "Library API"
  APP_VERSION: str = '1.0.0'
  DEBUG: bool = True


  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"


  @property
  def database_url(self) -> str:
    return f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
  

settings = Settings()