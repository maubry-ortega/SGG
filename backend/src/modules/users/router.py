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
        identity=user_in.identity
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
            "role": u.role
        }
        for u in users
    ]
