FROM python:3.7-alpine

# Instructs python not to buffer output
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# Dependency for postgresql support
RUN apk add --update postgresql-client
RUN apk add --update --virtual .tmp-postgres-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Delete the packages temporarily created for postgres
RUN apk del .tmp-postgres-build-deps

RUN mkdir /ams
WORKDIR /ams
COPY ./ams /ams


RUN adduser -D user
RUN chown -R user:user /ams
USER user