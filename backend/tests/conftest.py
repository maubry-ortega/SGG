import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app as main_app
from src.core.database import Base, get_db
from src.core.config import settings

# --- SQL Test Config ---
# For testing, we can use a local sqlite or a separate test schema in Neon
# Here we use the main SQL URL as provided but it's recommended to have a separate TEST_DATABASE_URL
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    # Create tables in the test DB
    Base.metadata.create_all(bind=engine)
    
    # Clean SQL tables before session using TRUNCATE CASCADE
    from sqlalchemy import text
    db = TestingSessionLocal()
    try:
        # Rollback any pending transactions first
        db.rollback()
        
        # Postgres-specific: TRUNCATE with CASCADE usually handles FKs better than DELETE order
        # Explicitly truncate core tables to ensure safety
        tables = ["audit_logs", "users", "programs", "regions"]
        for table in tables:
            try:
                db.execute(text(f"TRUNCATE TABLE {table} RESTART IDENTITY CASCADE"))
            except Exception:
                pass 
        db.commit()
        yield db
    finally:
        db.close()



@pytest.fixture(scope="function")
async def client(db_session):
    from httpx import AsyncClient, ASGITransport
    # Override get_db dependency to use the test session
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    main_app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=main_app), base_url="http://test") as c:
        yield c
    main_app.dependency_overrides.clear()

@pytest.fixture(scope="function", autouse=True)
async def init_test_mongodb():
    """Initializes MongoDB for testing using the DB name from environment."""
    from motor.motor_asyncio import AsyncIOMotorClient
    from beanie import init_beanie
    from src.shared.models.resource import SaggiResource, Comment
    
    # Use saggi_test_db if it exists, or fall back to MONGODB_DB_NAME
    test_db_name = os.getenv("MONGODB_TEST_DB_NAME", "saggi_test_db")
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    db = client[test_db_name]
    
    # Clean the test DB
    await client.drop_database(test_db_name)
    
    await init_beanie(
        database=db,
        document_models=[
            SaggiResource,
            Comment,
        ]
    )
    yield
    # Explicit close to avoid pending task errors
    client.close()

@pytest.fixture
async def auth_header(client):
    """Fixture to get a valid JWT header for a test user."""
    import uuid
    random_str = str(uuid.uuid4())[:8]
    username = f"testuser_{random_str}"
    email = f"test_{random_str}@saggi.com"

    # Create a test user
    user_data = {
        "full_name": "Test User",
        "email": email,
        "username": username,
        "password": "testpassword123"
    }
    await client.post(f"{settings.API_V1_STR}/users/", json=user_data)
    
    # Login
    login_res = await client.post(f"{settings.API_V1_STR}/auth/login", json={
        "username": username,
        "password": "testpassword123"
    })
    token = login_res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}
