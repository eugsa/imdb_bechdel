from transform import *

def generate_passing_per_year_report(spark):
  filename = './reports/generate_passing_per_year_report.csv'
  passing_per_year_df = get_passing_per_year_df(spark).toPandas()
  passing_per_year_df.to_csv(filename)