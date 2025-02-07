# Desafio Filmes e Séries

Este projeto tem como objetivo a ingestão de dados do TMDB (The Movie Database) utilizando AWS Lambda, com o intuito de complementar informações sobre filmes e séries. Os dados coletados são armazenados no Amazon S3 em formato JSON.

## Estrutura do Projeto

O projeto é organizado da seguinte forma:

```
desafio-filmes-series
├── src
│   ├── lambda_function.py      # Função principal da AWS Lambda para orquestrar a ingestão de dados.
│   ├── tmdb_api.py             # Funções para interagir com a API do TMDB.
│   ├── s3_utils.py             # Funções utilitárias para interagir com o Amazon S3.
│   └── types
│       └── index.py            # Definições de tipos e interfaces para o projeto.
├── requirements.txt             # Lista de dependências do projeto.
├── README.md                    # Documentação do projeto.
└── evidencias
    └── evidencias.md           # Evidências e documentação sobre a realização do desafio.
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

1. Configure suas credenciais da AWS para permitir o acesso ao S3.
2. Implemente a função `lambda_function.py` para orquestrar a ingestão de dados do TMDB.
3. Utilize `tmdb_api.py` para realizar chamadas à API do TMDB e obter dados sobre filmes e séries.
4. Armazene os dados obtidos no S3 utilizando as funções em `s3_utils.py`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.