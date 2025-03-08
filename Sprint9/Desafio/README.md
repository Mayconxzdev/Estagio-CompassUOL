# Desafio de Filmes e Séries – Camada Refined

Este projeto implementa a solução da Entrega 4 do Desafio de Filmes e Séries, onde os dados provenientes da Trusted Zone são transformados e modelados para compor a camada Refined, utilizando a abordagem multidimensional. A solução foi desenvolvida usando AWS Glue com Apache Spark (Spark Script Editor).

## Índice

- Visão Geral
- Arquitetura de Dados
  - Camada Trusted
  - Camada Refined
- Modelo Multidimensional
  - Tabela Fato
  - Tabelas Dimensionais
- Detalhes da Implementação
  - Pré-requisitos
  - Script do Job no AWS Glue
- Exemplos de Consultas
- Evidências

## Visão Geral

Nesta solução, os dados dos filmes são inicialmente coletados na Trusted Zone (já validados e padronizados) e, a partir deles, são realizadas transformações para criar a camada Refined. Essa camada é estruturada de forma a possibilitar análises multidimensionais e facilitar a integração com ferramentas de visualização, como o Amazon QuickSight, na próxima sprint.

## Arquitetura de Dados

### Camada Trusted

- **Origem dos Dados**: Arquivos no formato PARQUET armazenados no S3.
- **Local**: `s3://desafio-6/Trusted/TMDB/Parquet/Movies/2025/3/7/`

### Camada Refined

- **Objetivo**: Transformar e modelar os dados para análises, aplicando os princípios de modelagem multidimensional.
- **Formato de Persistência**: PARQUET (com particionamento, se necessário).
- **Local de Armazenamento**: `s3://desafio-6/Refined/`

## Modelo Multidimensional

O modelo multidimensional segue o conceito de esquema estrela, com uma tabela fato central que se conecta a várias tabelas dimensionais. As tabelas dimensionais armazenam os atributos descritivos dos filmes e ajudam a realizar análises cruzadas.

### Tabela Fato

**fato_filmes**:
Contém as chaves que relacionam os dados com as dimensões. As colunas criadas são:

- `movie_id`
- `id_financeiro`
- `id_popularidade`
- `id_filme`
- `id_tempo`

### Tabelas Dimensionais

**dim_financeiro**:
Armazena atributos financeiros do filme.

- Colunas:
  - `id_financeiro`
  - `budget`
  - `revenue`
  - `runtime`

**dim_popularidade**:
Contém métricas de popularidade e avaliações.

- Colunas:
  - `id_popularidade`
  - `popularity`
  - `vote_average`
  - `vote_count`

**dim_filme**:
Detalhes descritivos do filme.

- Colunas:
  - `id_filme`
  - `original_title`
  - `release_date`
  - `status`
  - `tagline`
  - `title`

**dim_tempo**:
Representa a dimensão temporal, extraindo componentes da data de lançamento.

- Colunas:
  - `id_tempo`
  - `ano`
  - `mês`
  - `dia`

No modelo multidimensional (esquema estrela), a tabela fato centraliza as chaves que se conectam às tabelas dimensionais, permitindo análises cruzadas (por exemplo, juntar dados financeiros com informações temporais e de popularidade).

## Detalhes da Implementação

### Pré-requisitos

- **AWS Glue**: Ambiente configurado para execução de jobs utilizando o Spark Script Editor.
- **S3**: Acesso aos buckets `desafio-6/Trusted` e `desafio-6/Refined`.
- **Formato dos Dados**: Arquivos no formato PARQUET na Trusted Zone.
- **Ferramenta de Visualização**: Planejada para integração futura com o Amazon QuickSight.

### Script do Job no AWS Glue

O script abaixo foi utilizado para ler os dados da Trusted Zone, transformá-los conforme o modelo multidimensional e gravá-los na camada Refined:

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import year, month, dayofmonth

# Parâmetros e inicialização do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho dos dados na Trusted Zone
trusted_path = "s3://desafio-6/Trusted/TMDB/Parquet/Movies/2025/3/7/"

# Leitura dos dados da Trusted Zone
movies_df = spark.read.parquet(trusted_path)

# Criação da Tabela Fato
fato_filmes = movies_df.selectExpr(
    "id as movie_id",
    "id as id_financeiro",
    "id as id_popularidade",
    "id as id_filme",
    "id as id_tempo"
)
fato_filmes.write.mode("overwrite").format("parquet").save("s3://desafio-6/Refined/fato_filmes")

# Criação da Dimensão Financeira
dim_financeiro = movies_df.selectExpr(
    "id as id_financeiro",
    "budget",
    "revenue",
    "runtime"
)
dim_financeiro.write.mode("overwrite").format("parquet").save("s3://desafio-6/Refined/dim_financeiro")

# Criação da Dimensão de Popularidade
dim_popularidade = movies_df.selectExpr(
    "id as id_popularidade",
    "popularity",
    "vote_average",
    "vote_count"
)
dim_popularidade.write.mode("overwrite").format("parquet").save("s3://desafio-6/Refined/dim_popularidade")

# Criação da Dimensão do Filme
dim_filme = movies_df.selectExpr(
    "id as id_filme",
    "original_title",
    "release_date",
    "status",
    "tagline",
    "title"
)
dim_filme.write.mode("overwrite").format("parquet").save("s3://desafio-6/Refined/dim_filme")

# Criação da Dimensão Temporal
dim_tempo = movies_df.selectExpr(
    "id as id_tempo",
    "year(release_date) as ano",
    "month(release_date) as mês",
    "dayofmonth(release_date) as dia"
)
dim_tempo.write.mode("overwrite").format("parquet").save("s3://desafio-6/Refined/dim_tempo")

job.commit()
```

# Exemplos de Consultas

Após a transformação dos dados, podemos executar consultas SQL sobre a camada Refined. Aqui estão alguns exemplos de consultas que podem ser realizadas:

**Consulta para analisar os filmes por ano de lançamento:**

```sql
SELECT t.ano, COUNT(f.movie_id) AS total_filmes
FROM fato_filmes f
JOIN dim_tempo t ON f.id_tempo = t.id_tempo
GROUP BY t.ano
ORDER BY t.ano;
```

**Consulta para comparar o orçamento e a receita dos filmes por popularidade:**

```sql
SELECT p.popularity, f.movie_id, d.budget, d.revenue
FROM fato_filmes f
JOIN dim_popularidade p ON f.id_popularidade = p.id_popularidade
JOIN dim_financeiro d ON f.id_financeiro = d.id_financeiro
ORDER BY p.popularity DESC;

```

**Consulta para obter filmes com avaliação acima da média:**

```sql
SELECT f.movie_id, d.title, p.vote_average
FROM fato_filmes f
JOIN dim_popularidade p ON f.id_popularidade = p.id_popularidade
JOIN dim_filme d ON f.id_filme = d.id_filme
WHERE p.vote_average > 7.0
ORDER BY p.vote_average DESC;
```

# Evidências

📁 [Evidências](../Evidencias/)
