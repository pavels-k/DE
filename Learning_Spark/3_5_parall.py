# page 44

# PYSPARK_PYTHON = ...\python.exe
from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SQLContext
import pandas as pd

spark = SparkContext.getOrCreate(SparkConf())
sqlContext = SQLContext(spark)


df_pd = pd.read_csv('test_table.csv', sep = ';')

df_sc = sqlContext.createDataFrame(df_pd)
df_sc.show()
