import matplotlib.pyplot as plt
from utils import *
from transform import *

def saving_figure(plt, filename):
    filepath = get_filepath(filename, FIGURES_PATH, '.png')
    plt.savefig(filepath)
    print(f"See saved figure as { filepath }")
    plt.close()

def generate_passing_per_year_plot(spark):
  passing_per_year_df = get_passing_per_year_df(spark).toPandas()
  plt.bar(passing_per_year_df.year, passing_per_year_df.movieCount)
  plt.title('Number of movies passing the Bechdel test per year')
  plt.xlabel('Years')
  plt.ylabel('Movie count')

  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)