FROM python:slim-bookworm

LABEL "maintainer"="gonzales@dopeldev.com"

USER root
RUN apt-get update && apt-get upgrade -y
WORKDIR /app
COPY about/ .
RUN pip install --root-user-action=ignore -r requirements.txt
EXPOSE 8181
CMD ["gunicorn", "app:app", "--bind", "127.0.0.1:8181", "--workers", "8"]
