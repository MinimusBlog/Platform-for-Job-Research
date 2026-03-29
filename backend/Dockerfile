FROM python:3.11-slim

# Установка рабочих директорий
WORKDIR /app

# Установка зависимостей для корректной сборки psycopg и других библиотек
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir email-validator

# Копируем весь код бэкенда
COPY . .

# Команда для запуска (учитываем, что main.py в папке app)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]