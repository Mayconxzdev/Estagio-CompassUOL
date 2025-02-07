def upload_to_s3(bucket_name, file_name, data):
    import boto3
    import json

    s3 = boto3.client('s3')
    
    # Converte os dados para JSON
    json_data = json.dumps(data)
    
    # Define o caminho do arquivo no S3
    s3_path = f"raw_zone/{file_name}.json"
    
    # Faz o upload do arquivo para o S3
    s3.put_object(Bucket=bucket_name, Key=s3_path, Body=json_data)

def create_s3_file_name(base_name, index):
    return f"{base_name}_{index}"