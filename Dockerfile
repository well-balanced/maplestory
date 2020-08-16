FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /maplestory
WORKDIR /maplestory
ADD requirements.txt /maplestory/
RUN pip install — upgrade pip && pip install -r requirements.txt
ADD . /maplestory/