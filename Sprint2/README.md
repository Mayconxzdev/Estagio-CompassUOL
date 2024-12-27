## SQL para Análise de Dados

Durante esta sprint, aprendi a utilizar SQL para realizar análises de dados. Aqui estão alguns dos principais comandos e conceitos que aprendi, do básico ao avançado:

### Alguns comando que eu aprendi

**SELECT**: Utilizado para selecionar dados de uma tabela.

```sql
SELECT * FROM tabela;
```

**WHERE**: Utilizado para filtrar registros.

```sql
SELECT * FROM tabela WHERE condição;
```

**GROUP BY**: Utilizado para agrupar registros que têm valores iguais em colunas especificadas.

```sql
SELECT coluna, COUNT(*) FROM tabela GROUP BY coluna;
```

**ORDER BY**: Utilizado para ordenar os resultados.

```sql
SELECT * FROM tabela ORDER BY coluna ASC|DESC;
```

**Subqueries**: Consultas dentro de outras consultas.

```sql
SELECT * FROM tabela WHERE coluna IN (SELECT coluna FROM tabela2 WHERE condição);
```

**Views**: Utilizado para criar vistas de consultas complexas.

```sql
CREATE VIEW nome_da_view AS SELECT colunas FROM tabela WHERE condição;
```

# Modelagem de Dados

**Modelagem Relacional**: Estruturação de dados em um modelo relacional, utilizando tabelas normalizadas para reduzir redundâncias e garantir a integridade dos dados. [Modelagem-Relacional](Evidencias/Modelo-racional.png)

**Modelagem Dimensional**: Criação de modelos dimensionais para data warehouses, utilizando tabelas fato e dimensão para organizar os dados de forma eficiente para análise. [Modelagem-Dimensional](Evidencias/Modelo-dimencional.png)

# Evidências

[Scripts](Desafio/concessionaria/)

[Evidencias](Evidencias)
