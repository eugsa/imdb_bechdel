from pyspark.sql.functions import *

def get_passing_per_year_df(spark):
  query = """
    SELECT year, bechdelRating, COUNT(title) as movieCount
    FROM imdb_bechdel
    WHERE bechdelRating == 3
    GROUP BY bechdelRating, year
    ORDER BY year DESC
  """
  df = spark.sql(query)
  return df

def get_grading_distribution_per_year_df(spark):
  query = """
    SELECT year, bechdelRating, COUNT(title) as movieCount
    FROM imdb_bechdel
    GROUP BY bechdelRating, year
    ORDER BY year DESC, bechdelRating ASC
  """
  df = spark.sql(query)
  return df

def get_genres_df(df):
  df_genre1 = df.selectExpr('id', 'genre1 AS genre')
  df_genre2 = df.selectExpr('id', 'genre2 AS genre')
  df_genre3 = df.selectExpr('id', 'genre3 AS genre')

  new_df = df_genre1.union(df_genre2).union(df_genre3)
  new_df = new_df.filter(new_df.genre.isNotNull())
  new_df = new_df.filter(new_df.genre != '\\N')
  return new_df

def get_distribution_per_genre_df(spark, df):
  genres_df = get_genres_df(df)
  df = df.drop(df.genre1).drop(df.genre2).drop(df.genre3)
  df.createOrReplaceTempView('movies')
  genres_df.createOrReplaceTempView('genres')

  query = """
    SELECT COUNT(m.title) AS countPerGenre, g.genre
    FROM movies AS m
    JOIN genres AS g
    ON m.id = g.id
    GROUP BY g.genre
    ORDER BY g.genre, COUNT(m.title)
  """
  distribution_per_genre_df = spark.sql(query)
  return distribution_per_genre_df
  
def get_grading_distribution_per_genre_df(spark, df):
  genres_df = get_genres_df(df)
  df = df.drop(df.genre1).drop(df.genre2).drop(df.genre3)
  df.createOrReplaceTempView('movies')
  genres_df.createOrReplaceTempView('genres')

  query = """
    SELECT COUNT(m.title) AS countPerGenrePerBechdelR, m.bechdelRating, g.genre
    FROM movies AS m
    JOIN genres AS g
    ON m.id = g.id
    GROUP BY g.genre, m.bechdelRating
    ORDER BY g.genre, m.bechdelRating, COUNT(m.title)
  """
  grading_distribution_per_genre_df = spark.sql(query)
  return grading_distribution_per_genre_df