"""Tag ORM models."""

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.core.database import Base


opportunity_tags = Table(
    "opportunity_tags",
    Base.metadata,
    Column("opportunity_id", Integer, ForeignKey("opportunities.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    opportunities = relationship(
        "Opportunity",
        secondary=opportunity_tags,
        back_populates="tags",
    )
