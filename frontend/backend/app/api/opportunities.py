"""CRUD endpoints for opportunities."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate, OpportunityResponse, OpportunityUpdate

router = APIRouter()


@router.post("/", response_model=OpportunityResponse, status_code=status.HTTP_201_CREATED)
def create_opportunity(
    payload: OpportunityCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> OpportunityResponse:
    # TODO: check permissions (employer role)
    opportunity = Opportunity(**payload.dict())
    db.add(opportunity)
    db.commit()
    db.refresh(opportunity)
    return opportunity


@router.get("/", response_model=List[OpportunityResponse])
def list_opportunities(db: Session = Depends(get_db)) -> List[OpportunityResponse]:
    return db.query(Opportunity).all()


@router.get("/{opportunity_id}", response_model=OpportunityResponse)
def get_opportunity(opportunity_id: int, db: Session = Depends(get_db)) -> OpportunityResponse:
    opportunity = db.get(Opportunity, opportunity_id)
    if not opportunity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opportunity not found")
    return opportunity


@router.patch("/{opportunity_id}", response_model=OpportunityResponse)
def update_opportunity(
    opportunity_id: int,
    payload: OpportunityUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> OpportunityResponse:
    opportunity = db.get(Opportunity, opportunity_id)
    if not opportunity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opportunity not found")
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(opportunity, field, value)
    db.commit()
    db.refresh(opportunity)
    return opportunity


@router.delete("/{opportunity_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_opportunity(
    opportunity_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> None:
    opportunity = db.get(Opportunity, opportunity_id)
    if not opportunity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Opportunity not found")
    db.delete(opportunity)
    db.commit()
