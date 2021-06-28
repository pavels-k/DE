import sys, os
sys.path.append('/opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/lib/spark/python/lib/py4j-0.10.7-src.zip')
sys.path.append('/opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/lib/spark/python')
os.environ["SPARK_HOME"] = "/opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/lib/spark"
os.environ["PYSPARK_PYTHON"] = "python" # "/usr/bin/python2.7"
os.environ["PYTHONPATH"] = "/home/ec2-user/jupyter/lib/graphframes-080.zip"
os.environ["PYSPARK_SUBMIT_ARGS"] = "--packages graphframes:graphframes:0.8.0-spark2.4-s_2.11 pyspark-shell"
