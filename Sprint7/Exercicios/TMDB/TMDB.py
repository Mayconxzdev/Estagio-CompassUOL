import requests
import pandas as pd
import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Carregar credenciais da AWS de um arquivo JSON
with open('aws_credenciais.json', 'r') as arquivo_credenciais:
    credenciais = json.load(arquivo_credenciais)

chave_acesso_aws = credenciais['aws_access_key_id']
chave_secreta_aws = credenciais['aws_secret_access_key']
token_sessao_aws = credenciais.get('aws_session_token')  # Pode ser opcional

chave_api = "b19482533361f027dec14391eb35d74d"

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
        aws_access_key_id=chave_acesso_aws,
        aws_secret_access_key=chave_secreta_aws,
        aws_session_token=token_sessao_aws,
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
