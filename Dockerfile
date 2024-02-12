FROM python:3.10

COPY ./app /app

RUN pip install -r app/requirements.txt

WORKDIR /app