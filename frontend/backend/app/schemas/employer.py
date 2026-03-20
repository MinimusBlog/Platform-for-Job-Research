"""Pydantic schemas for employers/companies."""

from typing import Optional

from pydantic import BaseModel, HttpUrl


class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None
    website: Optional[HttpUrl] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    description: Optional[str] = None
    website: Optional[HttpUrl] = None


class CompanyResponse(CompanyBase):
    id: int
    verification_status: str

    class Config:
        orm_mode = True
