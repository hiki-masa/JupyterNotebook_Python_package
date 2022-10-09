FROM python:3.10

RUN apt update && \
    apt install -y python3-pip

RUN pip install notebook

COPY ../Dockerfile/requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt