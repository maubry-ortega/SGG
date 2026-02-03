from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.core.security import create_access_token, create_refresh_token, verify_password, get_password_hash
from src.shared.models.user import User
from pydantic import BaseModel, EmailStr

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Tu cuenta está pendiente de activación por un administrador corporativo."
        )
    
    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
        "token_type": "bearer",
        "user": {
            "id": user.id, 
            "username": user.username, 
            "role": user.role,
            "points": user.points,
            "completed_guides_count": user.completed_guides_count,
            "saved_resources_count": user.saved_resources_count
        }
    }
    
class ChangePasswordRequest(BaseModel):
    user_id: int
    current_password: str
    new_password: str

@router.post("/change-password")
def change_password(data: ChangePasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user or not verify_password(data.current_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Contraseña actual incorrecta")
    
    user.hashed_password = get_password_hash(data.new_password)
    db.commit()
    return {"message": "Contraseña actualizada con éxito"}
