# Pyspark stateful processing example with twitter API and Apache Kafka
[![Linux](https://svgshare.com/i/Zhy.svg)](https://www.linux.org) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](LICENSE)

馃嚭馃嚫 馃嚞馃嚙
## What is this?
This is a repository of a hands-on project consisting of a pipeline of streaming processing with Apache Kafka, Apache Spark and Twitter Streaming API v2. This project is meant to understand the concepts behind stateful processing and event time processing with Spark Streaming. Data from recent tweets are ingested to one of the topics in Kafka, and then retrieved into a Spark streaming application for processing.

The Jupyter notebook provided here is writen in spanish. To use this repository or see *requirements*, please follow the instructions provided [here](docs/en.md).

馃嚜馃嚫
## De qu茅 se trata este repositorio?
Este repositorio contiene los materiales usados en un proyecto simples de procesamiento en streaming con Apache Kafka, Apache Spark y Twitter API v2. Se trat贸 de comprender algunos de los conceptos por detr谩s del procesamiento en streaming con Spark, tales como event time, stateful processing y watermarking. La idea aqu铆 es extraer los tweets m谩s recientes mediante una aplicaci贸n en Python, hacer la ingesta de la informaci贸n a Kafka y procesarlos dentro de Spark.

La aplicaci贸n de Spark se encuentra en el `streaming_app.ipynb` o en los scripts de Python. Para utilizar este reposit贸rio, por favor siga las instrucciones [aqui](docs/es.md).

## Estructura del repositorio
```
pyspark-stateful-processing-with-twitter-kafka
鈹?   LICENSE.txt 
鈹?   README.md
鈹?   requirements.txt
鈹?
鈹斺攢鈹?鈹?assets
鈹?   鈹?   jupyter_app.jpg
鈹?
鈹斺攢鈹?鈹?docs
鈹?   鈹?   en.md
鈹?   鈹?   es.md
鈹?
鈹斺攢鈹?鈹?src
    鈹?   streaming_app.ipynb
    鈹?   producer.py
    鈹?   tweetcount.py
    鈹?   wordcount.py
```

[![Jupyter notebook](assets/jupyter_app.jpg)](src/streaming_app.ipynb)