"""Application ORM models."""

from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SQLEnum, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class ApplicationStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id"), nullable=False)
    status = Column(SQLEnum(ApplicationStatus), default=ApplicationStatus.pending, nullable=False)
    message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="applications")
    opportunity = relationship("Opportunity", backref="applications")
