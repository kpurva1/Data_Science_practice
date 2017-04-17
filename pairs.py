from pyspark import SparkContext
import sys

sc = SparkContext("local", "app")

text_file = sc.textFile(sys.argv[1])

#1st RDD Source - destinatio nodes (key : source node)

counts = text_file.map(lambda line:line.split('\t')) \
             .map(lambda line:(line[0],line[1],line[2])) \
             .map(lambda x:[x[0],x[1]]) \
             .map(lambda node:(int(node[0]),int(node[1]))) \
             .sortByKey(1,1)

#2nd RDD destination - source nodes (key : destination node)

counts1 = text_file.map(lambda line:line.split('\t')) \
             .map(lambda line:(line[0],line[1],line[2])) \
             .map(lambda x:[x[1],x[0]]) \
             .map(lambda node:(int(node[0]),int(node[1]))) \
             .sortByKey(1,1)

#creating result RDD by taking intersection of above two RDDs

counts3 = counts.intersection(counts1) \
		.sortByKey(1,1) \
		.sortBy(lambda a:a[1]) \
		.groupByKey().mapValues(list) \
		.sortByKey(1,1)

counts3.saveAsTextFile(sys.argv[2])



