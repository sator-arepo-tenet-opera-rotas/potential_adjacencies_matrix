import amgen_0.py
import amgen_1.py
import amgen_2_secondary_store.py
import amgen_2_test_stub.py # assume it already passed this phase

#define traveling salesman algorithm and apply it to the stores's #networks
tsp = nx.approximation.traveling_salesman_problem
tsp(STRS)


#apply TSP algorithm to the second stores's networks
tsp(STRS2)
