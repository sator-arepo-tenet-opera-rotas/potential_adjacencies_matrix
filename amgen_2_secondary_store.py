import amgen_0.py
import amgen_1.py

#create a different Stores network
STRS2 = nx.Graph()
STRS2.add_nodes_from(["store1","store2","store3","store4","store5"])

#define weighted ebunch
e12 = [("store1","store2",2), ("store1","store4",3)]
e22 = [("store2","store3",3.7), ("store2","store4",1.4)]
e32 = [("store3","store4",4.9), ("store4","store5",5.4)]

#add edges
STRS2.add_weighted_edges_from(e12)
STRS2.add_weighted_edges_from(e22)
STRS2.add_weighted_edges_from(e32)

#plot
weight_labels=nx.get_edge_attributes(STRS2,'weight')
pos = nx.spring_layout(STRS2)
nx.draw(STRS2,pos,with_labels=True,)
nx.draw_networkx_edge_labels(STRS2,pos,edge_labels=weight_labels)
