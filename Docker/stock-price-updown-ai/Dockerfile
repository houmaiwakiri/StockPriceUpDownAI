FROM python:3.8-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install requests beautifulsoup4 pandas yfinance

WORKDIR /app/stock-price-updown-ai

ENV PYTHONUNBUFFERED=1