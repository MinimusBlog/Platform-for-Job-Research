"""Pydantic schemas for tags."""

from typing import Optional

from pydantic import BaseModel


class TagBase(BaseModel):
    name: str
    description: Optional[str] = None


class TagCreate(TagBase):
    pass


class TagResponse(TagBase):
    id: int

    class Config:
        orm_mode = True
