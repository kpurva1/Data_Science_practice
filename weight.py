from pyspark import SparkContext
import sys

sc = SparkContext("local", "app")

text_file = sc.textFile(sys.argv[1])


counts = text_file.map(lambda line:line.split('\t')) \
             .map(lambda line:(line[0],line[1],line[2])) \
             .map(lambda x:[x[1],x[2]]) \
             .map(lambda node:(int(node[0]),int(node[1]))) \
             .reduceByKey(lambda a, b: a + b) \
	     .sortByKey(1,1)
counts.saveAsTextFile(sys.argv[2])


