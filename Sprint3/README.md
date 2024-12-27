# Análise de Dados com Python, pandas e matplotlib.pyplot

Durante esta sprint, aprendi a utilizar Python, pandas e matplotlib.pyplot para realizar análises de dados. Aqui estão alguns dos principais comandos e conceitos que aprendi, do básico ao avançado:

### Alguns comandos que eu aprendi

#### Python

**Leitura de Arquivos**

```python
with open('arquivo.txt', 'r') as file:
    dados = file.read()
```

**Uso de Dicionários**

```python
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
valor = dicionario['chave1']
```

**Funções**

```python
def soma(a, b):
    return a + b
```

#### Pandas

**Leitura de dados**

```python
import pandas as pd
df = pd.read_csv('arquivo.csv')
```

**Filtragem de dados**

```python
import pandas as pd
df = pd.read_csv('arquivo.csv')
df_filtrado = df[df['coluna'] == 'valor']
```

**Agrupamento de dados**

```python
import pandas as pd
df = pd.read_csv('arquivo.csv')
df_agrupado = df.groupby('coluna').size()
```

#### Matplotlib.pyplot

**Criação de gráficos**

```python
import matplotlib.pyplot as plt
plt.plot(df['coluna'])
plt.show()
```

**Gráficos de barras**

```python
import matplotlib.pyplot as plt
df['coluna'].value_counts().plot(kind='bar')
plt.show()
```

**Gráficos de dispersão**

```python
import matplotlib.pyplot as plt
plt.scatter(df['coluna1'], df['coluna2'])
plt.show()
```

# Evidências

[Scripts]

[Evidencias](Evidencias)
