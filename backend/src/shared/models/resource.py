from datetime import datetime, timezone
from typing import List, Optional
from beanie import Document, Indexed
from pydantic import BaseModel, Field
import enum

class ResourceLevel(str, enum.Enum):
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class InteractionMetrics(BaseModel):
    views: int = 0
    downloads: int = 0
    likes: int = 0

class SaggiResource(Document):
    title: Indexed(str)
    description: str
    instructor_id: int  # Linked to SQL User ID
    tags: List[str] = []
    level: ResourceLevel = ResourceLevel.BASIC
    file_url: str
    is_public: bool = True
    metrics: InteractionMetrics = Field(default_factory=InteractionMetrics)
    version: int = 1
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Settings:
        name = "saggi_resources"

class Comment(Document):
    resource_id: Indexed(str)
    user_id: int
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


    class Settings:
        name = "saggi_comments"
