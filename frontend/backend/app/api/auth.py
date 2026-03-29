from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, Token, UserResponse
from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])

# Пока используем временное хранилище (заменить на DB позже)
fake_users_db = {}

@router.post("/register", response_model=UserResponse)
async def register(user_in: UserCreate):
    if user_in.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_dict = {
        "id": len(fake_users_db) + 1,
        "email": user_in.email,
        "role": user_in.role,
        "hashed_password": get_password_hash(user_in.password)
    }
    fake_users_db[user_in.email] = user_dict
    return user_dict

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    # Здесь должна быть проверка пароля через verify_password
    
    token = create_access_token({"sub": user["email"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer", "role": user["role"]}