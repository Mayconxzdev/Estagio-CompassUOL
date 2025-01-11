# Desafio AWS Cloud Quest - Aprendizado e Implementações

Este repositório documenta os aprendizados adquiridos durante a participação no **Desafio** e no **AWS Cloud Quest**. O objetivo principal destes dois foi utilizar diversos serviços da AWS, como EC2, S3, entre outros, para resolver problemas práticos de manipulação de dados, automação de tarefas e segurança na nuvem.

## Conceitos Básicos de Nuvem

### O que é Computação em Nuvem?

A **computação em nuvem** envolve o fornecimento de serviços de TI (como servidores, armazenamento, bancos de dados, redes, software, etc.) pela internet. A AWS oferece esses serviços, permitindo que as empresas escalem suas operações de forma eficiente e com baixo custo, sem a necessidade de manter infraestrutura física.

### Benefícios da Nuvem

- **Escalabilidade**: Capacidade de aumentar ou diminuir recursos conforme necessário, sem se preocupar com a infraestrutura física.
- **Redução de Custos**: Pagamento conforme o uso, permitindo economizar em comparação com investimentos em hardware e manutenção.
- **Agilidade**: Implementação rápida de soluções e novos serviços sem grandes investimentos iniciais.
- **Segurança**: Proteção de dados utilizando ferramentas avançadas de segurança e práticas recomendadas.

### Modelos de Implantação de Nuvem

- **Nuvem Pública**: A infraestrutura é compartilhada entre vários clientes, com gerenciamento feito pelo provedor de nuvem.
- **Nuvem Privada**: Infraestrutura dedicada a uma única organização, oferecendo maior controle e segurança.
- **Nuvem Híbrida**: Combina nuvens públicas e privadas, permitindo que dados e aplicativos se movam entre os dois ambientes conforme necessário.

## Serviços Principais da AWS

A AWS oferece uma série de serviços para atender diferentes necessidades empresariais. Durante o desafio, explorei os seguintes serviços:

- **Amazon S3**: Criação e manipulação de buckets para armazenamento e recuperação de dados. Integração com scripts Python para automação de tarefas de processamento de dados.
- **Amazon EC2**: Execução de instâncias EC2 para rodar scripts de processamento de dados, interagir com o S3 e automatizar tarefas no ambiente de nuvem.
- **Manipulação de Dados em CSV e JSON**: Processamento de dados utilizando as bibliotecas `pandas` ou `polars` para leitura, manipulação e exportação de dados nos formatos CSV e JSON.

### Segurança na Nuvem

A AWS implementa uma série de práticas de segurança em seus serviços, como o **Gerenciamento de Identidade e Acesso (IAM)**, que permite o controle sobre quem pode acessar os recursos da nuvem e com quais permissões. Também são oferecidas opções de **criptografia de dados** tanto em trânsito quanto em repouso, garantindo que as informações estejam protegidas.

### Modelos de Cobrança e Precificação

A AWS utiliza um modelo de cobrança **pay-as-you-go**, onde você paga apenas pelos recursos que utiliza. A cobrança pode variar dependendo do serviço, com base em tempo de uso, quantidade de dados processados ou armazenados, entre outros. A AWS oferece também opções de otimização de custos, como instâncias reservadas e descontos para uso a longo prazo.

### Casos de Uso Comuns

Empresas de diversos setores, como tecnologia, saúde e finanças, utilizam os serviços da AWS para:

- **Escalabilidade**: Empresas podem aumentar ou diminuir sua infraestrutura rapidamente conforme a demanda.
- **Armazenamento de Dados**: Organizações podem armazenar grandes volumes de dados de forma segura e acessível.
- **Automação de Processos**: Automatizar tarefas repetitivas com funções Lambda para melhorar a eficiência operacional.

### Impactos no Negócio

A adoção da nuvem pode transformar a forma como as empresas operam, proporcionando:

- **Redução de Custos**: Menor necessidade de investimentos em hardware e manutenção.
- **Maior Agilidade**: Capacidade de implementar novas soluções rapidamente.
- **Inovação**: As empresas podem focar mais em inovação ao delegar a infraestrutura para provedores de nuvem como a AWS.

## Objetivos do Desafio

Durante o desafio, foram trabalhados os seguintes objetivos:

