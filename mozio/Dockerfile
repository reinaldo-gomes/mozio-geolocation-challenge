# syntax=docker/dockerfile:1
FROM python:3.10.5-slim-buster
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pwd
COPY . .
EXPOSE 8000
STOPSIGNAL SIGINT
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]