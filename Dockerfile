FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY agent/ ./agent/
COPY backend/ ./backend/
COPY frontend/ ./frontend/

EXPOSE 5000

CMD ["python", "backend/app.py"]
