FROM ubuntu:14.04
EXPOSE 80
ADD app.py /tmp/app.py
RUN /bin/chmod 755 /tmp/app.py
RUN apt-get update
RUN apt-get install -y python python-flask
CMD ["/usr/bin/python", "/tmp/app.py"]
