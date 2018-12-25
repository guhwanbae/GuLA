import numpy as np

regular_mat = np.array([[1, 2], [3, 4]])
print("Regular matrix = \n", regular_mat)
print("The transposed matrix = \n", regular_mat.T)

# Note that taking the transpose of a vector(rank=1) does nothing.
vec = np.array([1, 2, 3])
print("Vector = ", vec)
print("The transpose vector = ", vec.T)
