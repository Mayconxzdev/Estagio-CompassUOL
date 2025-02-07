def lambda_handler(event, context):
    import json
    from tmdb_api import fetch_tmdb_data
    from s3_utils import upload_to_s3

    # Captura os dados do TMDB
    tmdb_data = fetch_tmdb_data()

    # Processa os dados recebidos
    processed_data = process_tmdb_data(tmdb_data)

    # Envia os dados processados para o S3
    s3_path = "raw/tmdb/json/"
    upload_to_s3(processed_data, s3_path)

    return {
        'statusCode': 200,
        'body': json.dumps('Dados processados e enviados para o S3 com sucesso!')
    }

def process_tmdb_data(data):
    # Função para processar os dados do TMDB
    # Aqui você pode adicionar lógica para filtrar ou transformar os dados conforme necessário
    return data