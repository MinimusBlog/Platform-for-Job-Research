"""Moderation and verification endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.employer import Company, VerificationStatus
from app.schemas.employer import CompanyResponse

router = APIRouter()


@router.get("/companies", response_model=List[CompanyResponse])
def list_companies_for_moderation(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    # TODO: check curator/admin role
    return db.query(Company).filter(Company.verification_status == VerificationStatus.pending).all()


@router.post("/companies/{company_id}/verify", response_model=CompanyResponse)
def verify_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    company = db.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    company.verification_status = VerificationStatus.verified
    db.commit()
    db.refresh(company)
    return company


@router.post("/companies/{company_id}/reject", response_model=CompanyResponse)
def reject_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    company = db.get(Company, company_id)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    company.verification_status = VerificationStatus.rejected
    db.commit()
    db.refresh(company)
    return company
