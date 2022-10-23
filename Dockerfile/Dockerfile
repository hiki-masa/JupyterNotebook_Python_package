FROM python:3.10

RUN apt update && \
    apt install -y python3-pip
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install notebook

COPY ../Dockerfile/requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt
