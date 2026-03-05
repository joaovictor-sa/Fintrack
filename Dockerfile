FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

EXPOSE 8000

# Roda migrate + create_demo_user antes de subir o servidor
CMD sh -c "python manage.py migrate && python manage.py create_demo_user && gunicorn app.wsgi:application --bind 0.0.0.0:8000"
