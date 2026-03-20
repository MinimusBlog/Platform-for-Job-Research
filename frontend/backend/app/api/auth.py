"""Authentication endpoints."""

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.user import User
from app.schemas.auth import Token, UserLogin, UserRegister, UserOut
from app.services.auth_service import authenticate_user, create_tokens, register_user

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserRegister, db: Session = Depends(get_db)) -> UserOut:
    existing = db.query(User).filter(User.email == user_in.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = register_user(db, user_in)
    return user


@router.post("/login", response_model=Token)
def login(user_in: UserLogin, db: Session = Depends(get_db)) -> Token:
    user = authenticate_user(db, user_in)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return create_tokens(user)


@router.post("/refresh", response_model=Token)
def refresh(token: str):
    # TODO: implement refresh token logic (store/validate refresh tokens)
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Refresh token not implemented yet")
