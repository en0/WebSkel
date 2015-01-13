FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y python python-flask pip
RUN pip install flask-RESTful

VOLUME /srv/http

