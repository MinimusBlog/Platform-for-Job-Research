"""Pydantic schemas for authentication flows."""

from datetime import datetime

from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: int | None = None
    exp: int | None = None


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None
    is_active: bool

    class Config:
        orm_mode = True
