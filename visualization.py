import matplotlib.pyplot as plt
import matplotlib as mpl
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

def generate_distribution_per_genre_plot(spark, df):
  distribution_per_genre_df = get_distribution_per_genre_df(spark, df).toPandas()

  plt.bar(distribution_per_genre_df.genre, distribution_per_genre_df.countPerGenre)
  plt.title('Count per genre')
  plt.xlabel('Genre')
  plt.ylabel('Count')
  plt.xticks(rotation=45, ha='right')
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.tight_layout()

  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)

def generate_grading_distribution_per_genre_plot(spark, df):
  grading_distribution_per_genre_df = get_grading_distribution_per_genre_df(spark, df).toPandas()

  pivot_df = grading_distribution_per_genre_df.pivot(index='genre', columns='bechdelRating', values='countPerGenrePerBechdelR').fillna(0)
  ax = pivot_df.plot(kind='bar', stacked=True, cmap=mpl.colormaps['tab10'], figsize=(12, 8))
  plt.title('Count per genre per Bechdel rating')
  plt.xlabel('Genre')
  plt.ylabel('Count')
  plt.xticks(rotation=45, ha='right')
  plt.legend(title='Bechdel Rating', bbox_to_anchor=(1.05, 1), loc='upper left')
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.tight_layout()

  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)

def generate_grading_percent_distribution_per_genre_plot(spark, df):
  grading_distribution_per_genre_df = get_grading_distribution_per_genre_df(spark, df).toPandas()

  pivot_df = grading_distribution_per_genre_df.pivot(index='genre', columns='bechdelRating', values='countPerGenrePerBechdelR').fillna(0)
  pivot_df_percentage = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100
  ax = pivot_df_percentage.plot(kind='bar', stacked=True, cmap=mpl.colormaps['tab10'], figsize=(12, 8))
  plt.title('Relative count (%) per genre per Bechdel rating')
  plt.xlabel('Genre')
  plt.ylabel('Count in percent')
  plt.xticks(rotation=45, ha='right')
  plt.legend(title='Bechdel Rating', bbox_to_anchor=(1.05, 1), loc='upper left')
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  plt.tight_layout()

  filename = inspect.stack()[0][3]
  saving_figure(plt, filename)

