FROM ubuntu:latest
LABEL authors="kyleschang"

ENTRYPOINT ["top", "-b"]

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install uv && uv pip install -r requirements.txt

COPY app/ app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]