import requests
import pandas as pd
import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Configure TMDB_API_KEY no ambiente; boto3 usa a cadeia padrão de credenciais AWS.
import os

chave_api = os.environ["TMDB_API_KEY"]

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={chave_api}&language=pt-BR"

resposta = requests.get(url)

if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
else:
    print(f"Erro ao fazer requisição: {resposta.status_code}")

dados = resposta.json()

filmes = []

for filme in dados['results']:
    df = {
        'Título': filme['title'],
        'Data de Lançamento': filme['release_date'],
        'Visão Geral': filme['overview'],
        'Votos': filme['vote_count'],
        'Média de Votos': filme['vote_average']
    }
    filmes.append(df)

df_filmes = pd.DataFrame(filmes)

print(df_filmes)

try:
    cliente_s3 = boto3.client(
        's3',
        region_name='us-east-1'
    )

    nome_bucket = 'tmdb123'
    nome_arquivo = 'filmes_mais_bem_avaliados.csv'

    df_filmes.to_csv(nome_arquivo, index=False)

    cliente_s3.upload_file(nome_arquivo, nome_bucket, nome_arquivo)
    print(f"Arquivo {nome_arquivo} enviado para o bucket {nome_bucket} no S3.")

except NoCredentialsError:
    print("Erro: Nenhuma credencial foi fornecida ou as credenciais são inválidas.")
except PartialCredentialsError:
    print("Erro: Credenciais incompletas fornecidas.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
