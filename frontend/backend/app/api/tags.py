"""Tag management endpoints."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagResponse, TagBase

router = APIRouter()


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
def create_tag(payload: TagCreate, db: Session = Depends(get_db)) -> TagResponse:
    tag = Tag(**payload.dict())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.get("/", response_model=List[TagResponse])
def list_tags(db: Session = Depends(get_db)) -> List[TagResponse]:
    return db.query(Tag).all()


@router.get("/{tag_id}", response_model=TagResponse)
def get_tag(tag_id: int, db: Session = Depends(get_db)) -> TagResponse:
    tag = db.get(Tag, tag_id)
    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return tag


@router.patch("/{tag_id}", response_model=TagResponse)
def update_tag(tag_id: int, payload: TagBase, db: Session = Depends(get_db)) -> TagResponse:
    tag = db.get(Tag, tag_id)
    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(tag, field, value)
    db.commit()
    db.refresh(tag)
    return tag


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(tag_id: int, db: Session = Depends(get_db)) -> None:
    tag = db.get(Tag, tag_id)
    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    db.delete(tag)
    db.commit()
