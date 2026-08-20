FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY monitoring ./monitoring

RUN mkdir -p data/raw data/processed models

ENV PYTHONPATH=/app/src

COPY start.py /app/start.py

CMD ["python", "start.py"]


