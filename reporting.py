from transform import *
from utils import *

def generate_passing_per_year_report(spark):
  function_name = inspect.stack()[0][3]
  filepath = get_filepath(function_name, REPORTS_PATH, '.csv')
  df = get_passing_per_year_df(spark).toPandas()
  df.to_csv(filepath)

def generate_grading_distribution_per_year_report(spark):
  function_name = inspect.stack()[0][3]
  filepath = get_filepath(function_name, REPORTS_PATH, '.csv')
  df = get_grading_distribution_per_year_df(spark).toPandas()
  df.to_csv(filepath)

def generate_grading_distribution_per_genre(spark, df):
  # function_name = inspect.stack()[0][3]
  # filepath = get_filepath(function_name, REPORTS_PATH, '.csv')
  df = get_grading_distribution_per_genre_df(spark, df).toPandas()
  # df.to_csv(filepath)