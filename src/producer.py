import tweepy
import time
from kafka import KafkaProducer
import os
from dotenv import load_dotenv
import sys

load_dotenv()

arguments = sys.argv
if len(arguments) > 5 or len(arguments) < 5:
	print("Please provide a Kafka topic, a Twitter query and the number of queries in the following format: \npython producer.py <topic> <Kafka bootstrap server address> <Twitter query> <max number of queries>")
else:
    topic_name = str(sys.argv[1])
    query = str(sys.argv[3])
    max_results = str(sys.argv[4])
    bootstrap_server = str(sys.argv[2])

    if __name__ == '__main__':
        consumer_key = os.environ["consumer_key"]
        consumer_secret = os.environ["consumer_secret"]
        access_token = os.environ["access_token"]
        access_token_secret = os.environ["access_token_secret"]

        client = tweepy.Client(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)

        print("Authentication completed. Starting...")

        producer = KafkaProducer(bootstrap_servers=[bootstrap_server])
        tweets = client.search_recent_tweets(query=query, max_results=max_results, user_auth=True, tweet_fields=["created_at,lang"])
        count = 0

        print("Streaming recent tweets about \""+query+"\" to Kafka...")
        for tweet in tweets.data:
            count += 1
            print("Sending tweet nr. "+str(count)+" out of "+str(max_results)+" to topic "+topic_name, end="\r")
            creation_time = str(tweet.created_at).split("+")[0]
            dict_ = str({"creation_time":creation_time, "tweet_text":tweet.text})
            producer.send(topic_name, str.encode(dict_))
            time.sleep(3)