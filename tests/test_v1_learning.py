import pytest
from src.core.config import settings

@pytest.mark.asyncio
async def test_create_and_retrieve_resource(client, auth_header):
    # Resource creation usually requires an instructor_id from the user. 
    # In a real scenario, we'd extract user from token. 
    # For this test, we create a dummy resource.
    
    resource_data = {
        "title": "Guía de Python Avanzado",
        "description": "Domina las estructuras de datos.",
        "instructor_id": 1,
        "tags": ["python", "backend"],
        "level": "advanced",
        "file_url": "https://s3.aws.com/guide.pdf"
    }
    
    # Note: The client.post is synchronous, but the app handles async internally.
    response = await client.post(f"{settings.API_V1_STR}/learning/", json=resource_data, headers=auth_header)

    assert response.status_code == 201
    created_resource = response.json()
    assert created_resource["title"] == "Guía de Python Avanzado"
    # assert "_id" in created_resource # MongoDB ID returned as id usually in serialized models, let's check Pydantic behavior for Beanie. Beanie uses _id internally but might serialize to id.
    
    # Beanie documents serialize ID as 'id' by default in recent versions via Pydantic model dump.
    resource_id = created_resource.get("_id") or created_resource.get("id")
    assert resource_id

    # Retrieve list
    response = await client.get(f"{settings.API_V1_STR}/learning/")
    assert response.status_code == 200
    assert len(response.json()) >= 1
    
    # Retrieve single
    response = await client.get(f"{settings.API_V1_STR}/learning/{resource_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Guía de Python Avanzado"

