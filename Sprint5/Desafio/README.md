# Desafio AWS com S3 e Manipulação de Dados

Este projeto realiza a criação de um bucket no Amazon S3, o upload de arquivos CSV e manipulação de dados utilizando Python, Pandas, e AWS SDK (boto3).

## Passos Realizados

1. **Carregar Credenciais AWS**

   - Utiliza um arquivo `credenciais.json` para carregar as credenciais de acesso (AccessKeyId, SecretAccessKey, e SessionToken) para autenticação na AWS.
   - O método `carregar_credenciais()` é responsável por carregar as credenciais em formato JSON.

2. **Criação do Bucket no S3**

   - O bucket é criado com a função `criar_bucket()`, que recebe o nome do bucket e a região como parâmetros.
   - Se a região for `us-east-1`, a criação é feita diretamente; para outras regiões, o parâmetro `LocationConstraint` é configurado.
   - A função imprime uma confirmação quando o bucket é criado com sucesso.

3. **Upload de Arquivo para o S3**

   - O arquivo `arquivo_original.csv` é enviado para o bucket utilizando a função `upload_arquivo()`.
   - Utilizando o método `upload_file` do boto3, o arquivo é enviado para o bucket configurado na AWS.
   - A função imprime uma mensagem de sucesso após o envio do arquivo.

4. **Manipulação de Dados com Pandas**

   - O arquivo CSV (`arquivo_original.csv`) é carregado com o Pandas usando `pd.read_csv()`, com um delimitador `;`.
   - A coluna `nu_idade` é manipulada para criar uma nova coluna `idade_grupo`, categorizando as idades em "Acima de 50" ou "50 ou menos".
   - A coluna `dt_nascimento` é convertida para o formato de data com `pd.to_datetime()`, e a coluna `ano_nascimento` é extraída com `.dt.year`.
   - A coluna `sg_sexo` é convertida para letras maiúsculas e salva como `sg_sexo_upper`.

5. **Salvar o Arquivo Manipulado**

   - O DataFrame manipulado é salvo em um novo arquivo CSV chamado `dados_manipulado.csv` utilizando `to_csv()`.
   - O arquivo é salvo com codificação UTF-8 e delimitado por ponto e vírgula.

6. **Upload do Arquivo Manipulado para o S3**
   - O arquivo manipulado `dados_manipulado.csv` é enviado para o bucket criado anteriormente.

## Arquivos Utilizados

- `credenciais.json`: Contém as credenciais de acesso à AWS (AccessKeyId, SecretAccessKey, e SessionToken).
- `arquivo_original.csv`: Arquivo CSV de entrada contendo dados para manipulação.
- `dados_manipulado.csv`: Arquivo CSV de saída com os dados manipulados.

## Código Completo

O código completo utilizado está disponível na pasta `evidencias`.

## Evidências

[Evidencias/Script](Evidencias/Script)
