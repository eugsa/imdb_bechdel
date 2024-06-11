def get_passing_per_year_df(spark):
  query = """
    SELECT year, bechdelRating, COUNT(title) as movieCount
    FROM imdb_bechdel
    WHERE bechdelRating == 3
    GROUP BY bechdelRating, year
    ORDER BY year DESC
  """
  passing_per_year_df = spark.sql(query)
  return passing_per_year_df

def get_grading_distribution_per_year_df(spark):
  query = """
    SELECT year, bechdelRating, COUNT(title) as movieCount
    FROM imdb_bechdel
    GROUP BY bechdelRating, year
    ORDER BY year DESC, bechdelRating ASC
  """
  grading_distribution_per_year_df = spark.sql(query)
  return grading_distribution_per_year_df
