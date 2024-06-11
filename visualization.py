import matplotlib.pyplot as plt
from utils import *
from transform import *

def get_filepath(filename, path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, path + filename)
    return filepath

def saving_figure(plt, filename):
    filepath = get_filepath(filename, FIGURES_PATH)
    plt.savefig(filepath)
    print(f"See saved figure as { filepath }.png")
    plt.close()

def generate_passing_per_year_plot(spark):
  passing_per_year_df = get_passing_per_year_df(spark).toPandas()
  plt.bar(passing_per_year_df.year, passing_per_year_df.movieCount)
  plt.title('Number of movies passing the Bechdel test per year')
  plt.xlabel('Years')
  plt.ylabel('Movie count')

  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)