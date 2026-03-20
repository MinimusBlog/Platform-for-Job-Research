"""Employer/company ORM models."""

from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Enum as SQLEnum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class VerificationStatus(str, Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    website = Column(String(255), nullable=True)
    verification_status = Column(SQLEnum(VerificationStatus), default=VerificationStatus.pending, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    owner = relationship("User", backref="companies")
