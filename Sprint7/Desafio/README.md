# Desafio de Filmes e Séries - Etapa 2

## Objetivo

Este projeto tem como objetivo realizar a ingestão de dados de filmes do gênero **Ação/Aventura** (Categoria da minha squad) a partir da API do TMDB e armazená-los na **RAW Zone do Amazon S3** no formato JSON. A solução é implementada utilizando **AWS Lambda** e a biblioteca `boto3` para interagir com o S3.

## Tecnologias Utilizadas

- **Python**
- **AWS Lambda**
- **Amazon S3**
- **TMDB API**
- **boto3** (SDK da AWS para Python)

## Estrutura do Projeto

O projeto consiste nos seguintes componentes:

### 1. Função Lambda

A função Lambda coleta os dados da API do TMDB e os salva no Amazon S3. O código principal está estruturado em:

- `discover_movies(page)`: Busca filmes da API TMDB com os gêneros definidos e retorna os resultados.
- `save_to_s3(data, file_path)`: Salva os dados no S3 no formato JSON.
- `lambda_handler(event, context)`: Controla o fluxo de execução da função Lambda, garantindo que os dados sejam extraídos e armazenados corretamente.

### 2. Armazenamento no Amazon S3

Os arquivos JSON são salvos na seguinte estrutura dentro do bucket `desafio-6`:
Raw/ tmdb/ json/ movie*data/ {YYYY}/{MM}/{DD}/discover_page*{page}\_{timestamp}.json

O timestamp é adicionado ao nome do arquivo para evitar sobrescrita.

## Como Executar

### 1. Configurar Variáveis de Ambiente

Antes de executar, defina a chave da API do TMDB como uma variável de ambiente no AWS Lambda:
TMDB_API_KEY= "Minha_Chave"

### 2. Criar e Configurar a Função Lambda

1. Criar uma **função Lambda** na AWS.
2. Adicionar uma **camada** contendo as dependências (`boto3`, `requests`).
3. Configurar a variável de ambiente `TMDB_API_KEY`.
4. Atribuir permissões para escrita no S3.
5. Fazer upload do código.

### 3. Testar Localmente

Para testar fora da AWS Lambda, execute:

```bash
python lambda_function.py
```

### 4. Executar na AWS Lambda

A função Lambda pode ser acionada manualmente ou por um gatilho de agendamento (EventBridge) para rodar periodicamente.

### 5. Evidencias

[📂 Acesse a pasta Evidências](../Evidencias/)
