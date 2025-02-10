import json
import boto3
import requests
import os
from datetime import datetime

tmdb_api_key = os.getenv('TMDB_API_KEY')
s3_client = boto3.client('s3')
bucket_name = 'desafio-6'

def discover_movies(page):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={tmdb_api_key}&with_genres=28,12&language=pt-BR&sort_by=release_date.desc&include_adult=false&include_video=false&page={page}&release_date.lte=2022-12-31"
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_to_s3(data, file_path):
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_path,
        Body=json.dumps(data, ensure_ascii=False)
    )

def lambda_handler(event, context):
    try:
        all_movies = []
        page = 1
        while True:
            movies = discover_movies(page)
            all_movies.extend(movies['results'])

            if len(all_movies) >= 100 or page >= movies['total_pages']:
                now = datetime.now()
                date_path = now.strftime("%Y/%m/%d")
                
                file_path = f"Raw/tmdb/json/movie_data/{date_path}/discover_page_{page}.json"
                save_to_s3(all_movies, file_path)
                all_movies = []

            if page >= movies['total_pages']:
                break
            
            page += 1
        
        return {
            'statusCode': 200,
            'body': json.dumps('Dados dos filmes salvos no S3 com sucesso!')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Ocorreu um erro: {str(e)}')
        }

if __name__ == "__main__":
    response = lambda_handler(None, None)
    print(response)
