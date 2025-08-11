FROM python:3.11.9-bookworm

ENV PYTHONUNBUFFERED=1

# Install dependencies required for psycopg2
RUN apt-get update && \
    apt-get install -y \
        gcc \
        python3-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt
COPY . /app

WORKDIR /app

ARG DEV=false

# Install Python dependencies from requirements.txt
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt  && \
    if [ $DEV = "true" ]; \
      then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"