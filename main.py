from pyspark.sql import SparkSession

filename = 'Bechdel_IMDB_Merge.csv'
dataset_path = '../data/'

def init():
  spark = SparkSession.builder \
      .master("local[1]") \
      .appName("imdb_bechdel_app") \
      .getOrCreate()

  df = spark.read.csv(path=dataset_path+filename,  inferSchema=True, header=True)
  return df

df = init()
print(df)