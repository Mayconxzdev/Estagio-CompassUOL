import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import year, month, dayofmonth, current_date

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'RAW_API_TMDB_PATH',
    'TRUSTED_API_TMDB_PATH'
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

raw_api_tmdb_path = args['RAW_API_TMDB_PATH']
trusted_api_tmdb_path = args['TRUSTED_API_TMDB_PATH']

df_raw = spark.read.json(raw_api_tmdb_path)
df_trusted = df_raw.dropna()
df_trusted = df_trusted.withColumn("ano", year(current_date())) \
                       .withColumn("mes", month(current_date())) \
                       .withColumn("dia", dayofmonth(current_date()))
df_trusted.write.partitionBy("ano", "mes", "dia").mode("overwrite").parquet(trusted_api_tmdb_path)

job.commit()