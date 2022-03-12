# How to use this repository
## Requisites
To be able to execute the `streaming_app.ipynb` or the scripts .py, it is necessary to have installed in your machine:
1. A Linux distro, a Virtual Machine with Linux installed or [WSL with Ubuntu](https://ubuntu.com/wsl) (Windows 10+).
2. Java (jdk 8 or 11) and Python (with pip). JAVA_HOME variable must be set (export variable).
3. Apache Spark (3.1+). SPARK_HOME variable must be set.
4. Apache Kafka (0.1+) and Zookeeper (you can follow installation instructions [here](https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm))
5. Git
6. An account in [Twitter Developers](https://developer.twitter.com)

## Instructions
#### 1. Download this repository
```
git clone https://github.com/kauvinlucas/pyspark-stateful-processing-with-twitter-kafka
cd pyspark-stateful-processing-with-twitter-kafka
```

#### 2. Install the Python modules in your machine (it is recommended that you create a [virtual environment](https://docs.python.org/es/3.8/library/venv.html)) first.
```
pip install -r requirements.txt
```

#### 3. Create a new project and get the *consumer key*, *comsumer secret*, *access token* and *access token secret* from [Twitter Developers](https://developer.twitter.com/en/portal/dashboard). Send the necessary information to a new file called `.env` in the *src* folder with the following command (replace `<value>` with the corresponding value):
```
SPARK_HOME=<path to Apache Spark folder> > src/.env
consumer_key=<consumer key> >> src/.env
consumer_secret=<consumer secret> >> src/.env
access_token=<access token> >> src/.env
access_token_secret=<access token secret>  >> src/.env
```

#### 4. Start Zookeeper Server and Kafka Server (replace `<value>` with the corresponding value)
```
<path to Zookeeper>/bin/zkServer.sh start
<path to Kafka>/bin/kafka-server-start.sh config/server.properties
```

#### 5. Create a new Kafka topic. The command has the following syntax:
```
<path to Kafka>/bin/kafka-topics.sh --create --bootstrap-server <server uri> --replication-factor <number> \
--partitions <number> --topic <topic>
```

For example:
```
<path to Kafka>/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 \
--partitions 1 --topic delatam-streaming
```

#### 6. Execute the Jupyter Notebook or one of the scripts in a new terminal :)
Make sure that you are still in the root path the of repository.

To start the Jupyter notebook:
```
jupyter notebook src/streaming_app.ipynb
```

To execute one of the scripts with spark-submit (to start the streaming job):
```
$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 \
src/<script name>.py <Kafka topic>
```

For example:
```
$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 \
src/wordcount.py delatam-streaming
```

To kill the streaming job in the terminal, press `CTRL`+`C` in the keyboard

#### 7. Spark Streaming will do the processing on the data that arrives to the Kafka topic. While executing the Spark job, you must execute also the `producer.py` to retrieve Twitter data to the Kafka topic in order to process it in Spark. The script command has the following syntax:
```
python src/producer.py <Kafka topic> <bootstrap server uri> <Twitter query> <max number of queries>
```

For example:
```
python src/producer.py delatam-streaming localhost:9092 olympics 50
```

## ¿Encountered errors while following the instructions?
Please open a new issue [here](https://github.com/kauvinlucas/pyspark-stateful-processing-with-twitter-kafka/issues).