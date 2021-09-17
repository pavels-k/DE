from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext
import pandas as pd
import codecs

def read_file(name):
    f = codecs.open(name, 'r', 'utf-8')
    return f.read()

sql_f = read_file('1.sql')

spark = SparkContext.getOrCreate(SparkConf())
sqlContext = SQLContext(spark)


table1 = sqlContext.read.csv('table1.csv', header="true", sep = ';')
#table1.show()
table1.createOrReplaceTempView('table1')
sqlContext.sql(f'''{sql_f}''').show()
