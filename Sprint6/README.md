# AWS Skill Builder Courses and Data Ingestion Challenge

Este repositório contém materiais e anotações dos seguintes cursos da AWS Skill Builder, além da documentação do desafio de ingestão de dados.

## Cursos

1. **Fundamentals of Analytics on AWS**

   - Introdução aos fundamentos da análise de dados na AWS.
   - Conceitos básicos e serviços principais.

2. **Serverless Analytics**

   - Análise de dados sem servidor.
   - Uso de serviços como AWS Lambda e Amazon Athena.

3. **Introduction to Amazon Athena**

   - Introdução ao Amazon Athena.
   - Consultas SQL diretamente no S3.

4. **AWS Glue Getting Started**

   - Primeiros passos com AWS Glue.
   - ETL (Extract, Transform, Load) na AWS.

5. **Amazon EMR Getting Started**

   - Primeiros passos com Amazon EMR.
   - Processamento de grandes volumes de dados com Hadoop.

6. **Getting Started with Amazon Redshift**

   - Primeiros passos com Amazon Redshift.
   - Armazenamento de dados em larga escala.

7. **Best Practices for Data Warehousing with Amazon Redshift**

   - Melhores práticas para data warehousing com Amazon Redshift.
   - Otimização e desempenho.

8. **Amazon QuickSight - Getting Started**
   - Primeiros passos com Amazon QuickSight.
   - Visualização de dados e criação de dashboards.

## Outros Tópicos

- **AWS Lambda e AWS Athena**
  - Integração de AWS Lambda com Amazon Athena para consultas dinâmicas.
  - Exemplos de uso e casos práticos.

# Desafio de Ingestão de Dados

## 1. Entendimento do Desafio

Certifique-se de que compreendeu os seguintes aspectos:

- **Escopo**: Ingestão de dados CSV para a RAW Zone no Amazon S3 usando Python e boto3.
- **Estrutura do Data Lake**: Inclui etapas de ingestão, armazenamento, processamento e consumo.
- **Requisitos de organização no Git**: Código, comentários, evidências, documentação (Markdown), e DockerFile.

## 2. Planejamento da Primeira Entrega

A primeira entrega foca em:

- **Implementar um script Python**:

  - Ler os arquivos CSV (movies.csv e series.csv) localmente.
  - Fazer upload desses arquivos para o bucket S3 na estrutura especificada:
    ```plaintext
    <nome do bucket>/Raw/Local/Movies/<ano>/<mes>/<dia>/movies.csv
    <nome do bucket>/Raw/Local/Series/<ano>/<mes>/<dia>/series.csv
    ```
  - Utilizar a biblioteca boto3 para interagir com o S3.

- **Criar um container Docker**:

  - Configurar o ambiente para executar o script Python.
  - Criar um DockerFile que inclua todas as dependências necessárias.

- **Executar o container localmente**:
  - Testar a ingestão de arquivos para a RAW Zone do bucket S3.

## 3. Implementação do Script Python

O script deverá conter:

- Função para ler os arquivos CSV.
- Função para conectar ao bucket S3 e enviar os arquivos na estrutura definida.
- Registro de logs para monitorar o processo.

## 4. Configuração do Docker

Configurar um arquivo Dockerfile com:

- Base image Python.
- Instalação das dependências (e.g., boto3).
- Montagem do diretório local para acessar os arquivos CSV.

## 5. Organização do Repositório Git

No repositório Git:

- Criar uma pasta para os arquivos do desafio.
- Estruturar o código, DockerFile e evidências em diretórios separados.

## 6. Documentação no Markdown

Criar um arquivo README.md contendo:

- Descrição do desafio.
- Explicação da solução implementada.
- Prints dos resultados obtidos durante a execução do container e upload no S3.

# Resumo

**Fundamentals of Analytics on AWS:** Aprendi os fundamentos da análise de dados na AWS, incluindo os principais serviços e conceitos básicos.

**Serverless Analytics:** Entendi como realizar análises de dados sem servidor utilizando serviços como AWS Lambda e Amazon Athena.

**Introduction to Amazon Athena:** Aprendi a usar o Amazon Athena para realizar consultas SQL diretamente no S3.

**AWS Glue Getting Started:** Explorei os primeiros passos com AWS Glue, focando em ETL (Extract, Transform, Load) na AWS.

**Amazon EMR Getting Started:** Compreendi como usar o Amazon EMR para processar grandes volumes de dados com Hadoop.

**Getting Started with Amazon Redshift:** Aprendi a configurar e usar o Amazon Redshift para armazenamento de dados em larga escala.

**Best Practices for Data Warehousing with Amazon Redshift:** Estudei as melhores práticas para data warehousing com Amazon Redshift, incluindo otimização e desempenho.

**Amazon QuickSight - Getting Started:** Aprendi a usar o Amazon QuickSight para visualização de dados e criação de dashboards.

**AWS Lambda e AWS Athena:** Explorei a integração de AWS Lambda com Amazon Athena para consultas dinâmicas e exemplos de uso prático.

# Exercícios

1. Exercício sobre Fundamentals of Analytics on AWS
   Resposta Ex1.

2. Exercício sobre Serverless Analytics
   Resposta Ex2.

# Evidências

Ao executar o código do exercício sobre Amazon Athena, observei que as consultas SQL foram executadas com sucesso, conforme podemos ver na imagem dentro do [Exercicios](Exercicios)

# Certificados

[Certificado do Curso Fundamentals of Analytics on AWS](Certificados)
