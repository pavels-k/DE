# page 44

from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext

spark = SparkContext.getOrCreate(SparkConf())
sqlContext = SQLContext(spark)

table = sqlContext.read.csv('C:\\Users\\Павел\\Desktop\\Спарк_Практика\\Моё\\test_table.csv', header="true", sep = ';')
table.show()

lines = sqlContext.read.text("C:\\Users\\Павел\\Desktop\\Спарк_Практика\\Моё\\test_text.txt")
lines.show()