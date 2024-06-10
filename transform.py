def get_top_10_most_recent_passing_df(spark):
  query = """
    SELECT title, year, bechdelRating
    FROM imdb_bechdel
    ORDER BY bechdelRating DESC, year DESC
    LIMIT 10
  """
  top_10_most_recent_passing_df = spark.sql(query)
  top_10_most_recent_passing_df.show()

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