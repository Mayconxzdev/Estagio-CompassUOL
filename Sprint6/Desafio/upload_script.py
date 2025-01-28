import boto3
import os
from datetime import datetime

aws_access_key_id= 'ASIAUZPNLNO6ON2MO7F6'
aws_secret_access_key= 'chVFTzgSRY/WpwCuzwT7Ou1LFN5lDXq2eipG40q0'
aws_session_token= 'IQoJb3JpZ2luX2VjEP7//////////wEaCXVzLWVhc3QtMSJIMEYCIQDpwLIDmwnh/WLPYjCs9oNlh7TcuEFgaMaHU/XZUE5uewIhANwOFJ8KFFArW7gDZN1aZgwn/A4gsD4JeeJpzwL5hZq6KqwDCPf//////////wEQABoMMzI5NTk5NjQyNTU2IgyzIaSrtV+F4Ec6o1IqgANwDvpdN6UjB8vBYOHlbeBicFgy6ZMiUHAHRe1sjyTH7l5hvk4wjQOcB2UkGMvYJ0XRTFozr0aJCYQ2Mpgy5ib8kiAUVQIpKN7alG3iFki6kpQ3cMc9PZTPqtUF1j7YaEjzJXYklxAqQv+vp6/vFrkpybNH0dtcuXnFTT916W3RqDlYfP+oI47rEvNj0Y2FkLlW3xfjB6tWWtUXdrvm9z4fIZ0i48i5kSVhLYpA6UaEeTzEXF/gzA89Pw45BBL4ZP0k5YBVtnBT6f9n2fnbNZX27GJcO4ZqxnilIjDysRnucdsEHEOe89mcGwOOqKXFmeqLfBaaMRi7ACwbOsAkdokLtOLcNJjngAK9DIx05QCWSk8NwPbxYKraL/ypjOxILMV8BONtwAUMR3ri+7pDV17ayB55o1zziF9PYAcPN7TSPtGPGHV7kONBat3So+wiWnVVZp9Bp0YazsmjWo+71agMl3nUdeRA+tmhCmkhZlCZ+FULySgVlmYPfHfXZAhjC1UwiebKvAY6pQF7pAkUswPeC7CYREaHmcmmC7WWkWRD483FTR/1CIxc1TnS04GF6Ryww+d+KWwHv+hM2rfpd8YcBzRAFTKU9GsSvlPRGkCz/MiTCuDTjgHSRHnsCBfRb1l0ruH8M8c8DZuYAE3Y+Gdd5tMr8zs3pGeUV7VUlLrmkImLc0VxyU1kzaeOvXK0OuXTQ+LMH79HxtSgJ5Iu3uH5wQSx9gwuHZczIUsAzUo='



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
