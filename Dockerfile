# Base image — official Python 3.12 slim (lightweight)
FROM python:3.12-slim

# Install Chrome and dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable so Selenium knows where Chrome is
ENV CHROME_BIN=/usr/bin/chromium

# Set working directory inside container
WORKDIR /app

# Copy and install dependencies first (Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Run all tests and generate HTML report
CMD ["pytest", "tests/", "-v", "--html=reports/report.html", "--self-contained-html"]