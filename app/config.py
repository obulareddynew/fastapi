from pydantic_settings import BaseSettings
import os


print("=== DEBUG: PRINTING ENVIRONMENT VARIABLES ===")
for key, value in os.environ.items():
    print(f"{key}: {value}")
class Settings(BaseSettings):
    database_hostname: str = os.getenv("DATABASE_HOSTNAME")
    database_port: str = os.getenv("DATABASE_PORT")
    database_password: str = os.getenv("DATABASE_PASSWORD")
    database_username: str = os.getenv("DATABASE_USERNAME")
    database_name: str = os.getenv("DATABASE_NAME")
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = os.getenv("ALGORITHM")
    access_token_expire_minutes: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)

    class Config:
        case_sensitive = True  # Ensures Railway env vars are read correctly
        extra = "allow"  # Allows extra env variables if needed


settings = Settings()
