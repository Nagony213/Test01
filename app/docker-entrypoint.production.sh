#!/bin/sh

sh -c /usr/sbin/nginx

source .venv/bin/activate

# Migrate Database2
python3 manage.py makemigrations --noinput

# Migrate Database
python3 manage.py migrate --noinput

# Run Gunicorn (WSGI Server)
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
