FROM frolvlad/alpine-python3

WORKDIR /app
ADD requirements.txt /app


RUN apk add --no-cache mariadb-dev \
    build-base \
    python3-dev

RUN python3 -m pip install --upgrade pip
RUN pwd && ls
RUN pip3 install -r requirements.txt

ADD . /app/
