from pyspark.sql import SparkSession
import visualization
import reporting
from config import *

def init():
  spark = SparkSession.builder \
      .master("local[1]") \
      .appName("imdb_bechdel_app") \
      .getOrCreate()

  df = spark.read.csv(path=DATASET_PATH+DATASET_FILENAME,  inferSchema=True, header=True)
  df.createOrReplaceTempView("imdb_bechdel")
  return spark, df

def generate_passing_per_year_plot():
  spark, df = init()
  visualization.generate_passing_per_year_plot(spark)

def generate_passing_per_year_report():
  spark, df = init()
  reporting.generate_passing_per_year_report(spark)

def generate_grading_distribution_per_year_report():
  spark, df = init()
  reporting.generate_grading_distribution_per_year_report(spark)

def generate_grading_distribution_per_genre():
  spark, df = init()
  reporting.generate_grading_distribution_per_genre(spark, df)
