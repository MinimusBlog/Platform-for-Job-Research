from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router 

app = FastAPI(title="Tramplin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.core.database import engine, Base

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # создание таблицы users и другие при старте
        await conn.run_sync(Base.metadata.create_all)

# Подключаем роутер авторизации
app.include_router(auth_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API Трамплин работает"}