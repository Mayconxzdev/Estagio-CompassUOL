# Analisando dados do csv

### Exemplo

Comecei analisando os dados referente ao csv e fazendo a importação do pandas e matplotlib

```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('googleplaystore.csv')
```

### Criando gráfico de barras

Depois de analisar fiz um codigo de barras contendo os top 5 apps por instalação.

```python
df['Installs'] = df['Installs'].astype(str)
df['Installs'] = df['Installs'].str.replace(',', '', regex=False).str.replace('+', '', regex=False)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

top_5_installs = df.nlargest(5, 'Installs')

plt.figure(figsize=(10, 6))
plt.bar(top_5_installs['App'], top_5_installs['Installs'], color='skyblue', edgecolor='black')
plt.xlabel('Aplicativos', fontsize=14)
plt.ylabel('Número de Instalações', fontsize=14)
plt.title('Top 5 Apps por Número de Instalações', fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=8)
for i, v in enumerate(top_5_installs['Installs']):
    plt.text(i, v + 0.05, f'{v:,}', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.show()
```

### Grafico pizza

Criei dois graficos pizza um seguindo o pedido ao desafio e outro que recomendo para uma visualização melhor

irei por o codigo do que eu recomendo, mas caso queira ver o outro grafico ficará na Evidencias

```python
category_counts = df['Category'].value_counts()


top_4_categories = category_counts.head(4)


other_categories = category_counts.iloc[4:].sum()


categories_to_plot = pd.concat([top_4_categories, pd.Series({'Outros': other_categories})])


plt.figure(figsize=(10, 6))
plt.pie(categories_to_plot, labels=categories_to_plot.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribuição de Apps por Categoria (Top 4 + Outros)')
plt.axis('equal')
plt.show()
```

### App mais caro

Aqui eu ja filtrei para buscar o app mais caro e criei um grafico para ele

```python
df['Price'] = df['Price'].replace({'\\$': '', ',': ''}, regex=True)
df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].str.strip()
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')


df_filtered = df[df['Price'] > 0.0]


if not df_filtered.empty:
    most_expensive_app = df_filtered.loc[df_filtered['Price'].idxmax()]


    print("O app mais caro é:", most_expensive_app)


    plt.figure(figsize=(8, 6))


    bars = plt.bar(most_expensive_app['App'], most_expensive_app['Price'], color='#FF6347', edgecolor='black', linewidth=1.5)


    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'${yval:,.2f}', ha='center', va='bottom', fontsize=12, color='black')


    plt.title(f'O Aplicativo Mais Caro: {most_expensive_app["App"]}', fontsize=16, weight='bold', color='#333333')
    plt.xlabel('App', fontsize=14)
    plt.ylabel('Preço (em USD)', fontsize=14)


    plt.xticks(fontsize=12, rotation=45, ha='right', color='#333333')
    plt.yticks(fontsize=12, color='#333333')


    plt.gcf().set_facecolor('#f2f2f2')


    plt.tight_layout()


    plt.show()
else:
    print("Não há aplicativos com preços válidos.")
```

### Aplicativos Mature+17

Aqui tambem filtrei para buscar os app Mature+17 e fiz um grafico top 10 baseado no preço

```python
mature_apps = df[df['Content Rating'] == 'Mature 17+']

mature_apps_count = mature_apps.shape[0]

if mature_apps_count > 0:
    print(f"\nQuantidade de aplicativos classificados como 'Mature 17+': {mature_apps_count}\n")


    mature_apps.loc[:, 'Price'] = mature_apps['Price'].replace({'\\$': '', ',': ''}, regex=True)
    mature_apps.loc[:, 'Price'] = pd.to_numeric(mature_apps['Price'], errors='coerce')


    mature_apps_sorted = mature_apps.sort_values(by='Price', ascending=False)


    top_10_mature_apps = mature_apps_sorted.head(10)


    plt.figure(figsize=(10, 6))
    plt.barh(top_10_mature_apps['App'], top_10_mature_apps['Price'], color='skyblue')
    plt.xlabel('Price ($)')
    plt.ylabel('App')
    plt.title('Top 10 Apps "Mature 17+" por Preço')
    plt.gca().invert_yaxis()
    plt.show()
else:
    print("Nenhum aplicativo classificado como 'Mature 17+' encontrado.")
```

### Reviews

Agora fiz a busca dos top 10 apps por número de reviews e fiz um grafico tambem

```python
def convert_reviews(value):
    if isinstance(value, str):
        if 'M' in value:
            return float(value.replace('M', '').strip()) * 1_000_000
        elif 'K' in value:
            return float(value.replace('K', '').strip()) * 1_000
    return pd.to_numeric(value, errors='coerce')


df['Reviews'] = df['Reviews'].apply(convert_reviews)

df_top_reviews = df.groupby('App')['Reviews'].max().reset_index()


top_10_reviews = df_top_reviews.sort_values(by='Reviews', ascending=False).head(10)


top_10_reviews['Reviews'] = top_10_reviews['Reviews'].astype(int)


print(top_10_reviews)


plt.figure(figsize=(10,6))
top_10_reviews.plot(kind='barh', x='App', y='Reviews', color='purple', legend=False)
plt.title('Top 10 Apps por Número de Reviews')
plt.xlabel('Número de Reviews')
plt.ylabel('Aplicativos')
plt.grid(True, axis='x')
plt.show()
```

### Apps por categoria

E para finalizar fiz um grafico baseado no número de apps por cada categoria

```python
category_counts = df['Category'].value_counts()


plt.figure(figsize=(12,6))
category_counts.head(10).plot(kind='bar', color='c')
plt.title('Número de Apps por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Número de Apps')
plt.xticks(rotation=45)
plt.show()
```

# Todos os graficos falado abaixo

### [Graficos](../Evidencias/)
