FROM python:3.9

WORKDIR /app

COPY ./python/ /app

CMD ["python", "test.py"]
