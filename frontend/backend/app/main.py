from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Создаем экземпляр приложения
app = FastAPI(title="Tramplin API")

# 2. Настраиваем CORS (обязательно для работы с Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Позже заменим на конкретные порты 5173, 5174, 5175
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Базовый тестовый маршрут
@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "API Трамплин успешно запущен",
        "docs": "/docs"
    }

# В будущем здесь будет:
# from app.api.auth import router as auth_router
# app.include_router(auth_router)