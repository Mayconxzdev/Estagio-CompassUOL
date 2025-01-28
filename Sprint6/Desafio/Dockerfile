FROM python:3.9-slim

WORKDIR /app

COPY . /app

#instalação boto3
RUN pip install --no-cache-dir boto3

CMD ["python", "upload_script.py"]