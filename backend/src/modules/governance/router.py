from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.shared.models.user import Region, Program
from pydantic import BaseModel

router = APIRouter()

class NameSchema(BaseModel):
    name: str

@router.post("/regions", status_code=status.HTTP_201_CREATED)
def create_region(data: NameSchema, db: Session = Depends(get_db)):
    region = Region(name=data.name)
    db.add(region)
    db.commit()
    db.refresh(region)
    return region

@router.get("/regions")
def get_regions(db: Session = Depends(get_db)):
    return db.query(Region).all()

@router.post("/programs", status_code=status.HTTP_201_CREATED)
def create_program(data: NameSchema, db: Session = Depends(get_db)):
    program = Program(name=data.name)
    db.add(program)
    db.commit()
    db.refresh(program)
    return program

@router.get("/programs")
def get_programs(db: Session = Depends(get_db)):
    return db.query(Program).all()
