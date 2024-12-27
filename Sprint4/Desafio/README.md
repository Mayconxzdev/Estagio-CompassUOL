# Desafio Docker

(irei por o markdown em )

Comecei criando um nano chamando nano Dockerfile.carguru e nele coloquei

```python
FROM python:3.9-slim
WORKDIR /app
COPY carguru.py .
CMD ["python", "carguru.py"]

```

Criei a imagem com

```
docker build -f Dockerfile.carguru -t carguru-image .

```

Executei um container a partir da imagem com

```
docker run --name carguru-container carguru-image
```

E sim da para reutilizar o container parado usando

```
docker start carguru-container

```

Agora criei um container interativo com nano chamado mascarar.py

```python
import hashlib

while True:
    input_string = input("Digite uma string para mascarar: ")
    hash_object = hashlib.sha1(input_string.encode())
    hex_dig = hash_object.hexdigest()
    print(f"Hash SHA-1: {hex_dig}")

```

Criei agora um Dockerfile.mascarar

```
FROM python:3.9-slim
WORKDIR /app
COPY mascarar.py .
CMD ["python", "mascarar.py"]
```

Agora contruindo a imagem Docker

```
docker build -f Dockerfile.mascarar -t mascarar-dados .

```

Iniciando um container a partir da imagemm permitindo entrada interativa

```
docker run -it --name mascarar-container mascarar-dados
```

# Todas as evidencias esta aqui

### [Evidencia].(../Evidencias/).
