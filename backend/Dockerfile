FROM python:3.8.2-slim-buster

ARG uid
ARG gid
ARG user=iamrobot
ARG group=iamrobot

RUN groupadd -o -g $gid $group && useradd -o -g $gid -u $uid $user && \
    mkdir -p /home/$user && chown -R $user:$group /home/$user && \
    mkdir -p /code && chown -R $user:$group /code 

RUN apt-get update && apt-get install -y make yaz \
    && pip install uvicorn fastapi

WORKDIR /code

EXPOSE 8000
