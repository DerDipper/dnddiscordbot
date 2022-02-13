# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY token token
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
