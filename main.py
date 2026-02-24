# main.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("MusicAnalysis").getOrCreate()

# Load datasets
logs = spark.read.csv('listening_logs.csv', header=True, inferSchema=True)
song = spark.read.csv('songs_metadata.csv', header=True, inferSchema=True)
#Register as views
logs.createOrReplaceTempView("listening_logs")
song.createOrReplaceTempView("songs_metadata")

# Task 1: User Favorite Genres
query = """
PUT QUERY HERE
"""
task1 = spark.sql(query)
task1.show()

# Task 2: Average Listen Time
query = """
PUT QUERY HERE
"""
task2 = spark.sql(query)
task2.show()

# Task 3: Create your own Genre Loyalty Scores and rank them and list out top 10
query = """
PUT QUERY HERE
"""
task3 = spark.sql(query)
task3.show()

# Task 4: Identify users who listen between 12 AM and 5 AM
query = """
PUT QUERY HERE
"""
task4 = spark.sql(query)
task4.show()