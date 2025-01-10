import boto3
import json

def carregar_credenciais():
    with open('credenciais.json', 'r') as file:
        return json.load(file)

def criar_bucket(nome_bucket, regiao):
    credenciais = carregar_credenciais()
    s3 = boto3.client(
        's3',
        aws_access_key_id=credenciais['AccessKeyId'],
        aws_secret_access_key=credenciais['SecretAccessKey'],
        aws_session_token=credenciais['SessionToken'],
        region_name=regiao
    )

    if regiao == 'us-east-1':
        s3.create_bucket(Bucket=nome_bucket)
    else:
        s3.create_bucket(
            Bucket=nome_bucket,
            CreateBucketConfiguration={'LocationConstraint': regiao}
        )
    print(f"Bucket '{nome_bucket}' criado com sucesso na região '{regiao}'!")

def upload_arquivo(file_name, bucket_name):
    credenciais = carregar_credenciais()
    s3 = boto3.client(
        's3',
        aws_access_key_id=credenciais['AccessKeyId'],
        aws_secret_access_key=credenciais['SecretAccessKey'],
        aws_session_token=credenciais['SessionToken']
    )
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Arquivo '{file_name}' enviado para o bucket '{bucket_name}' com sucesso.")

if __name__ == "__main__":
    regiao = "sa-east-1"
    nome_bucket = "desafio-1234"

    criar_bucket(nome_bucket, regiao)

    upload_arquivo("arquivo_original.csv", nome_bucket)
