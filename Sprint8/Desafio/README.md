# Desafio de Filmes e Séries - Etapa 3

## 1. Objetivo

O objetivo desta etapa do desafio é processar os dados da Camada Trusted do data lake, garantindo que estejam limpos e confiáveis. Isso será feito integrando os dados da RAW Zone para a Trusted Zone utilizando Apache Spark no AWS Glue. Os dados serão armazenados no S3 no formato Parquet, registrados no Glue Data Catalog e disponibilizados para consultas no AWS Athena.

## 2. Entregáveis

- Todo o código, comentários, evidências e demais artefatos devem estar devidamente organizados e versionados no Git.
- Arquivo Markdown contendo evidências, imagens e prints da realização do desafio, bem como a documentação detalhada das etapas executadas.
- Explicação sobre os motivadores de cada API e as perguntas que serão respondidas na última etapa do desafio.
- Código-fonte documentado e organizado:
  - **Código AWS Glue para processamento de arquivos CSV.**
  - **Código AWS Glue para processamento de arquivos JSON (API TMDB).**

## 3. Preparação

Antes de iniciar, é fundamental compreender completamente o escopo do Desafio de Filmes e Séries, conforme descrito na Sprint 6.

## 4. Desafio

O desafio está dividido em cinco entregas, sendo esta a **Entrega 3**, que se concentra no processamento da Camada Trusted.

### 4.1. Entrega 3 - Processamento da Camada Trusted

A Camada Trusted do data lake contém dados limpos e confiáveis, resultantes da integração de diversas fontes na RAW Zone.

#### Escopo desta Etapa:

- Utilizar **AWS Glue com Apache Spark** para processar os dados da RAW Zone e armazená-los na Trusted Zone.
- Os dados serão armazenados no S3 no formato **Parquet**.
- Os dados JSON da API TMDB serão **particionados por ano, mês e dia** com base na data de criação do arquivo.
- Os dados CSV (batch) **não serão particionados**.
- Todos os dados da Trusted Zone estarão disponíveis no **AWS Athena** através de consultas SQL.

#### Configuração dos Jobs no AWS Glue:

- **Spark script editor** será utilizado para desenvolver os jobs.
- **Configuração dos Jobs:**
  - **Worker type:** G1.x (menor configuração disponível).
  - **Número de workers:** 2 (mínimo necessário).
  - **Timeout do job:** 60 minutos ou menos.

### 4.2. Código-Fonte

#### **Processamento de Arquivos CSV (AWS Glue)**

```python
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import year, month, dayofmonth, current_date

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'RAW_MOVIES_PATH',
    'RAW_SERIES_PATH',
    'TRUSTED_MOVIES_PATH',
    'TRUSTED_SERIES_PATH'
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

raw_movies_path = args['RAW_MOVIES_PATH']
raw_series_path = args['RAW_SERIES_PATH']
trusted_movies_path = args['TRUSTED_MOVIES_PATH']
trusted_series_path = args['TRUSTED_SERIES_PATH']

df_movies_raw = spark.read.csv(raw_movies_path, header=True, inferSchema=True)
df_movies_trusted = df_movies_raw.dropna()
df_movies_trusted = df_movies_trusted.withColumn("ano", year(current_date()).cast("string")) \
                                     .withColumn("mes", month(current_date()).cast("string")) \
                                     .withColumn("dia", dayofmonth(current_date()).cast("string"))
df_movies_trusted.write.partitionBy("ano", "mes", "dia").mode("overwrite").parquet(trusted_movies_path)

df_series_raw = spark.read.csv(raw_series_path, header=True, inferSchema=True)
df_series_trusted = df_series_raw.dropna()
df_series_trusted = df_series_trusted.withColumn("ano", year(current_date()).cast("string")) \
                                     .withColumn("mes", month(current_date()).cast("string")) \
                                     .withColumn("dia", dayofmonth(current_date()).cast("string"))
df_series_trusted.write.partitionBy("ano", "mes", "dia").mode("overwrite").parquet(trusted_series_path)

job.commit()
```

#### **Processamento de Arquivos JSON (API TMDB - AWS Glue)**

```python
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import year, month, dayofmonth, current_date

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'RAW_API_TMDB_PATH',
    'TRUSTED_API_TMDB_PATH'
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

raw_api_tmdb_path = args['RAW_API_TMDB_PATH']
trusted_api_tmdb_path = args['TRUSTED_API_TMDB_PATH']

df_raw = spark.read.json(raw_api_tmdb_path)
df_trusted = df_raw.dropna()
df_trusted = df_trusted.withColumn("ano", year(current_date())) \
                       .withColumn("mes", month(current_date())) \
                       .withColumn("dia", dayofmonth(current_date()))
df_trusted.write.partitionBy("ano", "mes", "dia").mode("overwrite").parquet(trusted_api_tmdb_path)

job.commit()

```

### 4.3. Parâmetros dos Jobs

Os seguintes parâmetros foram utilizados nos Jobs AWS Glue:

#### **Processamento de CSV:**

- `RAW_MOVIES_PATH`: Caminho dos arquivos CSV de filmes na RAW Zone.
- `RAW_SERIES_PATH`: Caminho dos arquivos CSV de séries na RAW Zone.
- `TRUSTED_MOVIES_PATH`: Caminho dos arquivos de filmes na Trusted Zone.
- `TRUSTED_SERIES_PATH`: Caminho dos arquivos de séries na Trusted Zone.

#### **Processamento de JSON:**

- `RAW_API_TMDB_PATH`: Caminho dos arquivos JSON da API TMDB na RAW Zone.
- `TRUSTED_API_TMDB_PATH`: Caminho dos arquivos JSON da API TMDB na Trusted Zone.

### 📂 Evidências

📁 [Evidências](../Evidencias/)
