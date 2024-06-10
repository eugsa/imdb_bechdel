from pyspark.sql import SparkSession
from transform import *
import visualization

filename = 'Bechdel_IMDB_Merge.csv'
dataset_path = '../data/'

def init():
  spark = SparkSession.builder \
      .master("local[1]") \
      .appName("imdb_bechdel_app") \
      .getOrCreate()

  df = spark.read.csv(path=dataset_path+filename,  inferSchema=True, header=True)
  df.createOrReplaceTempView("imdb_bechdel")
  return spark, df

def generate_passing_per_year_plot(spark):
  visualization.generate_passing_per_year_plot(spark)
  # passing_per_year_df = get_passing_per_year_df(spark).toPandas()
  # plt.bar(passing_per_year_df.year, passing_per_year_df.movieCount)
  # plt.title('Number of movies passing the Bechdel test per year')
  # plt.xlabel('Years')
  # plt.ylabel('Movie count')
  # plt.show()

spark, df = init()

generate_passing_per_year_plot(spark)