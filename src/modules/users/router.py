from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.shared.models.user import User, UserRole, UserIdentity
from src.core.security import get_password_hash
from pydantic import BaseModel, EmailStr

router = APIRouter()

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    username: str
    password: str
    role: UserRole = UserRole.STUDENT
    identity: UserIdentity = UserIdentity.COMMUNITY

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        full_name=user_in.full_name,
        email=user_in.email,
        username=user_in.username,
        hashed_password=get_password_hash(user_in.password),
        role=user_in.role,
        identity=user_in.identity
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
