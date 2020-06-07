from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="test_0")
logs = sc.textFile("hdfs://192.168.5.153:9000/LICENSE.txt")

logs.count()
logs.collect()
logs.getNumPartitions()