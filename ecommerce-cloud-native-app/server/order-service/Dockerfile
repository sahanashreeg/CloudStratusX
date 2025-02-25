# Use an official Python runtime as a parent image
# Dockerfile for product-service, order-service, and user-service
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
