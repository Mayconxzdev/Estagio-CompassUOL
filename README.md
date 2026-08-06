# Programa de Bolsas Compass UOL — Engenharia de Dados

Repositório histórico da minha participação no **Programa de Bolsas da Compass UOL**, realizado entre **outubro de 2024 e março de 2025**.

Ao longo de **10 sprints**, evoluí dos fundamentos de Git, Linux e SQL até a construção de um pipeline de dados em AWS com ingestão por arquivos e API, Data Lake em camadas, processamento distribuído, consultas analíticas e dashboard.

> Este material deve ser avaliado como registro de formação prática e evolução técnica. Não representa um ambiente empresarial de produção nem um único produto comercial.

## Visão geral

| Campo | Informação |
|---|---|
| Programa | Programa de Bolsas Compass UOL |
| Período | Out. 2024 – mar. 2025 |
| Duração | Aproximadamente seis meses |
| Organização | 10 sprints |
| Área | Engenharia de Dados |
| Status | Concluído |

## Pipeline desenvolvido

Nas sprints finais, construí um pipeline para análise de dados de filmes e séries:

```text
Arquivos CSV + API TMDB
          ↓
Python / boto3 / AWS Lambda
          ↓
Amazon S3 — Raw Zone
          ↓
AWS Glue + Apache Spark
          ↓
Trusted Zone — Parquet particionado
          ↓
Refined Zone — modelo dimensional
          ↓
Amazon Athena
          ↓
Amazon QuickSight
```

O fluxo envolveu:

1. ingestão de arquivos CSV em estrutura organizada no Amazon S3;
2. consumo da API do TMDB com Python;
3. execução da coleta em AWS Lambda e gravação via boto3;
4. processamento de CSV e JSON com AWS Glue e PySpark;
5. transformação para Parquet e particionamento por data;
6. organização das camadas Raw, Trusted e Refined;
7. modelagem relacional e dimensional, com tabelas fato e dimensão;
8. consultas SQL no Amazon Athena;
9. dashboard analítico no Amazon QuickSight.

## Jornada por sprint

| Sprint | Conteúdo principal |
|---|---|
| [Sprint 1](Sprint1) | Git, GitHub, terminal Linux e controle de versão |
| [Sprint 2](Sprint2) | SQL, consultas, modelagem relacional e dimensional |
| [Sprint 3](Sprint3) | Análise de dados com Python, Pandas e Matplotlib |
| [Sprint 4](Sprint4) | Aplicações Python executadas em containers Docker |
| [Sprint 5](Sprint5) | AWS S3, EC2, boto3, Pandas e Polars |
| [Sprint 6](Sprint6) | Ingestão de CSV para a Raw Zone do Data Lake no S3 |
| [Sprint 7](Sprint7) | API TMDB, AWS Lambda, boto3 e armazenamento JSON no S3 |
| [Sprint 8](Sprint8) | Raw → Trusted com AWS Glue, PySpark, Parquet e particionamento |
| [Sprint 9](Sprint9) | Pipeline ETL, camada Refined e modelagem dimensional |
| [Sprint 10](Sprint10) | Consultas com Athena e dashboard no QuickSight |

## Tecnologias demonstradas

### Linguagens e dados

`Python` · `SQL` · `Pandas` · `Polars` · `PySpark` · `Matplotlib` · `CSV` · `JSON` · `Parquet`

### Engenharia de dados

`ETL` · `Data Lake` · `Raw/Trusted/Refined` · `DataFrames` · `Spark SQL` · `modelagem relacional` · `modelagem dimensional` · `tabelas fato e dimensão`

### AWS

`Amazon S3` · `Amazon EC2` · `AWS Lambda` · `AWS Glue` · `Glue Data Catalog` · `Amazon Athena` · `Amazon QuickSight` · `AWS IAM` · `boto3`

### Desenvolvimento

`Git` · `GitHub` · `Linux` · `Docker`

## Evidências técnicas

- função Lambda para paginação e coleta de filmes na API TMDB;
- gravação de JSON em caminhos organizados no S3;
- jobs Glue/PySpark para leitura de CSV e JSON;
- remoção de registros incompletos;
- escrita em Parquet particionado por ano, mês e dia;
- preparação das camadas Trusted e Refined;
- consultas Athena e dashboard QuickSight;
- código, anotações e capturas preservados por sprint.

## O que este repositório comprova

- progressão prática em dados e cloud ao longo de dez entregas;
- integração entre Python, APIs e serviços AWS;
- construção de pipeline em diferentes camadas;
- processamento com Spark e formatos analíticos;
- modelagem e comunicação de resultados em dashboard;
- documentação da evolução técnica.

## Limites

- o ambiente AWS utilizado durante o programa não permanece ativo;
- o repositório preserva exercícios do período e não foi reescrito como produto de produção;
- serviços estudados em cursos não são apresentados como experiência operacional avançada quando não aparecem no pipeline implementado;
- não são declarados volume, SLA ou ganho de desempenho sem artefato reproduzível correspondente.

## Autor

**Maycon Ferreira**

Projetos mais recentes: [github.com/Mayconxzdev](https://github.com/Mayconxzdev) · [Portfólio](https://mayconxzdev.github.io/)
