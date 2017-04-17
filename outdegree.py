from pyspark import SparkContext
import sys

sc = SparkContext("local", "app")

text_file = sc.textFile(sys.argv[1])

#for outdegree calculating occurance of a perticular node in source column

counts = text_file.map(lambda line:line.split('\t')) \
             .map(lambda line:(line[0],line[1],line[2])) \
             .flatMap(lambda x:[x[0]]) \
             .map(lambda node:(int(node),1)) \
             .reduceByKey(lambda a, b: a + b) \
	     .sortByKey(1,1)
counts.saveAsTextFile(sys.argv[2])


