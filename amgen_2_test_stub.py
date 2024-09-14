import amgen_0.py
import amgen_1.py
import amgen_2_secondary_store.py

#find shortest path from Store 2 to Store 5
nx.astar_path(STRS2,"store2","store5", weight='weight')
