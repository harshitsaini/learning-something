from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="test_app")

license_files = sc.textFile("hdfs://192.168.5.153:9000/licenses")

words = license_files.flatMap(lambda x:x.split(' '))
words.take(5)
# ['The', 'MIT', 'License', '(MIT)', '']

lowercase = words.map(lambda x:x.lower())
lowercase.take(5)
# ['the', 'mit', 'license', '(mit)', '']

longwords = words.filter(lambda x:len(x)>12)
longwords.take(3)
# ['documentation', 'MERCHANTABILITY,', 'NONINFRINGEMENT.']
