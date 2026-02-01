import pytest
from src.core.config import settings

@pytest.mark.asyncio
async def test_create_and_retrieve_resource(client, auth_header):
    # Mock storage service to avoid real upload
    from unittest.mock import AsyncMock, patch
    from src.modules.learning import router
    
    # We patch the instance imported in the router
    with patch("src.modules.learning.router.storage_service.upload_file", new_callable=AsyncMock) as mock_upload:
        mock_upload.return_value = "https://s3.aws.com/fake-guide.pdf"
        
        resource_data = {
            "title": "Guía de Python Avanzado",
            "description": "Domina las estructuras de datos.",
            "instructor_id": "1", # Form data sends strings
            "level": "advanced",
             # Tags handling in simple form data usually requires repeated keys or special parsing. 
             # FastAPI default List[str] form expects same key multiple times.
             # Client usage: data={"tags": ["python", "backend"]} handles it or distinct tuples.
        }
        
        # Tags need to be passed carefully in httpx for list
        # httpx handles list values in data dict by sending multiple fields with same name
        form_data = {
           "title": "Guía de Python Avanzado",
           "description": "Domina las estructuras de datos.",
           "instructor_id": "1", 
           "level": "advanced",
           "tags": ["python", "backend"] 
        }

        # Fake file
        files = {"file": ("guide.pdf", b"%PDF-1.4 content", "application/pdf")}
        
        # Note: The client.post is synchronous, but the app handles async internally.
        response = await client.post(f"{settings.API_V1_STR}/learning/", data=form_data, files=files, headers=auth_header)
        
        assert response.status_code == 201
        created_resource = response.json()
        assert created_resource["title"] == "Guía de Python Avanzado"
        assert created_resource["file_url"] == "https://s3.aws.com/fake-guide.pdf"
        
        # Check mock usage
        mock_upload.assert_called_once()
    
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


