import pandas as pd
import boto3
import json

def carregar_credenciais():
    with open('credenciais.json', 'r') as file:
        return json.load(file)

def baixar_arquivo_s3(bucket_name, file_name, local_path):
    credenciais = carregar_credenciais()
    s3 = boto3.client(
        's3',
        aws_access_key_id=credenciais['AccessKeyId'],
        aws_secret_access_key=credenciais['SecretAccessKey'],
        aws_session_token=credenciais['SessionToken']
    )
    s3.download_file(bucket_name, file_name, local_path)
    print(f"Arquivo '{file_name}' baixado do bucket '{bucket_name}' para '{local_path}'.")

def processar_e_upload(bucket_name, input_file_name, output_file_name):

    local_file_path = 'temp_' + input_file_name

    baixar_arquivo_s3(bucket_name, input_file_name, local_file_path)

    df = pd.read_csv(local_file_path, delimiter=';')

    df['idade_grupo'] = df['nu_idade'].apply(lambda x: 'Acima de 50' if x > 50 else '50 ou menos')
    df['dt_nascimento'] = pd.to_datetime(df['dt_nascimento'], format='%d/%m/%Y')
    df['ano_nascimento'] = df['dt_nascimento'].dt.year
    df['sg_sexo_upper'] = df['sg_sexo'].str.upper()

    manipulated_local_file_path = 'temp_' + output_file_name
    df.to_csv(manipulated_local_file_path, index=False, sep=';', lineterminator='\r\n', encoding='utf-8-sig')

    credenciais = carregar_credenciais()
    s3 = boto3.client(
        's3',
        aws_access_key_id=credenciais['AccessKeyId'],
        aws_secret_access_key=credenciais['SecretAccessKey'],
        aws_session_token=credenciais['SessionToken']
    )

    s3.upload_file(manipulated_local_file_path, bucket_name, output_file_name)
    print(f"O arquivo manipulado '{output_file_name}' foi enviado com sucesso para o bucket '{bucket_name}'.")

if __name__ == "__main__":

    bucket_name = 'desafio-1234'
    input_file_name = 'arquivo_original.csv'  
    output_file_name = 'dados_manipulado.csv' 

    processar_e_upload(bucket_name, input_file_name, output_file_name)
