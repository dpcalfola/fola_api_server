FROM python:3.11.0rc2-alpine3.16

MAINTAINER FolaFlor
LABEL maintainer="https://dpcalfola.tistory.com/"

ENV PYTHONUNBUFFRED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./Django_app /Django_app
WORKDIR /Django_app
EXPOSE 48007

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        Django-user

ENV PATH="/py/bin:$PATH"

USER Django-user
