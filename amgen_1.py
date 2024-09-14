import amgen_0.py

#create adjacency matrix
adj1 = nx.adjacency_matrix(STRS)
adj1.todense()

#find all shortest paths starting at Store 1
length1, path1 = nx.single_source_dijkstra(STRS,"store1")

length1
