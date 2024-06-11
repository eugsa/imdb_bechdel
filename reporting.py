from transform import *
from utils import *

def generate_passing_per_year_report(spark):
  filename = inspect.stack()[0][3]
  filename = filename.split('generate_')[1] + '.csv'
  filepath = get_filepath(filename, REPORTS_PATH)

  passing_per_year_df = get_passing_per_year_df(spark).toPandas()
  passing_per_year_df.to_csv(filepath)