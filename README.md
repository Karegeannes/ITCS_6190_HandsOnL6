# Music Streaming Analysis Using Spark Structured APIs

## Overview

## Dataset Description

## Repository Structure

## Output Directory Structure

## Tasks and Outputs

### Task 1: User Favorite Genres

Selected each user's most played genre.

Query:
```bash
SELECT user_id, MAX_BY(genre, play_count) AS favorite_genre
FROM (
   SELECT l.user_id, s.genre, COUNT(*) AS play_count
   FROM listening_logs l
   JOIN songs_metadata s ON l.song_id = s.song_id
   GROUP BY l.user_id, s.genre
)
GROUP BY user_id
```

Example Output:
```bash
+--------+--------------+
| user_id|favorite_genre|
+--------+--------------+
|  user_1|           Pop|
| user_10|           Pop|
|user_100|          Jazz|
| user_11|       Hip-Hop|
| user_12|          Jazz|
| user_13|          Rock|
| user_14|          Jazz|
| user_15|          Rock|
| user_16|       Hip-Hop|
| user_17|     Classical|
| user_18|          Rock|
| user_19|          Rock|
|  user_2|          Rock|
| user_20|     Classical|
| user_21|          Jazz|
| user_22|          Jazz|
| user_23|          Rock|
| user_24|     Classical|
| user_25|          Jazz|
| user_26|          Jazz|
+--------+--------------+
```
### Task 2: Average Listen Time

Simply got the average listen duration for each song in the listening logs.

Query:
```bash
SELECT song_id, AVG(duration_sec) AS avg_listen_time
FROM listening_logs
GROUP BY song_id
ORDER BY avg_listen_time DESC
```

Example Output:
```bash
+-------+------------------+
|song_id|   avg_listen_time|
+-------+------------------+
|song_19| 201.2608695652174|
|song_11|             198.5|
|song_43|197.11764705882354|
|song_16|             192.7|
|song_44|192.05263157894737|
| song_6|             192.0|
|song_49| 190.1764705882353|
|song_37| 188.5909090909091|
|song_50|182.57894736842104|
| song_3|182.52941176470588|
|song_29|            182.25|
|song_26| 180.1578947368421|
|song_36|179.55555555555554|
| song_8|             179.5|
| song_2| 178.8235294117647|
| song_4|178.26315789473685|
|song_40|             172.5|
|song_13|171.94444444444446|
|song_30|           171.625|
|song_47|             169.9|
+-------+------------------+
```

### Task 3: Create your own Genre Loyalty Scores and rank them and list out top 10

For I went with play count of their most played genre / average playcount across genres to calculate their loyalty score.

Query:
```bash
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
```

Example Output:
```bash
+-------+------------------+
|user_id|     loyalty_score|
+-------+------------------+
| user_8|               2.5|
|user_69|2.3076923076923075|
|user_12|2.2222222222222223|
|user_81|2.1818181818181817|
|user_99| 2.142857142857143|
|user_94|2.0833333333333335|
|user_18|2.0833333333333335|
|user_73|               2.0|
|user_40|               2.0|
|user_82|               2.0|
+-------+------------------+
```

### Task 4: Identify users who listen between 12 AM and 5 AM

Used HOUR(timestamp) in listening_logs to identify users that listen between 12 AM and 5 AM

Query:
```bash
```

Example Output:
```bash
+-------------------+
|early_morning_users|
+-------------------+
|            user_58|
|            user_94|
|            user_14|
|            user_56|
|            user_22|
|            user_68|
|            user_86|
|            user_97|
|            user_65|
|            user_47|
|            user_66|
|            user_21|
|            user_19|
|            user_18|
|            user_13|
|            user_51|
|             user_7|
|            user_95|
|            user_52|
|             user_5|
+-------------------+
```

## Execution Instructions
## *Prerequisites*

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. *Python 3.x*:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. *PySpark*:
   - Install using pip:
     ```bash
     pip install pyspark
     ```

3. *Apache Spark*:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

### *2. Running the Analysis Tasks*

####  *Running Locally*

1. *Generate the Input*:
  ```bash
   python3 datagen.py
   ```

2. **Execute Each Task Using spark-submit**:
   ```bash
     spark-submit main.py
   ```

3. *Verify the Outputs*:
   Check the outputs/ directory for the resulting files:
   ```bash
   ls outputs/
   ```

## Errors and Resolutions
