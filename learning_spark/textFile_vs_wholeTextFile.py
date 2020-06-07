from pyspark import SparkContext

sc = SparkContext(master="spark://192.168.5.153:7077", appName="test_0")

logs = sc.textFile("hdfs://192.168.5.153:9000/licenses/*")
logs.count()
# 2054
len(logs.collect())
# 2054
logs.collect()[0]
# 'The MIT License (MIT)'
logs.getNumPartitions()
# 47

logs = sc.wholeTextFiles("hdfs://192.168.5.153:9000/licenses/*")
logs.count()
# 47
len(logs.collect())
# 47
logs.collect()[0]
# ('hdfs://192.168.5.153:9000/licenses/LICENSE-AnchorJS.txt',
#  'The MIT License (MIT)\n\nCopyright (c) <year> <copyright'
#  + ' holders>\n\nPermission is hereby granted, free of charge'
#  + ', to any person obtaining a copy\nof this software and associated'
#  + 'documentation files (the "Software"), to deal\nin the Software '
#  + 'without restriction, including without limitation the rights\nto'
#  + ' use, copy, modify, merge, publish, distribute, sublicense, '
#  + 'and/or sell\ncopies of the Software, and to permit persons to '
#  + 'whom the Software is\nfurnished to do so, subject to the following'
#  + ' conditions:\n\nThe above copyright notice and this permission '
#  + 'notice shall be included in\nall copies or substantial portions of'
#  + ' the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY'
#  + ' OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE '
#  + 'WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND '
#  + 'NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS'
#  + ' BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN'
#  + ' ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN '
#  + 'CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\nTHE SOFTWARE.')
logs.getNumPartitions()
# 2
