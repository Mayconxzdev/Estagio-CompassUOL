import os

lista_animais = [
    "Leão", "Tigre", "Elefante", "Zebra", "Girafa", "Crocodilo", "Jacaré", "Macaco", "Canguru", "Koala",
    "Pinguim", "Rinoceronte", "Hipopótamo", "Urso", "Lobo", "Raposa", "Coruja", "Águia", "Delfim", "Tubarão"
]

lista_animais.sort()

[print(animal) for animal in lista_animais]

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

pasta_csv = os.path.join(diretorio_atual, "arquivos_criados")
os.makedirs(pasta_csv, exist_ok=True)

caminho_arquivo = os.path.join(pasta_csv, "animais.csv")

with open(caminho_arquivo, "w", encoding="utf-8") as file:
    for animal in lista_animais:
        file.write(f"{animal}\n")
