#! /usr/bin/env python
# -*- coding: utf-8 -*-

# page 44
from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext

spark = SparkContext.getOrCreate(SparkConf())
sqlContext = SQLContext(spark)

table = sqlContext.read.csv('/home/pavel/Рабочий стол/hadoop/DE/Learning_Spark/Mint/test_table.csv', header="true", sep = ';')
table.show()

lines = sqlContext.read.text("/home/pavel/Рабочий стол/hadoop/DE/Learning_Spark/Mint/test_text.txt")
lines.show()
