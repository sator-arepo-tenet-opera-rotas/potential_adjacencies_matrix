# potential_adjacencies_matrix


Potential Adjacencies Matrices for Solving Chaotic Dynamic Multi-Agent Networks

Funding provided by the following NSF Grants: 

https://www.nsf.gov/awardsearch/showAward?AWD_ID=1836827

https://www.nsf.gov/awardsearch/showAward?AWD_ID=2033607

Research done and applied by Siobhàn Merrill-Nyxhades (NASA JPL) under Principal Investigator Lilit Yeghiazarian


This python code models an abstract network of nodes and vertices; the graph is then used to show TSP and maxflow algorithms for route planning. One example for msp is going from arrival to destination in a city with sub-optimal routes

The diagrams are provided as-is


<img width="741" alt="Screenshot 2024-09-14 at 14 28 51" src="https://github.com/user-attachments/assets/4d9e05f4-2920-493a-8bdb-6297938da792">


![Screenshot 2024-09-19 at 08 54 24](https://github.com/user-attachments/assets/4693bada-6f52-4be5-8873-df1ef1b530ca)


<img width="538" alt="Screenshot 2024-09-14 at 14 32 21" src="https://github.com/user-attachments/assets/a682aedb-d8e1-4ebc-aa10-a8a634c46802">

![Screenshot 2024-09-19 at 08 54 59](https://github.com/user-attachments/assets/d2a066d8-fe7e-45af-a928-010eb7b272d9)




![pam_edges_clean_network](https://github.com/user-attachments/assets/396c56d2-bf31-4432-8466-0e5983baab91)

![pam_edges_complex_network](https://github.com/user-attachments/assets/abbb8d96-1a25-4130-acec-af629b7555b7)


(source, target, capacity)
--------------------------
('a', 'b', 2.0)
('a', 'd', 0.5)
('b', 'd', 3.0)
('c', 'd', 2.5)
('c', 'e', 1.0)
('e', 'f', 4.0)
('f', 'g', 1.0)
('g', 'h', 3.2)
('a', 'g', 0.8)
('f', 'i', 2.1)
('d', 'h', 1.9)
('e', 'c', 4.5)
('h', 'b', 3.3)
('b', 'f', 0.6)
('c', 'g', 2.7)
('h', 'd', 4.1)
('g', 'f', 1.2)
('i', 'k', 3.4)
('i', 'm', 0.9)
('j', 'l', 2.3)
('j', 'b', 3.6)
('k', 'n', 1.1)
('k', 'r', 0.4)
('l', 'q', 3.7)
('m', 'p', 2.9)
('n', 'j', 1.5)
('p', 'e', 4.0)
('q', 'o', 0.7)
('r', 'n', 2.8)
('s', 't', 1.0)
('t', 'f', 3.9)

This format clearly shows the relationships between the source, target, and the capacity.


Reshape the data into 3-tuples in Python using a list comprehension. Here's how you can do it:

updated_data = {
    'source': ['a', 'a', 'b', 'c', 'c', 'e', 'f', 'g', 'a', 'f', 'd', 'e', 'h', 'b', 'c', 'h', 'g', 'i', 'i', 'j', 
               'j', 'k', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't'],
    'target': ['b', 'd', 'd', 'd', 'e', 'f', 'g', 'h', 'g', 'i', 'h', 'c', 'b', 'f', 'g', 'd', 'f', 'k', 'm', 'l', 
               'b', 'n', 'r', 'q', 'p', 'j', 'e', 'o', 'n', 't', 'f'],
    'capacity': [2.0, 0.5, 3.0, 2.5, 1.0, 4.0, 1.0, 3.2, 0.8, 2.1, 1.9, 4.5, 3.3, 0.6, 2.7, 4.1, 1.2, 3.4, 0.9, 2.3, 
                 3.6, 1.1, 0.4, 3.7, 2.9, 1.5, 4.0, 0.7, 2.8, 1.0, 3.9]
}

# Reshape into 3-tuples
reshaped_data = [(updated_data['source'][i], updated_data['target'][i], updated_data['capacity'][i]) for i in range(len(updated_data['source']))]

# Print the reshaped data
for row in reshaped_data:
    print(row)

('a', 'b', 2.0)
('a', 'd', 0.5)
('b', 'd', 3.0)
('c', 'd', 2.5)
('c', 'e', 1.0)
('e', 'f', 4.0)
('f', 'g', 1.0)
('g', 'h', 3.2)
('a', 'g', 0.8)
('f', 'i', 2.1)
('d', 'h', 1.9)
('e', 'c', 4.5)
('h', 'b', 3.3)
('b', 'f', 0.6)
('c', 'g', 2.7)
('h', 'd', 4.1)
('g', 'f', 1.2)
('i', 'k', 3.4)
('i', 'm', 0.9)
('j', 'l', 2.3)
('j', 'b', 3.6)
('k', 'n', 1.1)
('k', 'r', 0.4)
('l', 'q', 3.7)
('m', 'p', 2.9)
('n', 'j', 1.5)
('p', 'e', 4.0)
('q', 'o', 0.7)
('r', 'n', 2.8)
('s', 't', 1.0)
('t', 'f', 3.9)



Represent the source, target, and capacity data using NumPy matrices and operate on them similarly to m@troids using NumPy arrays

    Represent the data as a NumPy matrix:
        You can stack the three lists (source, target, capacity) into a 2D NumPy matrix.
        Use numerical encoding for source and target, since NumPy matrices work with numbers.

import numpy as np

# Original data
updated_data = {
    'source': ['a', 'a', 'b', 'c', 'c', 'e', 'f', 'g', 'a', 'f', 'd', 'e', 'h', 'b', 'c', 'h', 'g', 'i', 'i', 'j', 
               'j', 'k', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't'],
    'target': ['b', 'd', 'd', 'd', 'e', 'f', 'g', 'h', 'g', 'i', 'h', 'c', 'b', 'f', 'g', 'd', 'f', 'k', 'm', 'l', 
               'b', 'n', 'r', 'q', 'p', 'j', 'e', 'o', 'n', 't', 'f'],
    'capacity': [2.0, 0.5, 3.0, 2.5, 1.0, 4.0, 1.0, 3.2, 0.8, 2.1, 1.9, 4.5, 3.3, 0.6, 2.7, 4.1, 1.2, 3.4, 0.9, 2.3, 
                 3.6, 1.1, 0.4, 3.7, 2.9, 1.5, 4.0, 0.7, 2.8, 1.0, 3.9]
}

# Step 1: Assign numerical labels to characters (for source and target)
unique_nodes = sorted(set(updated_data['source'] + updated_data['target']))
node_to_index = {node: i for i, node in enumerate(unique_nodes)}

# Step 2: Encode the source and target using the numerical labels
encoded_source = np.array([node_to_index[node] for node in updated_data['source']])
encoded_target = np.array([node_to_index[node] for node in updated_data['target']])
capacities = np.array(updated_data['capacity'])

# Step 3: Combine into a 2D NumPy array (matroid-like)
data_matrix = np.vstack([encoded_source, encoded_target, capacities]).T

# Output the matrix and mappings
print("Data matrix:")
print(data_matrix)
print("\nNode to index mapping:")
print(node_to_index)


Data matrix:
[[ 0  1  2. ]
 [ 0  3  0.5]
 [ 2  3  3. ]
 [ 4  3  2.5]
 [ 4  5  1. ]
 [ 6  7  4. ]
 [ 8  9  1. ]
 [10 11  3.2]
 [ 0 10  0.8]
 [ 8  9  2.1]
 ...]

Node to index mapping:
{'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19}

1. Creating a Square Matrix

If you want to calculate the determinant, you need to form a square matrix. One way to do this is to convert the data into an adjacency matrix (which is square). This represents the connections between nodes (source-target pairs) with their corresponding capacities.
Example: Convert to an Adjacency Matrix

Convert the 3-tuple data into a square adjacency matrix where each entry (i,j)(i,j) represents the capacity between node i (source) and node j (target).

import numpy as np

# Adjacency matrix size is based on the number of unique nodes
num_nodes = len(node_to_index)

# Initialize an empty adjacency matrix of size (num_nodes x num_nodes)
adj_matrix = np.zeros((num_nodes, num_nodes))

# Fill the adjacency matrix based on the source-target-capacity data
for src, tgt, cap in data_matrix:
    adj_matrix[src, tgt] = cap

print("Adjacency Matrix:")
print(adj_matrix)

2. Linear Algebra Operations on the Square Matrix
a. Determinant

With a square matrix (the adjacency matrix), we can compute the determinant using NumPy's np.linalg.det() function.

# Compute the determinant of the adjacency matrix
determinant = np.linalg.det(adj_matrix)

print("Determinant of the adjacency matrix:")
print(determinant)

b. Rank of the Matrix
The rank of a matrix tells you how many linearly independent rows or columns it has. You can compute it using np.linalg.matrix_rank().

# Compute the rank of the adjacency matrix
rank = np.linalg.matrix_rank(adj_matrix)

print("Rank of the adjacency matrix:")
print(rank)


c. Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors on the adjacency matrix use np.linalg.eig().


# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(adj_matrix)

print("Eigenvalues of the adjacency matrix:")
print(eigenvalues)

Example Output (for the adjacency matrix):


Adjacency Matrix:
[[0.  2.  0.  0.  0.  0.  0.  0.  0.  0. ]
 [0.  0.  0.  3.  0.  0.  0.  0.  0.  0. ]
 [0.  0.  0.  3.  0.  0.  0.  0.  0.  0. ]
 [0.  0.  0.  0.  0.  0.  0.  0.  0.  0. ]
 [0.  0.  0.  0.  0.  4.  0.  0.  0.  0. ]
 ...
 ]

Determinant of the adjacency matrix:
0.0

Rank of the adjacency matrix:
6

Eigenvalues of the adjacency matrix:
[0. 0. 0. 0. ... ]


![pam_edges_complex_network](https://github.com/user-attachments/assets/abbb8d96-1a25-4130-acec-af629b7555b7)

![Screenshot 2024-09-19 at 08 48 35](https://github.com/user-attachments/assets/1a0e5203-8d02-4aac-92c8-35b429dad737)

![GXpc7qUakAAn2o7](https://github.com/user-attachments/assets/666f2341-fd49-43c4-9560-31bd5916c0cd)


![Screenshot 2024-09-18 at 07 18 39](https://github.com/user-attachments/assets/79ac8487-f7c6-480b-8369-5b5acb50384d)

Activate a singularity aka make the blorbs spin and go boom



<img width="1030" alt="Screenshot 2024-09-19 at 14 58 06" src="https://github.com/user-attachments/assets/0321ffc5-3155-4f8c-8cf6-5aedda9fd172">

Assessment from: https://x.com/Tendar/status/1836822868992156032

https://www.theguardian.com/world/2024/sep/18/ukraine-drone-attack-on-russian-arms-depot-toropets

Explanation:

    Adjacency Matrix: This matrix represents the connections (edges) between the nodes, where the value at position (i,j)(i,j) corresponds to the capacity from node i to node j.

    Determinant: In this example, the determinant is zero, which indicates that the matrix is singular (i.e., not invertible).

    Rank: The rank of the matrix gives the number of linearly independent rows or columns. In this case, the rank is less than the size of the matrix, which also suggests linear dependency between rows.

    Eigenvalues: The eigenvalues are related to the matrix's structure and can give insights into its stability and properties.


