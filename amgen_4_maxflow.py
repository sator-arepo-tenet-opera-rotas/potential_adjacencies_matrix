
#build the city intersection network
G1=nx.DiGraph() 
G1.add_edge("a", "b", capacity=2.0) # residential area designated as vertex "a"
G1.add_edge("a", "d", capacity=0.5)
G1.add_edge("b", "d", capacity=3.0)
G1.add_edge("c", "d", capacity=2.5)
G1.add_edge("c", "e", capacity=1.0)
G1.add_edge("e", "f", capacity=4.0)
G1.add_edge("f", "g", capacity=1.0) #  downtown area as vertex "g"

#plot network
capacity_labels=nx.get_edge_attributes(G1,'capacity')
pos = nx.spring_layout(G1)
nx.draw(G1,pos,with_labels=True,)
nx.draw_networkx_edge_labels(G1,pos,edge_labels=capacity_labels)


#find cut-points
partition = nx.minimum_cut(G1, "a", "g")

print(partition)
