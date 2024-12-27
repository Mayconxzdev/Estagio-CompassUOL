# Prática de Python com Containers Docker

Durante esta sprint, aprendi a utilizar Docker para executar scripts Python. Aqui estão alguns dos principais comandos e conceitos que aprendi, do básico ao avançado:

## Alguns comandos que eu aprendi de Docker

**Instalação do Docker**
Iniciando a como instalar docker no terminal (aprendi a Instalação nos outros porem preferir utilizar ubuntu)

sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker

**Verificar a instalação do Docker:**
Para Verificara versão e se foi feito a instalação

docker --version

**Contruir uma imagem Docker**

docker build -t nome-da-imagem .

**Listar imagens Docer**

docker images

**Executar um container Docker**

docker run --name nome-do-container nome-da-imagem

**Listar todos os container (até os parados)**

docker ps -a

**Parar um container**

docker stop nome-do-container

**Remover um container**

docker rm nome-do-container

# Evidências

[Evidencias](Evidencias)
