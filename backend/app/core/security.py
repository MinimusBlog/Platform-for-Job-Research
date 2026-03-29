import bcrypt
import hashlib
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt

# Конфигурация
SECRET_KEY = "TRAMPLIN_SUPER_SECRET_KEY_2024" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440 

def _get_prehash(password: str) -> bytes:
    """
    Хэшируем пароль в SHA-256 и возвращаем байты.
    Это гарантирует длину в 64 символа.
    """
    digest = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return digest.encode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        prehashed = _get_prehash(plain_password)
        return bcrypt.checkpw(prehashed, hashed_password.encode("utf-8"))
    except Exception:
        return False

def get_password_hash(password: str) -> str:
    """
    Создает безопасный хэш пароля.
    """
    prehashed = _get_prehash(password)
    # Генерируем соль и хэшируем
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(prehashed, salt)
    return hashed.decode("utf-8")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)