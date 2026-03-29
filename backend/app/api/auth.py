from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import UserCreate, Token
from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

# Временное хранилище
temp_users_db = {}

@router.post("/register", status_code=201)
async def register(user_data: UserCreate):
    if user_data.email in temp_users_db:
        raise HTTPException(status_code=400, detail="Пользователь с таким Email уже есть")
    
    hashed_password = get_password_hash(user_data.password)
    temp_users_db[user_data.email] = {
        "email": user_data.email,
        "password": hashed_password,
        "role": user_data.role
    }
    return {"message": "Регистрация успешна"}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = temp_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный Email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user["email"], "role": user["role"]})
    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "role": user["role"]
    }