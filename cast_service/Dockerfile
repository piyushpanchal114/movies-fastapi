FROM python:3.12.3-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip install pipenv --upgrade

COPY Pipfile Pipfile.lock /usr/src/app/

RUN pipenv install --deploy --system

COPY . .

EXPOSE 8000
