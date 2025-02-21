from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, rand
from pyspark.sql.types import StringType, IntegerType
import random

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")
df_nomes.printSchema()
df_nomes.show(10)

escolaridades = ["Fundamental", "Medio", "Superior"]
def random_escolaridade():
    return random.choice(escolaridades)

escolaridade_udf = udf(random_escolaridade, StringType())
df_nomes = df_nomes.withColumn("Escolaridade", escolaridade_udf())

paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Equador", "Guiana", "Paraguai", "Peru", 
          "Suriname", "Uruguai", "Venezuela", "França"]
def random_pais():
    return random.choice(paises)

pais_udf = udf(random_pais, StringType())
df_nomes = df_nomes.withColumn("Pais", pais_udf())

def random_ano():
    return random.randint(1945, 2010)

ano_udf = udf(random_ano, IntegerType())
df_nomes = df_nomes.withColumn("AnoNascimento", ano_udf())

df_nomes.show(10)

df_nomes.createOrReplaceTempView("pessoas")

df_select = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")
df_select.show(10)

df_millennials = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994")
print(f"Número de Millennials: {df_millennials.count()}")

df_generations = spark.sql("""
    SELECT Pais, 
           CASE 
               WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
               WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
               WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
               WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
           END AS Geração, 
           COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geração
    ORDER BY Pais, Geração, Quantidade
""")
df_generations.show()