- **Uso do Amazon S3**: Criação e manipulação de buckets para armazenar e recuperar dados, com foco em integrar o S3 com scripts Python.
- **Uso do Amazon EC2**: Implementação de instâncias EC2 para executar scripts de processamento de dados, interagir com o S3 e executar tarefas automatizadas.
- **Manipulação de Dados em CSV e JSON**: Processamento de dados utilizando as bibliotecas `pandas` e `polars` para leitura, manipulação e exportação de arquivos em formatos CSV e JSON.
- **Integração de serviços**: Conectar o S3, EC2outras ferramentas AWS para realizar um fluxo de trabalho completo, desde o armazenamento até a manipulação e análise de dados.

## Ferramentas Utilizadas

Durante o desafio, as seguintes ferramentas foram essenciais:

- **AWS S3**: Para armazenamento de arquivos e dados.
- **AWS EC2**: Para execução de scripts de processamento de dados.
- **boto3**: Biblioteca Python para interagir com os serviços da AWS.
- **pandas**: Biblioteca Python para manipulação de dados em formato tabular (CSV).
- **polars**: Biblioteca alternativa ao `pandas`, utilizada para manipulação de dados de forma eficiente e com alto desempenho.

## Estrutura do Projeto

A estrutura do projeto foi organizada da seguinte forma:

- **Bucket S3**: O bucket utilizado no desafio foi chamado `desafio`, onde os arquivos de dados foram armazenados e manipulados.
- **Pasta de Scripts**: Todos os scripts utilizados para processamento de dados estão localizados na pasta `Evidencias/Script`.

## O que foi aprendido

Durante o desafio, aprendi:

- **AWS S3**: Como criar buckets, carregar arquivos e realizar operações básicas de leitura e escrita com objetos no S3.
- **AWS EC2**: Como configurar instâncias EC2 para executar scripts de processamento de dados e automatizar tarefas.
- **Python & AWS**: Como integrar o Python com a AWS utilizando `boto3` para interagir com o S3, EC2, RDS e Lambda.
- **Manipulação de Dados**: Aprendi a manipular dados utilizando `pandas` para processar arquivos CSV e `polars` para trabalhar com grandes volumes de dados de maneira eficiente.

## Conclusão

Este desafio me proporcionou uma visão abrangente sobre como utilizar os serviços da AWS para resolver problemas de negócios e otimizar processos. A experiência adquirida com **EC2**, **S3** e **segurança na nuvem** é fundamental para desenvolver soluções baseadas em nuvem eficientes e escaláveis. Com esse conhecimento, estou capacitado a implementar soluções que ajudam as empresas a inovar, reduzir custos e aumentar sua agilidade no mercado.

Durante o desafio, além de trabalhar com os serviços da AWS diretamente, busquei conhecimentos de fontes externas para expandir minha compreensão e melhorar a implementação do projeto. Algumas das áreas em que me aprofundei foram:

- **Melhores Práticas de Arquitetura na AWS**: Pesquisei sobre as melhores práticas para projetar arquiteturas seguras, escaláveis e eficientes na AWS, garantindo que a solução fosse otimizada e atendesse aos requisitos de desempenho e segurança.
- **Segurança na Nuvem**: Investi em aprender mais sobre as práticas recomendadas de segurança na nuvem, incluindo criptografia de dados, gerenciamento de identidade e acesso (IAM), e como mitigar vulnerabilidades em ambientes de nuvem.

- **Automação e Otimização de Custos**: Explorei técnicas de automação "usando AWS Lambda" e ferramentas de monitoramento de custos, como o AWS Cost Explorer, para garantir que os recursos estivessem sendo utilizados de forma eficiente e com o mínimo de desperdício financeiro.

- **Performance e Escalabilidade**: Aprofundei-me no uso de autoescalabilidade com EC2 e como otimizar a performance de aplicações e bancos de dados em larga escala, além de explorar diferentes tipos de instâncias e seu impacto no desempenho.

- **Integração entre Serviços AWS**: Procurei entender mais sobre a integração de diferentes serviços da AWS (S3, EC2, Lambda, RDS) e como orquestrar fluxos de trabalho complexos para uma automação mais robusta e escalável.

Esses conhecimentos complementares foram cruciais para o sucesso do projeto, pois permitiram que eu aplicasse as melhores práticas em todas as etapas do desenvolvimento e aproveitasse ao máximo as funcionalidades oferecidas pela AWS.

algumas desses conhecimentos não foram exigidos diretamente no desafio, mas foram adquiridos com o objetivo de expandir minhas habilidades e estar preparado para futuros projetos e melhorias. Eles me permitem aplicar soluções mais robustas e escaláveis, caso surjam necessidades específicas no futuro.

Este repositório reflete meu aprendizado e experiência com a AWS, podendo ser expandido conforme novas necessidades ou integrações com outros serviços da plataforma.
