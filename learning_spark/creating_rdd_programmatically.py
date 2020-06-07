from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="test_0")

parallel_rdd = sc.parallelize(list(range(10)))
parallel_rdd.count()
# 10

range_rdd = sc.range(10)
range_rdd.count()
# 10
