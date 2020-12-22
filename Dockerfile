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

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
# RUN python manage.py runserver