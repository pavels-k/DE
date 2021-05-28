#! /usr/bin/env python
# -*- coding: utf-8 -*-

# page 47
from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext

spark = SparkContext.getOrCreate(SparkConf())
sqlContext = SQLContext(spark)



table1 = sqlContext.read.csv('test_table.csv', header="true", sep = ';')
table2 = sqlContext.read.csv('test_table_2.csv', header="true", sep = ';')

table_union = table1.union(table2)
table_union.show()


for line in table_union.take(2):
    print(line)