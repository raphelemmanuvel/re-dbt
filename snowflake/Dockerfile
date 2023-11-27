FROM python:3.11.0-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip3 install poetry==1.5.1
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

ADD . /app/
