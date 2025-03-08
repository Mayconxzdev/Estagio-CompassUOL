# Desafio de Engenharia de Dados: Processamento de Filmes e Séries com AWS Glue e Spark

Este projeto faz parte do **Desafio de Engenharia de Dados**, no qual desenvolvemos um pipeline ETL (Extract, Transform, Load) para processar dados de filmes e séries. Utilizamos **AWS Glue** e **Apache Spark** para realizar as transformações necessárias e otimizar o processamento de dados em larga escala. A seguir, apresento um resumo das tecnologias utilizadas, os principais aprendizados adquiridos e a estrutura do projeto.

## Tecnologias e Ferramentas Utilizadas

- **AWS Glue**: Serviço de ETL totalmente gerenciado que facilita a preparação e carga de dados para análise. Permite a criação de jobs para extração, transformação e carregamento de dados de maneira escalável. [Documentação do AWS Glue](https://docs.aws.amazon.com/glue/)
- **Apache Spark**: Framework de código aberto para processamento de dados em larga escala, oferecendo APIs para manipulação de dados estruturados e não estruturados. Utilizado em conjunto com o AWS Glue para realizar transformações complexas nos dados. [Documentação do Apache Spark](https://spark.apache.org/docs/latest/)
- **Amazon S3**: Serviço de armazenamento de objetos da AWS, utilizado para armazenar dados brutos (raw data) e dados processados (refined data). [Documentação do Amazon S3](https://aws.amazon.com/s3/)
- **AWS IAM**: Serviço de gerenciamento de identidades e acessos da AWS, utilizado para definir permissões e roles necessárias para a execução dos jobs no AWS Glue. [Documentação do AWS IAM](https://aws.amazon.com/iam/)

## Aprendizados Adquiridos

- **Configuração de Ambiente na AWS**: Aprendi a configurar serviços da AWS, como IAM para gerenciamento de permissões, S3 para armazenamento de dados e Glue para orquestração de jobs ETL.
- **Desenvolvimento de Jobs ETL com AWS Glue e Spark**: Desenvolvi habilidades na criação de scripts Spark dentro do AWS Glue para realizar transformações de dados, incluindo leitura de dados do S3, aplicação de funções de transformação e gravação dos dados processados de volta no S3.
- **Modelagem de Dados**: Compreendi a importância de estruturar os dados de forma eficiente para análises futuras, utilizando conceitos de tabelas fato e dimensões.
- **Automação de Processos**: Aprendi a automatizar o fluxo de dados desde a ingestão até a transformação e carga, garantindo eficiência e escalabilidade no processamento.
- **Boas Práticas de Segurança e Custos**: Entendi a necessidade de gerenciar permissões de forma adequada e monitorar os recursos utilizados para otimizar custos na nuvem.

## Estrutura do Projeto

- **Desafio/**: Contém os scripts desenvolvidos para o processamento ETL utilizando AWS Glue e Spark.
- **Evidencias/**: Diretório destinado a evidências dos dados e resultados armazenados no Amazon S3.

## Considerações Finais

Este projeto proporcionou uma experiência prática no desenvolvimento de pipelines ETL utilizando serviços gerenciados da AWS e ferramentas de processamento de dados em larga escala. Os conhecimentos adquiridos são fundamentais para a construção de soluções escaláveis e eficientes no contexto de engenharia de dados.

Para mais detalhes sobre a implementação e os scripts utilizados, consulte os arquivos na pasta `Desafio/` deste repositório.

![Evidência do Desafio](Evidencias/)
