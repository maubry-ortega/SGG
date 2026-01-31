from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
import enum
from datetime import datetime, timezone

Base = declarative_base()

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    INSTRUCTOR = "instructor"
    STUDENT = "student"

class UserIdentity(str, enum.Enum):
    COMMUNITY = "community"
    CORPORATE = "corporate"

class Region(Base):
    __tablename__ = "regions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    users = relationship("User", back_populates="region")

class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.STUDENT)
    identity = Column(Enum(UserIdentity), default=UserIdentity.COMMUNITY)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=True)
    is_active = Column(Boolean, default=True)
    reputation = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), onupdate=lambda: datetime.now(timezone.utc))

    region = relationship("Region", back_populates="users")

    # Audit trail for the "Brain"
    audit_logs = relationship("AuditLog", back_populates="user")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)  # e.g., "login", "create_resource", "update_role"
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    ip_address = Column(String)

    user = relationship("User", back_populates="audit_logs")
