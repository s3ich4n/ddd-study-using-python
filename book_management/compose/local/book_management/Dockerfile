#
# book_management 앱의 Dockerfile
#   1. poetry 설치
#   2. 의존성 관련 설치
#   3. 앱 설치
#
# @author      Seongeun Yu (s3ich4n@gmail.com)
# @date        2023/04/07 14:00 created.
# @license     Please refer to the LICENSE file on a root directory of project.
#


ARG PYTHON_VERSION=3.8-slim-buster

### ### ### ### ### ### ###
# STAGE 0. Prerequisites  #
### ### ### ### ### ### ###
FROM python:${PYTHON_VERSION} as python

FROM python as poetry-prerequisites-stage

LABEL maintainer="s3ich4n <s3ich4n@gmail.com>"
LABEL description="Heavily inspired by max-pfeiffer python-poetry"
LABEL version="0.1.0"

ENV APP_NAME=book_management

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=${POETRY_VERSION} \
    POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

# https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        build-essential \
        # psycopg2 dependencies
        libpq-dev \
        # poetry install
        curl \
        # Translations dependencies
        gettext \
    && curl -sSL https://install.python-poetry.org | python -

### ### ### ### ###
# STAGE 1. build  #
### ### ### ### ###
FROM poetry-prerequisites-stage as python-build-stage

ENV PYTHONUNBUFFERED=1 \
    # https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
    PYTHONDONTWRITEBYTECODE=1 \
    # https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
    PYTHONPATH=/${APP_NAME} \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # https://python-poetry.org/docs/configuration/#virtualenvsin-project
    POETRY_CACHE_DIR=/${APP_NAME}/.cache \
    VIRTUAL_ENVIRONMENT_PATH=/${APP_NAME}/.venv \
    APPLICATION_SERVER_PORT=$APPLICATION_SERVER_PORT \
    POETRY_VERSION=1.4.1

# Adding the virtual environment to PATH in order to "activate" it.
# https://docs.python.org/3/library/venv.html#how-venvs-work
ENV PATH="$VIRTUAL_ENVIRONMENT_PATH/bin:$PATH"

### ### ### ### ###
# STAGE 2. 'run'  #
### ### ### ### ###
FROM python-build-stage as python-run-stage

# Set the WORKDIR to the application root.
# https://www.uvicorn.org/settings/#development
# https://docs.docker.com/engine/reference/builder/#workdir
WORKDIR ${PYTHONPATH}
COPY . ${PYTHONPATH}

# Create cache directory and set permissions because user 1001 has no home
# and poetry cache directory.
# https://python-poetry.org/docs/configuration/#cache-directory
RUN mkdir ${POETRY_CACHE_DIR}

# install dependencies via Poetry
RUN poetry install

RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY ./compose/local/book_management/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/book_management/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

ENTRYPOINT ["/entrypoint"]
