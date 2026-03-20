"""Opportunity ORM models."""

from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Column,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class OpportunityType(str, Enum):
    job = "job"
    event = "event"


class OpportunityFormat(str, Enum):
    online = "online"
    offline = "offline"
    hybrid = "hybrid"


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(SQLEnum(OpportunityType), nullable=False)
    format = Column(SQLEnum(OpportunityFormat), nullable=False)
    location = Column(String(255), nullable=True)
    start_at = Column(DateTime, nullable=True)
    end_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    employer_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    employer = relationship("Company", backref="opportunities")
    tags = relationship(
        "Tag",
        secondary="opportunity_tags",
        back_populates="opportunities",
    )
