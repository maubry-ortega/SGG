from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from typing import List
from src.shared.models.resource import SaggiResource, ResourceLevel
from src.shared.utils.storage import storage_service
from pydantic import BaseModel, Json

router = APIRouter()

# Wrapper model not used directly in Form, but kept for reference or structured updates later
class ResourceCreate(BaseModel):
    title: str
    description: str
    instructor_id: int
    tags: List[str] = []
    level: ResourceLevel = ResourceLevel.BASIC

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_resource(
    title: str = Form(...),
    description: str = Form(...),
    instructor_id: int = Form(...),
    level: ResourceLevel = Form(ResourceLevel.BASIC),
    tags: List[str] = Form([]), # Requires special handling for lists in Form usually, or Json string
    file: UploadFile = File(...)
):
    # handling list form data can be tricky/loose in FastAPI depending on client. 
    # For now assuming simple list or comma separated if we parse, but let's stick to standard internal parsing if needed. 
    # Or just use the model_validate_json if sending complex data as json string part.
    
    # 1. Upload File
    file_url = await storage_service.upload_file(file)
    
    # 2. Create Resource
    resource = SaggiResource(
        title=title,
        description=description,
        instructor_id=instructor_id,
        level=level,
        tags=tags,
        file_url=file_url
    )
    await resource.insert()
    return resource



@router.get("/")
async def list_resources():
    return await SaggiResource.find_all().to_list()

@router.get("/{id}")
async def get_resource(id: str):
    resource = await SaggiResource.get(id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource
