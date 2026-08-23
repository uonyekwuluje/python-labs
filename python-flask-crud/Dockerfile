FROM python:3.12-slim

# Prevent Python from creating .pyc files
# and enable unbuffered logging.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies first for better Docker layer caching.
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application.
COPY app.py .
COPY templates ./templates
COPY static ./static

# Flask/Gunicorn listens here.
EXPOSE 5000

# Run database initialization before starting Gunicorn.
CMD ["sh", "-c", "flask --app app init-db && gunicorn --bind 0.0.0.0:5000 --workers 2 --threads 4 app:app"]
