"""User ORM models."""

from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime, Enum as SQLEnum, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Role(str, Enum):
    user = "user"
    employer = "employer"
    curator = "curator"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    role = Column(SQLEnum(Role), default=Role.user, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    contacts = relationship(
        "UserContact",
        foreign_keys="[UserContact.user_id]",
        back_populates="user",
        cascade="all, delete-orphan",
    )
