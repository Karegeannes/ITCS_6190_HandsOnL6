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
    SELECT user_id, MAX_BY(genre, play_count) AS favorite_genre
    FROM (
        SELECT l.user_id, s.genre, COUNT(*) AS play_count
        FROM listening_logs l
        JOIN songs_metadata s ON l.song_id = s.song_id
        GROUP BY l.user_id, s.genre
    )
    GROUP BY user_id
"""
task1 = spark.sql(query)
task1.show()

# Task 2: Average Listen Time
#Used average listen time by song
query = """
    SELECT song_id, AVG(duration_sec) AS avg_listen_time
    FROM listening_logs
    GROUP BY song_id
    ORDER BY avg_listen_time DESC
"""
task2 = spark.sql(query)
task2.show()

# Task 3: Create your own Genre Loyalty Scores and rank them and list out top 10
#My Genre Loyalty Score: favorite genre playcount / average genre playcount
query = """
    SELECT user_id, MAX(play_count)/AVG(play_count) as loyalty_score
    FROM (
        SELECT l.user_id, s.genre, COUNT(*) AS play_count
        FROM listening_logs l
        JOIN songs_metadata s ON l.song_id = s.song_id
        GROUP BY l.user_id, s.genre
    )
    GROUP BY user_id
    ORDER BY loyalty_score DESC
    LIMIT 10
"""
task3 = spark.sql(query)
task3.show()

# Task 4: Identify users who listen between 12 AM and 5 AM
query = """
    SELECT DISTINCT user_id as early_morning_users
    FROM listening_logs
    WHERE HOUR(timestamp) >= 0 AND HOUR(timestamp) < 5
"""
task4 = spark.sql(query)
task4.show()