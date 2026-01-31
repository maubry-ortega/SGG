from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "SGG Smart Guide Grid"
    PRODUCT_NAME: str = "Saggi"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # SQL DB (Neon) - Pulled from .env
    SQLALCHEMY_DATABASE_URL: str
    
    # NoSQL DB (MongoDB) - Pulled from .env
    MONGODB_URL: str
    MONGODB_DB_NAME: str = "saggi_db"
    MONGODB_TEST_DB_NAME: str = "saggi_test_db"

    # JWT - Pulled from .env
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # Email
    EMAIL_USER: Optional[str] = None
    EMAIL_PASSWORD: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env", 
        case_sensitive=True, 
        extra="ignore", # Allow undefined env vars
        env_file_encoding='utf-8'
    )



settings = Settings()
