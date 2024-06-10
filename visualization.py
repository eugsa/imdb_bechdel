import matplotlib.pyplot as plt
from transform import *

def generate_passing_per_year_plot(spark):
  passing_per_year_df = get_passing_per_year_df(spark).toPandas()
  plt.bar(passing_per_year_df.year, passing_per_year_df.movieCount)
  plt.title('Number of movies passing the Bechdel test per year')
  plt.xlabel('Years')
  plt.ylabel('Movie count')
  plt.show()