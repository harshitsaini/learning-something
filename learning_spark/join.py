from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="joins")

stores = sc.parallelize([(100, 'Boca Raton'),
	(101, 'Columbia'),
	(102, 'Cambridge'),
	(103, 'Naperville')
	])

salespeople = sc.parallelize([(1, 'Henry', 100),
	(2, 'Karen', 100),
	(3, 'Paul', 101),
	(4, 'Jimmy', 102),
	(5, 'Janice', None)
	])

salespeople.keyBy(lambda x: x[2]).join(stores).collect()
# [(100, ((1, 'Henry', 100), 'Boca Raton')), (100, ((2, 'Karen', 100), 'Boca Raton')), (101, ((3, 'Paul', 101), 'Columbia')), (102, ((4, 'Jimmy', 102), 'Cambridge'))]

salespeople.keyBy(lambda x: x[2]).leftOuterJoin(stores).collect()
# [(None, ((5, 'Janice', None), None)), (100, ((1, 'Henry', 100), 'Boca Raton')), (100, ((2, 'Karen', 100), 'Boca Raton')), (101, ((3, 'Paul', 101), 'Columbia')), (102, ((4, 'Jimmy', 102), 'Cambridge'))]

stores.rightOuterJoin(salespeople.keyBy(lambda x:x[2])).collect()
# [(100, ('Boca Raton', (1, 'Henry', 100))),
#  (100, ('Boca Raton', (2, 'Karen', 100))),
#  (None, (None, (5, 'Janice', None))),
#  (101, ('Columbia', (3, 'Paul', 101))),
#  (102, ('Cambridge', (4, 'Jimmy', 102)))]

stores.fullOuterJoin(salespeople.keyBy(lambda x:x[2])).collect()
# [(None, (None, (5, 'Janice', None))),
#  (100, ('Boca Raton', (1, 'Henry', 100))),
#  (100, ('Boca Raton', (2, 'Karen', 100))),
#  (101, ('Columbia', (3, 'Paul', 101))),
#  (102, ('Cambridge', (4, 'Jimmy', 102))),
#  (103, ('Naperville', None))]


salespeople.keyBy(lambda x:x[2]).cogroup(stores).mapValues(lambda x: [item for sublist in x for item in sublist]).collect()
# [(100, [(1, 'Henry', 100), (2, 'Karen', 100), 'Boca Raton']),
#  (None, [(5, 'Janice', None)]),
#  (101, [(3, 'Paul', 101), 'Columbia']),
#  (102, [(4, 'Jimmy', 102), 'Cambridge']),
#  (103, ['Naperville'])]

salespeople.keyBy(lambda x:x[2]).cartesian(stores).collect()
# [((100, (1, 'Henry', 100)), (100, 'Boca Raton')),
#  ((100, (1, 'Henry', 100)), (101, 'Columbia')),
#  ((100, (2, 'Karen', 100)), (100, 'Boca Raton')),
#  ((100, (2, 'Karen', 100)), (101, 'Columbia')),
#  ((100, (1, 'Henry', 100)), (102, 'Cambridge')),
#  ((100, (1, 'Henry', 100)), (103, 'Naperville')),
#  ((100, (2, 'Karen', 100)), (102, 'Cambridge')),
#  ((100, (2, 'Karen', 100)), (103, 'Naperville')),
#  ((101, (3, 'Paul', 101)), (100, 'Boca Raton')),
#  ((101, (3, 'Paul', 101)), (101, 'Columbia')),
#  ((102, (4, 'Jimmy', 102)), (100, 'Boca Raton')),
#  ((102, (4, 'Jimmy', 102)), (101, 'Columbia')),
#  ((None, (5, 'Janice', None)), (100, 'Boca Raton')),
#  ((None, (5, 'Janice', None)), (101, 'Columbia')),
#  ((101, (3, 'Paul', 101)), (102, 'Cambridge')),
#  ((101, (3, 'Paul', 101)), (103, 'Naperville')),
#  ((102, (4, 'Jimmy', 102)), (102, 'Cambridge')),
#  ((102, (4, 'Jimmy', 102)), (103, 'Naperville')),
#  ((None, (5, 'Janice', None)), (102, 'Cambridge')),
#  ((None, (5, 'Janice', None)), (103, 'Naperville'))]
