from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.core.database import get_db
from src.shared.models.user import User, UserRole, UserIdentity
from src.shared.utils.email import enviar_credenciales
from src.core.security import get_password_hash, generate_memorable_password
from pydantic import BaseModel, EmailStr
from typing import Optional

router = APIRouter()

@router.get("/leaderboard")
def get_leaderboard(limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).order_by(User.points.desc()).limit(limit).all()
    # Mask hashed passwords in response for security
    return [
        {
            "id": u.id,
            "username": u.username,
            "full_name": u.full_name,
            "points": u.points,
            "role": u.role,
            "email": u.email
        }
        for u in users
    ]

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    password: Optional[str] = None
    role: UserRole = UserRole.STUDENT
    identity: UserIdentity = UserIdentity.COMMUNITY

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    # Generate memorable password if none provided
    raw_password = user_in.password or generate_memorable_password()
    
    db_user = User(
        full_name=user_in.full_name,
        email=user_in.email,
        username=user_in.username,
        hashed_password=get_password_hash(raw_password),
        role=user_in.role,
        identity=user_in.identity,
        is_active=False if user_in.identity == UserIdentity.CORPORATE else True
    )
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El nombre de usuario o el correo ya están registrados"
        )
    db.refresh(db_user)
    
    # Send credentials email asynchronously/sequentially for now
    enviar_credenciales(
        email=db_user.email,
        username=db_user.username,
        password=raw_password,
        full_name=db_user.full_name
    )
    
    return db_user

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None

@router.patch("/{user_id}")
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if user_in.full_name:
        user.full_name = user_in.full_name
    if user_in.email:
        user.email = user_in.email
    
    db.commit()
    db.refresh(user)
    return user

@router.get("/pending")
def get_pending_users(db: Session = Depends(get_db)):
    # In a real app, verify that the requester is an ADMIN
    return db.query(User).filter(User.is_active == False).all()

@router.patch("/{user_id}/activate")
def activate_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    user.is_active = True
    db.commit()
    return {"message": f"Usuario {user.username} activado correctamente"}
