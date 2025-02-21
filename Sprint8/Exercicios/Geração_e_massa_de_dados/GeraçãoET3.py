import random
import time
import os
import names

random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

aux = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

dados = [random.choice(aux) for _ in range(qtd_nomes_aleatorios)]

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_csv = os.path.join(diretorio_atual, "arquivos_criados")
os.makedirs(pasta_csv, exist_ok=True) 

caminho_arquivo_nomes = os.path.join(pasta_csv, "nomes_aleatorios.txt")

with open(caminho_arquivo_nomes, "w", encoding="utf-8") as file:
    for nome in dados:
        file.write(f"{nome}\n")

print(f"Arquivo '{caminho_arquivo_nomes}' gerado com sucesso!")