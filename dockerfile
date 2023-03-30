FROM nginx:mainline-alpine
ENV PYTHONUNBUFFERED 1
ENV PATH=/home/user/.local/bin:$PATH
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev python3 py3-pip py3-virtualenv \
    && ln -sf python3 /usr/bin/python
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY app /app
WORKDIR /app
RUN chmod +x docker-entrypoint.production.sh
RUN python -m venv .venv \
    && source .venv/bin/activate \
    && pip install django-bootstrap5 mysqlclient gunicorn django-redis \
    && deactivate \
    && apk del build-deps
CMD /app/docker-entrypoint.production.sh
