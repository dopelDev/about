FROM python:slim-bookworm

LABEL "maintainer"="gonzales@dopeldev.com"

USER root
RUN apt-get update && apt-get upgrade -y
WORKDIR /app
COPY about/ .
RUN pip install -r requirements.txt
EXPOSE 8181
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8181", "--workers", "3"]
