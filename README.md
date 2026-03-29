# 🚀 Трамплин — Карьерная платформа для IT-студентов
> Экосистема, где студенты не просто
ищут работу, а строят карьеру с нуля: находят менторов, участвуют в карьерных мероприятиях
компаний и получают предложения о стажировках, основываясь на своих навыках и активности.

---

## 🛠 Требования
Для работы с проектом вам понадобятся:
* **Docker** и **Docker Compose** (рекомендуемый способ для быстрого старта)
* **Node.js** (v18+) и **Python** (3.10+) — если планируете запускать сервисы вручную.

---

## 🛠 Технологический стек

### Frontend
| Технология | Версия | Назначение |
|------------|--------|------------|
| Vue.js | 3.x | Основной фреймворк |
| Pinia | 2.x | Управление состоянием |
| Vue Router | 4.x | Маршрутизация |
| Vite | 5.x | Сборка проекта |
| Axios | 1.x | HTTP-запросы |
| TailwindCSS | 3.x | Стилизация |

### Backend
| Технология | Версия | Назначение |
|------------|--------|------------|
| FastAPI | 0.110+ | Web-фреймворк |
| SQLAlchemy | 2.x | ORM |
| Pydantic | 2.6+ | Валидация данных |
| Python-JOSE | 3.3+ | JWT-токены |
| Passlib | 1.7+ | Хэширование паролей |
| Uvicorn | 0.29+ | ASGI-сервер |

### База данных
| Технология | Версия | Назначение |
|------------|--------|------------|
| SQLite | 3.x | Разработка (по умолчанию) |
| PostgreSQL | 15+ | Продакшн (опционально) |
| AsyncPG | 0.29+ | Асинхронный драйвер |

---

## 🐳 Быстрый старт через Docker (Рекомендуется)

Самый простой способ поднять всю экосистему (Frontend, Backend, Database) одной командой:

### 1. Клонировать репозиторий
```bash
git clone [https://github.com/MinimusBlog/Platform-for-Job-Research.git](https://github.com/MinimusBlog/Platform-for-Job-Research.git)
cd Platform-for-Job-Research
```

# 2. Запуск всех сервисов
``` bash
docker compose up --build
```
### 3. Доступ к проекту
 - Frontend: http://localhost:5173

 - Backend API: http://localhost:8000

 - Swagger (Документация API): http://localhost:8000/docs
 
---
## Локальный запуск

### 1. Установка общих зависимостей
``` bash
npm install
npm run install:all
```

### 2. Запуск backend
# MacOS/Linux
```bash
source .venv/bin/activate
```

# Windows
``` bash
.venv\Scripts\activate.bat
```
``` bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 3. Запуск frontend
```bash
cd frontend
npm run dev
```