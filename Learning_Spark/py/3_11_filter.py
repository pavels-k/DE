#! /usr/bin/env python
# -*- coding: utf-8 -*-

# page 46
from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext, functions as f

spark = SparkContext.getOrCreate(SparkConf())
sqlContext = SQLContext(spark)

lines = sqlContext.read.text("test_text.txt")
new_lines = lines.where(f.col('value').like("%has%"))
new_lines.show()