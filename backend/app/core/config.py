from pydantic import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str = 'postgres'
    POSTGRES_PASSWORD: str = 'postgres'
    POSTGRES_DB: str = 'guards_db'
    DATABASE_URL: str = 'postgresql://postgres:postgres@db:5432/guards_db'
    SECRET_KEY: str = 'supersecretkey'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = '.env'

settings = Settings()
