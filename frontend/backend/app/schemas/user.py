"""Pydantic schemas for user profiles."""

from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
