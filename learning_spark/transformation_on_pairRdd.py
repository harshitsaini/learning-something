from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="test")


kvpairs = sc.parallelize([('city', 'Hayward'), ('state', 'CA'), ('zip', 94541), ('country', 'USA')])

kvpairs.keys().collect()
# ['city', 'state', 'zip', 'country']                                             
kvpairs.values().collect()
# ['Hayward', 'CA', 94541, 'USA']


kvpairs = sc.parallelize([('city', 'Hayward', 1), ('state', 'CA', 2), ('zip', 94541, 3), ('country', 'USA', 4)])
kvpairs.keyBy(lambda x:x[2]).collect()
# [(1, ('city', 'Hayward', 1)), (2, ('state', 'CA', 2)), (3, ('zip', 94541, 3)), (4, ('country', 'USA', 4))]
kvpairs.keyBy(lambda x:x[0]).collect()
# [('city', ('city', 'Hayward', 1)), ('state', ('state', 'CA', 2)), ('zip', ('zip', 94541, 3)), ('country', ('country', 'USA', 4))]


locwtemps = sc.parallelize(["Hayward,71|69|71|71", "Alexandria,50|48|12", "Melbourne,88|21"])
kvpairs = locwtemps.map(lambda x: x.split(','))
kvpairs.take(4)
# [['Hayward', '71|69|71|71'], ['Alexandria', '50|48|12'], ['Melbourne', '88|21']]
locwtemplist = kvpairs.mapValues(lambda x: x.split('|')).mapValues(lambda x: [int(s) for s in x])
locwtemplist.take(4)
# [('Hayward', [71, 69, 71, 71]), ('Alexandria', [50, 48, 12]), ('Melbourne', [88, 21])]
locwtemps = kvpairs.flatMapValues(lambda x: x.split('|')).map(lambda x: (x[0], int(x[1])))
locwtemps.take(4)
# [('Hayward', 71), ('Hayward', 69), ('Hayward', 71), ('Hayward', 71)]



grouped = locwtemps.groupByKey()
grouped.take(1)
# [('Melbourne', <pyspark.resultiterable.ResultIterable object at 0x7eff8d62c710>)]
avgtemps = grouped.mapValues(lambda x: sum(x)/len(x))
avgtemps.collect()
# [('Melbourne', 54.5), ('Alexandria', 36.666666666666664), ('Hayward', 70.5)]



tempups = locwtemps.mapValues(lambda x: (x, 1))
tempups.take(2)
# [('Hayward', (71, 1)), ('Hayward', (69, 1))]
inputstoavg = tempups.reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1]))
averages = inputstoavg.map(lambda x: (x[0], x[1][0]/x[1][1]))
averages.take(4)
# [('Melbourne', 54.5), ('Alexandria', 36.666666666666664), ('Hayward', 70.5)]


maxbycity = locwtemps.foldByKey(0, lambda x,y: x if x > y else y)
maxbycity.collect()
# [('Melbourne', 88), ('Alexandria', 50), ('Hayward', 71)]

sortedbycity = locwtemps.sortByKey()
sortedbycity.collect()
# [('Alexandria', 50), ('Alexandria', 48), ('Alexandria', 12), ('Hayward', 71), ('Hayward', 69), ('Hayward', 71), ('Hayward', 71), ('Melbourne', 88), ('Melbourne', 21)]