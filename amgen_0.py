
#import packages
import networkx as nx

#create the Stores network
STRS = nx.Graph()
STRS.add_nodes_from(["store1","store2","store3","store4","store5"])

#define weighted ebunches, which represent lists of edges
e1 = [("store1","store2",2),("store1","store3",2.4),
    ("store1","store4",3),("store1","store5",3)]

e2 = [("store2","store3",3.7),("store2","store4",1.4),
    ("store2","store5",4.3)]

e3 = [("store3","store4",4.9),("store3","store5",0.9),
    ("store4","store5",5.4)]

#add edges
STRS.add_weighted_edges_from(e1)
STRS.add_weighted_edges_from(e2)
STRS.add_weighted_edges_from(e3)

#plot
weight_labels=nx.get_edge_attributes(STRS,'weight')
pos = nx.spring_layout(STRS)
nx.draw(STRS,pos,with_labels=True,)

nx.draw_networkx_edge_labels(STRS, pos,edge_labels=weight_labels)
