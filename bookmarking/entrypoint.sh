#!/bin/bash

sleep 10

python manage.py migrate

python manage.py collectstatic --noinput

exec gunicorn bookmarking.wsgi:application --bind 0.0.0.0:8000
