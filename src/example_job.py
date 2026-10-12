from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col


print('hello from outside')

def etl(df: DataFrame):
  df = df.select(col('name')).filter(col('age')>=35)
  return df

def job():
  spark = SparkSession.builder.appName("Example spark job").getOrCreate()
  sample_data = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Eve", "age": 40}
  ] 
  df = spark.createDataFrame(sample_data)
  df.explain()
  df = etl(df)
  df.show()
  spark.stop()

if __name__ == "__main__":
  print('hello from main')
  job()