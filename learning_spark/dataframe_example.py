from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('test_1').master("spark://192.168.5.153:7077").getOrCreate()

df = spark.read.json("hdfs://192.168.5.153:9000/people.json")
df.collect()                                                                	
# [Row(age=69, name='harshit'), Row(age=2, name='rahul'), Row(age=3, name='ram')] 
df.dtypes
# [('age', 'bigint'), ('name', 'string')]
df.show()
# +---+-------+
# |age|   name|
# +---+-------+
# | 69|harshit|
# |  2|  rahul|
# |  3|    ram|
# +---+-------+



from pyspark.sql import SQLContext

sqlContext = SQLContext(spark)
sqlContext.registerDataFrameAsTable(df, "people")

df2 = spark.sql("SELECT name, age FROM people WHERE age > 20")
df2.show()
# +-------+---+
# |   name|age|
# +-------+---+
# |harshit| 69|
# +-------+---+

