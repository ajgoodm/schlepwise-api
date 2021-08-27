FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /var/code

COPY . .

RUN pip install -r requirements.txt
RUN export $(xargs < .env)
