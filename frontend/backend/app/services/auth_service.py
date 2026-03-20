"""Authentication business logic."""

from datetime import timedelta
from typing import Optional

from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.user import User
from app.schemas.auth import UserLogin, UserRegister


def register_user(db: Session, user_in: UserRegister) -> User:
    user = User(
        email=user_in.email,
        full_name=user_in.full_name,
        hashed_password=get_password_hash(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, user_in: UserLogin) -> Optional[User]:
    user = db.query(User).filter(User.email == user_in.email).first()
    if not user or not verify_password(user_in.password, user.hashed_password):
        return None
    return user


def create_tokens(user: User, expires_delta: Optional[timedelta] = None) -> dict:
    access_token = create_access_token({"sub": str(user.id)}, expires_delta=expires_delta)
    return {"access_token": access_token, "token_type": "bearer"}
