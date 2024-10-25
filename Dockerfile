FROM python:3-bullseye

LABEL "maintainer"="dopel@dopeldev.com"

USER root
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        build-essential \
        python3-dev \
        libffi-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
WORKDIR /app
COPY about/ .
RUN pip install -r requirements.txt
EXPOSE 8181
CMD ["gunicorn", "app:app", "--bind", "127.0.0.1:8181", "--workers", "8"]
