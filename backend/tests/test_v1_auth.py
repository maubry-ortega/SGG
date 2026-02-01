import pytest
from src.core.config import settings

@pytest.mark.asyncio
async def test_health_grid(client):
    response = await client.get(f"{settings.API_V1_STR}/health-grid")
    assert response.status_code == 200
    assert response.json() == {"status": "SGG Core Grid operational"}

@pytest.mark.asyncio
async def test_user_registration_and_login(client):
    # 1. Register
    user_data = {
        "full_name": "Auth Tester",
        "email": "tester@saggi.com",
        "username": "tester",
        "password": "strongpassword123"
    }
    reg_response = await client.post(f"{settings.API_V1_STR}/users/", json=user_data)
    assert reg_response.status_code == 201
    
    # 2. Login
    login_data = {
        "username": "tester",
        "password": "strongpassword123"
    }
    login_response = await client.post(f"{settings.API_V1_STR}/auth/login", json=login_data)
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    assert "refresh_token" in login_response.json()

@pytest.mark.asyncio
async def test_login_invalid_credentials(client):
    login_data = {
        "username": "nonexistent",
        "password": "wrongpassword"
    }
    response = await client.post(f"{settings.API_V1_STR}/auth/login", json=login_data)
    assert response.status_code == 401

