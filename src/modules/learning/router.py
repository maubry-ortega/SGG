from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from src.shared.models.resource import SaggiResource, ResourceLevel
from pydantic import BaseModel

router = APIRouter()

class ResourceCreate(BaseModel):
    title: str
    description: str
    instructor_id: int
    tags: List[str] = []
    level: ResourceLevel = ResourceLevel.BASIC
    file_url: str

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_resource(resource_in: ResourceCreate):
    resource = SaggiResource(**resource_in.model_dump())
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
