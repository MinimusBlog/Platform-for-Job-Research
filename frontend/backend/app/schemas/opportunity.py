"""Pydantic schemas for opportunities."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OpportunityType(str, Enum):
    job = "job"
    event = "event"


class OpportunityFormat(str, Enum):
    online = "online"
    offline = "offline"
    hybrid = "hybrid"


class OpportunityBase(BaseModel):
    title: str
    description: Optional[str] = None
    type: OpportunityType
    format: OpportunityFormat
    location: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None


class OpportunityCreate(OpportunityBase):
    employer_id: int


class OpportunityUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None


class OpportunityResponse(OpportunityBase):
    id: int

    class Config:
        orm_mode = True
