import boto3
import os
from datetime import datetime

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")



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
