from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings

# --- SQL Database (Neon) ---
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get SQL session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- NoSQL Database (MongoDB) ---
mongo_client = AsyncIOMotorClient(settings.MONGODB_URL)
mongo_db = mongo_client[settings.MONGODB_DB_NAME]

async def init_beanie_db():
    from beanie import init_beanie
    from src.shared.models.resource import SaggiResource, Comment
    
    await init_beanie(
        database=mongo_db,
        document_models=[
            SaggiResource,
            Comment,
        ]
    )

