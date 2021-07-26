FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /var/code

COPY . .