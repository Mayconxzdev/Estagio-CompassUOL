# Desafio de Filmes e Séries - Etapa 5: Criação de Dashboard no AWS QuickSight

## Descrição

Na Etapa 5 do Desafio de Filmes e Séries, o objetivo foi criar um dashboard interativo no AWS QuickSight, consumindo os dados processados na Camada Refined do data lake. A análise foi feita a partir dos dados armazenados no AWS S3 em formato Parquet, com a integração do Amazon Athena para consultas SQL.

Este README descreve como foi realizada a criação do dashboard e os principais insights extraídos da análise.

## Estrutura do Projeto

- **Camada Refined:** Contém os dados processados e organizados para análise.
- **Fonte de Dados:** Os dados são consumidos pelo AWS QuickSight a partir do Amazon Athena.
- **Dashboard:** O dashboard é composto por diferentes visualizações para apresentar os insights sobre o desempenho dos filmes e séries.

## Passos para Criação do Dashboard

1.  **Preparação dos Dados**

    - Os dados utilizados para o dashboard foram processados na Camada Refined utilizando o AWS Glue, transformando-os para o formato Parquet e realizando particionamento conforme necessário.

2.  **Integração com o Amazon Athena**

    - O Amazon Athena foi configurado para acessar os dados da Camada Refined no S3 e permitir consultas SQL.
    - Os dados foram estruturados para garantir que as consultas fossem rápidas e eficientes.

3.  **Criação de Conjunto de Dados no QuickSight**

    - No AWS QuickSight, criamos um conjunto de dados que se conecta diretamente ao Athena.
    - Esse conjunto de dados serve como a base para a criação das visualizações.

4.  **Criação de Visualizações**

    - Foram criados diferentes tipos de visualizações para explorar os dados e extrair insights valiosos:
      - Gráficos de Barras para comparar o desempenho de filmes por ROI.
      - Gráficos de Linhas para analisar a evolução da popularidade dos filmes ao longo do tempo.
      - Gráficos de Dispersão para observar a correlação entre orçamento e receita dos filmes.

5.  **Publicação e Compartilhamento**
    - O dashboard foi publicado no QuickSight e está disponível para visualização.
    - Ele permite que usuários interajam com os dados e visualizem os insights gerados a partir das análises.

## Tecnologias Utilizadas

- **Amazon S3:** Armazenamento dos dados processados.
- **Amazon Athena:** Execução de consultas SQL nos dados armazenados no S3.
- **AWS QuickSight:** Ferramenta para criação de dashboards interativos.
- **AWS Glue:** Transformação dos dados para o formato Parquet e particionamento.

## Insights Obtidos

A partir dos dados apresentados no dashboard, conseguimos obter diversos insights, como:

- Comparação de ROI entre os filmes da franquia Bad Boys.
- Análise de popularidade ao longo do tempo.
- Avaliação do impacto do orçamento nas receitas dos filmes.

## Conclusão

A Etapa 5 do Desafio de Filmes e Séries proporcionou uma excelente oportunidade para trabalhar com ferramentas poderosas da AWS, como o Athena e o QuickSight, para criar visualizações e extrair insights valiosos a partir de grandes volumes de dados.
