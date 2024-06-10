from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

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

def get_top_10_most_recent_passing_df(spark):
  query = """
    SELECT title, year, bechdelRating
    FROM imdb_bechdel
    ORDER BY bechdelRating DESC, year DESC
    LIMIT 10
  """
  top_10_most_recent_passing_df = spark.sql(query)
  top_10_most_recent_passing_df.show()

def get_passing_per_year_df(spark):
  query = """
    SELECT year, bechdelRating, COUNT(title) as movieCount
    FROM imdb_bechdel
    WHERE bechdelRating == 3
    GROUP BY bechdelRating, year
    ORDER BY year DESC
  """
  passing_per_year_df = spark.sql(query)
  return passing_per_year_df

def generate_passing_per_year_plot(spark):
  passing_per_year_df = get_passing_per_year_df(spark).toPandas()
  plt.bar(passing_per_year_df.year, passing_per_year_df.movieCount)
  plt.title('Number of movies passing the Bechdel test per year')
  plt.xlabel('Years')
  plt.ylabel('Movie count')
  plt.show()

spark, df = init()

generate_passing_per_year_plot(spark)