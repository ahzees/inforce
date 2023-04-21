FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /inforce
WORKDIR /inforce

ADD . /inforce/

RUN pip install poetry

COPY poetry.lock pyproject.toml /inforce/

RUN poetry config virtualenvs.create false
RUN poetry install
