"""User contact (friendship) ORM models."""

from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class UserContact(Base):
    __tablename__ = "user_contacts"
    __table_args__ = (UniqueConstraint("user_id", "contact_id", name="uq_user_contact"),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    contact_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(50), default="pending", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", foreign_keys=[user_id], back_populates="contacts")
    contact = relationship("User", foreign_keys=[contact_id])
