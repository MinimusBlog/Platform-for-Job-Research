"""Pydantic schemas for applications."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ApplicationStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"


class ApplicationBase(BaseModel):
    opportunity_id: int
    message: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    status: Optional[ApplicationStatus] = None


class ApplicationResponse(ApplicationBase):
    id: int
    user_id: int
    status: ApplicationStatus
    created_at: datetime

    class Config:
        orm_mode = True
