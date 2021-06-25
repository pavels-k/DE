#! /usr/bin/env python
# -*- coding: utf-8 -*-

# page 44
from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext

spark = SparkContext.getOrCreate(SparkConf())
sqlContext = SQLContext(spark)



table = sqlContext.read.csv('test_table.csv', header="true", sep = ';')
table.show()

lines = sqlContext.read.text("test_text.txt")
lines.show()
