FROM nginx

RUN head -n3 /etc/apt/sources.list > /tmp/sources.list.tmp && cat /tmp/sources.list.tmp > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y wget apt-utils
RUN wget http://nginx.org/keys/nginx_signing.key -O - | apt-key add - 
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y python nginx-nr-agent
