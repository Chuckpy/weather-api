FROM python:3.9

# set work directory
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /src/requirements.txt

# install dependencies
# RUN set -eux \
#     && apk add --no-cache --virtual .build-deps build-base \
#     libressl-dev libffi-dev gcc musl-dev python3-dev \
#     postgresql-dev \
#     && pip install --upgrade pip setuptools wheel \
#     && pip install -r /usr/src/app/requirements.txt \
#     && rm -rf /root/.cache/pip

RUN set -eux
# RUN apk add --no-cache --virtual .build-deps build-base libressl-dev libffi-dev gcc musl-dev python3-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r /src/requirements.txt
RUN rm -rf /root/.cache/pip

# copy project
COPY . /src

RUN ls
CMD [ "python3", "main.py" ]