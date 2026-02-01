import os
import shutil
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status, Depends
from src.shared.models.resource import SaggiResource, ResourceLevel
from src.shared.models.user import User
from src.core.database import get_db
from sqlalchemy.orm import Session
from beanie import PydanticObjectId
from datetime import datetime, timezone

router = APIRouter()

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_pdf(
    title: str = Form(...),
    description: str = Form(...),
    level: ResourceLevel = Form(ResourceLevel.BASIC),
    tags: str = Form(""),
    uploader_id: int = Form(0),
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF.")

    file_path = os.path.join(UPLOAD_DIR, f"{datetime.now().timestamp()}_{file.filename}")
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resource = SaggiResource(
        title=title,
        description=description,
        level=level,
        tags=tags.split(",") if tags else [],
        file_url=file_path,
        uploader_id=uploader_id,
        is_approved=False
    )
    
    await resource.insert()
    return {"message": "PDF subido con éxito. Pendiente de aprobación por un administrador.", "id": str(resource.id)}

@router.get("/", response_model=List[SaggiResource])
async def get_public_resources():
    return await SaggiResource.find(SaggiResource.is_approved == True).to_list()

@router.get("/pending", response_model=List[SaggiResource])
async def get_pending_resources():
    # In a real app, only Admins could call this
    return await SaggiResource.find(SaggiResource.is_approved == False).to_list()

@router.patch("/{id}/approve")
async def approve_resource(id: str, db: Session = Depends(get_db)):
    resource = await SaggiResource.get(id)
    if not resource:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    
    resource.is_approved = True
    resource.updated_at = datetime.now(timezone.utc)
    await resource.save()

    # Award points to the uploader
    if resource.uploader_id > 0:
        uploader = db.query(User).filter(User.id == resource.uploader_id).first()
        if uploader:
            uploader.points += 50
            db.commit()
    
    return {"message": "Recurso aprobado y ahora es público (+50 puntos para el autor)", "id": str(resource.id)}

@router.delete("/{id}")
async def delete_resource(id: str):
    resource = await SaggiResource.get(id)
    if not resource:
        raise HTTPException(status_code=404, detail="Recurso no encontrado")
    
    # Optional: Delete actual file
    if os.path.exists(resource.file_url):
        os.remove(resource.file_url)
        
    await resource.delete()
    return {"message": "Recurso eliminado"}
