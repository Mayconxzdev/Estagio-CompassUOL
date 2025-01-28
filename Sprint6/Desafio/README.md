# Desafio de Ingestão de Dados para a RAW Zone no Amazon S3

## 1. Entendimento do Desafio

Este projeto tem como objetivo a ingestão de dados CSV para a RAW Zone no Amazon S3 usando Python e boto3. A estrutura do Data Lake inclui etapas de ingestão, armazenamento, processamento e consumo.

## 2. Planejamento da Primeira Entrega

### Implementação do Script Python

- Ler os arquivos CSV (`movies.csv` e `series.csv`) localmente.
- Fazer upload desses arquivos para o bucket S3 na estrutura especificada:
  /Raw/Local/Movies////movies.csv e /Raw/Local/Series////series.csv

- Utilizar a biblioteca boto3 para interagir com o S3.

### Criar um Container Docker

- Configurar o ambiente para executar o script Python.
- Criar um DockerFile que inclua todas as dependências necessárias.
- Executar o container localmente para testar a ingestão de arquivos para a RAW Zone do bucket S3.

## 3. Implementação do Script Python

O script deverá conter:

- Função para ler os arquivos CSV.
- Função para conectar ao bucket S3 e enviar os arquivos na estrutura definida.
- Registro de logs para monitorar o processo.

### Código do Script

```python
import boto3
import os
from datetime import datetime

aws_access_key_id= 'SEU_ACCESS_KEY_ID'
aws_secret_access_key= 'SEU_SECRET_ACCESS_KEY'
aws_session_token= 'SEU_SESSION_TOKEN'

def enviar_arquivo_para_s3(caminho_arquivo, nome_bucket):
  s3_client = boto3.client(
      's3',
      aws_access_key_id=aws_access_key_id,
      aws_secret_access_key=aws_secret_access_key,
      aws_session_token=aws_session_token,
      region_name='us-east-1'
  )
  hoje = datetime.today()
  ano, mes, dia = hoje.year, hoje.month, hoje.day
  caminho_s3 = f"Raw/Local/{os.path.basename(caminho_arquivo).split('.')[0].capitalize()}/{ano}/{mes}/{dia}/{os.path.basename(caminho_arquivo)}"

  try:
      s3_client.upload_file(caminho_arquivo, nome_bucket, caminho_s3)
      print(f"Arquivo {caminho_arquivo} enviado com sucesso para {caminho_s3}")
  except Exception as e:
      print(f"Erro ao enviar arquivo {caminho_arquivo}: {e}")

def principal():
  nome_bucket = 'desafio-6'
  arquivo_filmes = '/app/data/movies.csv'
  arquivo_series = '/app/data/series.csv'

  enviar_arquivo_para_s3(arquivo_filmes, nome_bucket)
  enviar_arquivo_para_s3(arquivo_series, nome_bucket)

if __name__ == "__main__":
  principal()
```

### Código do Dockerfile

```python
FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Instalação do boto3
RUN pip install --no-cache-dir boto3

CMD ["python", "upload_script.py"]
```

#### Minha construção de imagem Docker:

docker build -t desafio6 .

docker run --rm -v C:\Users... desafio6
