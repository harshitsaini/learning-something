from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="test_0")

numbers = sc.range(0, 1000000, 1, 2)
evens = numbers.filter(lambda x: x % 2)
evens.persist()

noelements = evens.count()
listofelements = evens.collect()

# Persistence levels
evens.persist(StorageLevel.MEMORY_AND_DISK)
evens.persist(StorageLevel.MEMORY_AND_DISK_2)
evens.persist(StorageLevel.DISK_ONLY)
evens.persist(StorageLevel.DISK_ONLY_2)
evens.persist(StorageLevel.MEMORY_ONLY)
evens.persist(StorageLevel.MEMORY_ONLY_2)
evens.persist(StorageLevel.OFF_HEAP)

"""
Level                Space used  CPU time  In memory  On disk  Serialized
-------------------------------------------------------------------------
MEMORY_ONLY          High        Low       Y          N        N
MEMORY_ONLY_SER      Low         High      Y          N        Y
MEMORY_AND_DISK      High        Medium    Some       Some     Some
MEMORY_AND_DISK_SER  Low         High      Some       Some     Y
DISK_ONLY            Low         High      N          Y        Y
"""


# Unpersisting all rdds
for (id, rdd) in sc._jsc.getPersistentRDDs().items():
    rdd.unpersist()
    print("Unpersisted {} rdd".format(id))
