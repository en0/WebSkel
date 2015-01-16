FROM ubuntu:14.04


RUN apt-get --fix-missing update
RUN apt-get install -y supervisor python python-flask python-pip
RUN pip install flask-RESTful

VOLUME /srv/http

ADD http/ /srv/http
ADD python-flask.conf /etc/supervisor/conf.d/

CMD supervisord -n
