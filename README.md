# Data_Science_practice
1 : to gain experience with Open Baltimore data, Jupyter notebooks, pandas, and building/evaluating classifiers
2. to explore python connector for MySQL 
3. Implement 2-class logistic regression using gradient descent as outlined in the lecture notes. You can do either batch or stochastic versions of the algorithm.
4. simple Spark programs. graph.tsv, which contains a file in which each line is a triple of the form: SOURCE_NODE <TAB> DESTINATION_NODE <TAB> WEIGHT. Note that source and destination nodes are integers, as are weights. 
    For each node, compute the outdegree (number of outgoing edges) and output the (node, count) pairs in sorted order by node : outdegree.py.
    For each node, compute the sum of weights of incoming edges and output the (node, weight_sum) pairs in order sorted by node: weight.py.
    For each node X, find a list of all other nodes Y such that there is an (X, Y) edge in the graph and a (Y, X) edge in the graph, and output the (X, [Y1, Y2, ..., Yn]) pairs in order sorted by X. :pairs.py. 
