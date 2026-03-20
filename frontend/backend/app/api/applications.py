"""Endpoints to manage applications (отклики)."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationResponse, ApplicationUpdate

router = APIRouter()


@router.post("/", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_application(
    payload: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> ApplicationResponse:
    application = Application(user_id=current_user.id, **payload.dict())
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@router.get("/", response_model=List[ApplicationResponse])
def list_applications(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> List[ApplicationResponse]:
    return db.query(Application).filter(Application.user_id == current_user.id).all()


@router.patch("/{application_id}", response_model=ApplicationResponse)
def update_application(
    application_id: int,
    payload: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> ApplicationResponse:
    application = db.get(Application, application_id)
    if not application or application.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(application, field, value)

    db.commit()
    db.refresh(application)
    return application
