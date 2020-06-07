import re

from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="word_count")

doc = sc.textFile("hdfs://192.168.5.153:9000/shakespeare.txt")

flattened = doc.filter(lambda line: len(line)>0).flatMap(lambda line: re.split('\W+', line))
flattened.take(6)

kvpairs = flattened.filter(lambda word: len(word)>0).map(lambda word:(word.lower(), 1))
kvpairs.take(5)

countsbyword = kvpairs.reduceByKey(lambda x,y: x+y).sortByKey(ascending=False)
countsbyword.take(10)

topwords = countsbyword.map(lambda x: (x[1], x[0])).sortByKey(ascending=False)
print(topwords.take(5))

topwords.saveAsTextFile("file:///home/harshit/Desktop/word_count/")