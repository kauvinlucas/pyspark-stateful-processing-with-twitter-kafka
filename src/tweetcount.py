import findspark
import os
from dotenv import load_dotenv
import sys

load_dotenv()

arguments = sys.argv
if len(arguments) > 2 or len(arguments) < 2:
	print("Please provide a Kafka topic in this format: \npython wordcount.py <topic>")
else:
    topic_name = str(sys.argv[1])

    if __name__ == '__main__':
        from pyspark.sql import SparkSession
        import pyspark.sql.types as t
        import pyspark.sql.functions as f

        # Start SparkSession
        spark = spark_session = SparkSession \
            .builder \
            .appName("Twitter Kafka Stream") \
            .getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")
        print("SparkSession started...")

        # Reduce number of Shuffle partitions to 5
        spark.conf.set("spark.sql.shuffle.partitions", "5")

        # Read Kafka topic
        streaming_in = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", topic_name).option("startingOffsets", "latest").load()

        # Stateful processing with watermark
        schema = t.StructType([
                t.StructField("creation_time", t.StringType(), True),
                t.StructField("tweet_text", t.StringType(), False)])
        recent_tweets = streaming_in.selectExpr("CAST(value AS STRING)")
        recent_tweets = recent_tweets.select(f.from_json(f.col("value"), schema).alias("data")).select("data.*")
        recent_tweets = recent_tweets.withColumn("creation_time",f.to_timestamp("creation_time"))
        query_event_time = recent_tweets.withWatermark("creation_time", "1 minutes").groupBy(f.window(f.col("creation_time"), "5 minutes", "1 minutes")).count().writeStream.queryName("tweets_per_window").format("console").outputMode("update").start()
        print("Streaming processing started...")
        print("Execute the 'producer.py' script to start processing streaming data")
        query_event_time.awaitTermination()