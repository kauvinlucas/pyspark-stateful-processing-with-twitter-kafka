# Cómo utilizar este repositorio
## Requisitos
Para poder ejecutar el `streaming_app.ipynb` o los scripts .py, es necesario tener instalado en su máquina:
1. Una distribución Linux, una Virtual Machine con Linux o [WSL con Ubuntu](https://ubuntu.com/wsl) (Windows 10+).
2. Java (jdk 8 o 11) y Python (con pip). La variable JAVA_HOME debe está definida en el sistema.
3. Apache Spark (3.1+). La variable SPARK_HOME debe está definida en el sistema.
4. Apache Kafka (0.1+) y Zookeeper configurado (puedes seguir las instrucciones de instalación [aquí](https://www.tutorialspoint.com/apache_kafka/apache_kafka_installation_steps.htm))
5. Git
6. Una cuenta en [Twitter Developers](https://developer.twitter.com)

## Instrucciones
#### 1. Descargar este repositorio
```
git clone https://github.com/kauvinlucas/pyspark-stateful-processing-with-twitter-kafka
cd pyspark-stateful-processing-with-twitter-kafka
```

#### 2. Ejecutar el siguiente comando para instalar los módulos de Python en su máquina (se recomienda crear antes un entorno virtual de Python. Instrucciones por [aquí](https://docs.python.org/es/3.8/library/venv.html))
```
pip install -r requirements.txt
```

#### 3. Crear un nuevo proyecto y obtener el *consumer key*, *comsumer secret*, *access token* y *access token secret* desde [Twitter Developers](https://developer.twitter.com/en/portal/dashboard). Enviar la información a un nuevo archivo denominado `.env` dentro de *src* con el siguiente comando (reemplazar los <valor> con el valor correspondiente):
```
SPARK_HOME=<directorio donde se encuentra instalado spark> > src/.env
consumer_key=<tu consumer key> >> src/.env
consumer_secret=<tu consumer secret> >> src/.env
access_token=<tu access token> >> src/.env
access_token_secret=<tu access token secret>  >> src/.env
```

#### 4. Activar el Zookeper Server y Kafka Server (reemplazar los <valor> con el directorio correspondiente)
```
cd <directorio al Zookeeper>
bin/zkServer.sh start
cd <directorio al Kafka>
bin/kafka-server-start.sh config/server.properties
```

#### 5. Crear un nuevo tópico de Kafka. El comando tiene la siguiente sintaxis:
```
bin/kafka-topics.sh --create --bootstrap-server <servidor> --replication-factor <valor> --partitions <valor> --topic <tópico>
```

Ejemplo:
```
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic delatam-streaming
```

#### 6. Iniciar el Jupyter Notebook o uno de los scripts :)
Para iniciar el Jupyter notebook:
```
jupyter notebook src/streaming_app.ipynb
```

Para ejecutar uno de los scripts con spark-submit:
```
$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 src/<nombre del script>.py <tópico de Kafka>
```

Por ejemplo:
```
$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 src/wordcount.py delatam-streaming
```

Para terminar el job en la terminal, basta presionar `CTRL` + `C`

#### 7. Spark Streaming hará el procesamiento de los datos que llegan al Kafka. Es necesario ejecutar el `producer.py` para que los datos del Twitter fluyan al tópico de Kafka que hemos creado. El comando se construye de la siguiente manera:
```
python src/producer.py <tópico de Kafka> <bootstrap server de Kafka> <tópico de la consulta en Twitter> <número máximo de consultas>
```

Ejemplo:
```
python src/producer.py delatam-streaming localhost:9092 olympics 50
```

## ¿Tienes algún problema al utilizar este repositorio?
Por favor abrir un nuevo tópico en [issues](https://github.com/kauvinlucas/pyspark-stateful-processing-with-twitter-kafka/issues).