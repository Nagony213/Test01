FROM python:alpine
ENV PYTHONUNBUFFERED 1
ENV PATH=/home/user/.local/bin:$PATH
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN mkdir /app
WORKDIR /app
RUN adduser -D user
USER user
RUN pip install django-bootstrap5 mysqlclient gunicorn django-redis
USER root
RUN apk del build-deps
USER user
