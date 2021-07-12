import sys, os
sys.path.append('/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark/python/lib/py4j-0.10.7-src.zip')
sys.path.append('/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark/python')
os.environ["SPARK_HOME"] = "/opt/cloudera/parcels/CDH-6.3.2-1.cdh6.3.2.p0.1605554/lib/spark"
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python2.7"

import pandas as pd

def _show(df,cnt=20):
    return pd.DataFrame(df.take(cnt),columns=df.columns)

def _sql(s,cnt=20):
    
    df = spark.sql(s) 
    return pd.DataFrame(df.take(cnt),columns=df.columns)