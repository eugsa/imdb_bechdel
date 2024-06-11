from transform import *
from utils import *

def get_filepath_report(function_name, path, file_extension):
  filename = function_name.split('generate_')[1] + '.csv'
  filepath = get_filepath(filename, path)
  return filepath

def generate_passing_per_year_report(spark):
  function_name = inspect.stack()[0][3]
  filepath = get_filepath_report(function_name, REPORTS_PATH, '.csv')
  df = get_passing_per_year_df(spark).toPandas()
  df.to_csv(filepath)

def generate_grading_distribution_per_year_report(spark):
  function_name = inspect.stack()[0][3]
  filepath = get_filepath_report(function_name, REPORTS_PATH, '.csv')
  df = get_grading_distribution_per_year_df(spark).toPandas()
  df.to_csv(filepath)