#FROM python:3.11.0rc2-alpine3.16
FROM python:3.10.10-alpine3.17

MAINTAINER FolaFlor
LABEL maintainer="https://dpcalfola.tistory.com/"

ENV PYTHONUNBUFFRED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./Django_app /Django_app
WORKDIR /Django_app
EXPOSE 48007

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Installation psycopg2 dependency applications
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    # --use-pep517 option is for psycopg2 \
    # https://github.com/pypa/pip/issues/8559
    /py/bin/pip install -r /tmp/requirements.txt --use-pep517 && \
    # Install dev packages if ARG DEV is true
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # Remove temp dir
    rm -rf /tmp && \
    # Container user setting
    adduser \
        --disabled-password \
        --no-create-home \
        Django-user

ENV PATH="/py/bin:$PATH"

USER Django-user
