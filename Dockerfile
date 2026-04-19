FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install firefox && \
    playwright install-deps firefox

COPY . .

RUN mkdir -p allure-results

CMD ["pytest", "--alluredir=allure-results", "-v"]