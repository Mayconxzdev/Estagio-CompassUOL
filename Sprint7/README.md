## 📖 Sobre a Sprint

Esta sprint tem como objetivo a ingestão de dados de filmes do TMDB (The Movie Database) para o Amazon S3 utilizando AWS Lambda e boto3. O foco é armazenar os filmes do gênero Ação/Aventura (Categoria da minha squad) em formato JSON na RAW Zone do Data lake.

## 🚀 Tecnologias Utilizadas

- **Python** 🐍
- **AWS Lambda** ☁️
- **Amazon S3** 🗄️
- **TMDB API** 🎬
- **boto3** 🔧
- **Apache Spark** ⚡

## 📌 Como Executar a Sprint

1. Configurar a Chave de API do TMDB no AWS Lambda como variável de ambiente (TMDB_API_KEY).
2. Criar um Bucket S3 (caso ainda não exista) para armazenar os dados.
3. Criar a Função Lambda no AWS e fazer o upload do código fornecido.
4. Executar a Função Lambda para coletar os dados do TMDB e armazená-los no S3.
5. Utilizar Apache Spark para processar e analisar os dados.

## 📌 AWS Lambda - Coletando e Salvando Dados no S3

A função Lambda é responsável por:

- Buscar os dados na API do TMDB usando requests.
- Processar os filmes do gênero Ação/Aventura.
- Salvar os dados no S3 em formato JSON.

### 📜 Código AWS Lambda

```python
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
```

## 📌 Apache Spark - Processamento de Dados

### 🟢 Spark - Códigos Iniciantes

Criando um DataFrame a partir de JSON

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LeituraJSON").getOrCreate()
df = spark.read.json("s3://desafio-6/Raw/tmdb/json/movie_data/*.json")
df.show()
```

Selecionando colunas específicas:

```python
df.select("title", "release_date", "vote_average").show()
```

Filtrando filmes com nota maior que 7:

```python
df.filter(df.vote_average > 7).show()
```

### 🟡 Spark - Códigos Intermediários

Convertendo a coluna release_date para formato de data:

```python
from pyspark.sql.functions import to_date
df = df.withColumn("release_date", to_date(df.release_date, "yyyy-MM-dd"))
df.show()
```

Agrupando os filmes por ano e calculando a média de avaliações:

```python
from pyspark.sql.functions import year, avg

df.groupBy(year(df.release_date).alias("Ano")).agg(avg("vote_average").alias("Média de Votos")).show()
```

Ordenando os filmes pelos mais votados:

```python
df.orderBy(df.vote_average.desc()).show(10)
```

### 🔴 Spark - Códigos Avançados

Escrevendo os dados processados no S3 em formato Parquet

```python
df.write.mode("overwrite").parquet("s3://desafio-6/Processed/movies.parquet")
```

Criando uma Tabela Temporária para SQL

```python
df.createOrReplaceTempView("filmes")
spark.sql("SELECT title, vote_average FROM filmes WHERE vote_average > 8 ORDER BY vote_average DESC").show()
```

Fazendo Join com outra tabela (Exemplo: detalhes dos filmes)

```python
df_detalhes = spark.read.json("s3://desafio-6/Raw/tmdb/json/movie_details/*.json")
df_join = df.join(df_detalhes, "id").select("title", "runtime", "genres")
df_join.show()
```

## 📌 Conclusão

Esta sprint automatiza a coleta de filmes do TMDB e organiza os dados no AWS S3, permitindo processamento posterior com Apache Spark. 🚀

## 📌 Evidências

🔗 [Evidências do Projeto](../evidencias)
