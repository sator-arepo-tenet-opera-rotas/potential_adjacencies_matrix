import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("edges.csv")

# Sample CSV data (otherwise use edges.csv)
#data = {
#    'source': ['a', 'a', 'b', 'c', 'c', 'e', 'f'],
#    'target': ['b', 'd', 'd', 'd', 'e', 'f', 'g'],
#    'capacity': [2.0, 0.5, 3.0, 2.5, 1.0, 4.0, 1.0]
#}

# Create a directed graph
G1 = nx.DiGraph()

# Add edges and capacities from CSV
for index, row in df.iterrows():
    G1.add_edge(row['source'], row['target'], capacity=row['capacity'])

# Get edge capacities for plotting
capacity_labels = nx.get_edge_attributes(G1, 'capacity')

# Plot the graph
pos = nx.spring_layout(G1)
nx.draw(G1, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(G1, pos, edge_labels=capacity_labels)

# Find minimum cut between residential area 'a' and downtown 'g'
partition = nx.minimum_cut(G1, "a", "g")
print("Minimum Cut:", partition)

# Show plot
plt.show()
