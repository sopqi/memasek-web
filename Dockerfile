FROM python:3.10-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV SECRET_KEY="dummy_key_for_build"
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "memasek.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--worker-class", "gthread", "--threads", "20"]