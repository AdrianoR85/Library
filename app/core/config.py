from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  """ Application configuration settings loaded from environment variables."""
  # Database settings
  DATABASE_HOST: str 
  DATABASE_PORT: int
  DATABASE_NAME: str 
  DATABASE_USER: str 
  DATABASE_PASSWORD: str 
  # Security settings
  SECRET_KEY: str 
  ALGORITHM: str 
  ACCESS_TOKEN_EXPIRE_MINUTES: int 
  # Application settings 
  APP_NAME: str 
  APP_VERSION: str 
  DEBUG: bool 


  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"


  @property
  def database_url(self) -> str:
    return f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
  

settings = Settings() # type: ignore