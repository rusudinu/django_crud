FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py makemigrations

RUN python manage.py migrate --run-syncdb

EXPOSE 8000

# ENTRYPOINT export DJANGO_DEBUG=False
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT gunicorn --workers=8 --threads=2 -b 0.0.0.0:8000 django_crud.wsgi
# RUN python manage.py runserver