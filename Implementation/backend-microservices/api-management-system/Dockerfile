FROM python:3.7-alpine

# Instructs python not to buffer output
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /ams
WORKDIR /ams
COPY ./ams /ams


RUN adduser -D user
RUN chown -R user:user /ams
USER user