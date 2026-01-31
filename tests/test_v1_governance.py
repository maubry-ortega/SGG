import pytest
from src.core.config import settings

@pytest.mark.asyncio
async def test_create_and_list_regions(client, auth_header):
    # 1. Create a region
    region_data = {"name": "Amazonia"}
    response = await client.post(f"{settings.API_V1_STR}/gov/regions", json=region_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Amazonia"
    assert "id" in data

    # 2. List regions
    response = await client.get(f"{settings.API_V1_STR}/gov/regions")
    assert response.status_code == 200
    assert len(response.json()) >= 1

@pytest.mark.asyncio
async def test_create_and_list_programs(client):
    program_data = {"name": "Desarrollo de Software"}
    response = await client.post(f"{settings.API_V1_STR}/gov/programs", json=program_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Desarrollo de Software"

    response = await client.get(f"{settings.API_V1_STR}/gov/programs")
    assert response.status_code == 200
    assert len(response.json()) >= 1

