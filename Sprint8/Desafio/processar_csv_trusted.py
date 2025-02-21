import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import year, month, dayofmonth, current_date

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'RAW_MOVIES_PATH',
    'RAW_SERIES_PATH',
    'TRUSTED_MOVIES_PATH',
    'TRUSTED_SERIES_PATH'
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

raw_movies_path = args['RAW_MOVIES_PATH']
raw_series_path = args['RAW_SERIES_PATH']
trusted_movies_path = args['TRUSTED_MOVIES_PATH']
trusted_series_path = args['TRUSTED_SERIES_PATH']

df_movies_raw = spark.read.csv(raw_movies_path, header=True, inferSchema=True)
df_movies_trusted = df_movies_raw.dropna()
df_movies_trusted = df_movies_trusted.withColumn("ano", year(current_date()).cast("string")) \
                                     .withColumn("mes", month(current_date()).cast("string")) \
                                     .withColumn("dia", dayofmonth(current_date()).cast("string"))
df_movies_trusted.write.partitionBy("ano", "mes", "dia").mode("overwrite").parquet(trusted_movies_path)

df_series_raw = spark.read.csv(raw_series_path, header=True, inferSchema=True)
df_series_trusted = df_series_raw.dropna()
df_series_trusted = df_series_trusted.withColumn("ano", year(current_date()).cast("string")) \
                                     .withColumn("mes", month(current_date()).cast("string")) \
                                     .withColumn("dia", dayofmonth(current_date()).cast("string"))
df_series_trusted.write.partitionBy("ano", "mes", "dia").mode("overwrite").parquet(trusted_series_path)

job.commit()