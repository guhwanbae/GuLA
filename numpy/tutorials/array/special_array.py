import numpy as np

# Make a matrix of all zeros.
zero_mat = np.zeros((2,2))
print("Zero matrix = \n", zero_mat)

# Make a matrix of all ones.
const_ones_mat = np.ones((3,2))
print("Ones = \n", const_ones_mat)

# Make a constant matrix.
const_mat = np.full((2,2), 7)
print("Constant matrix = \n", const_mat)

# Make a identity matrix.
eye_mat = np.eye(3)
print("Identical matrix(3x3) = \n", eye_mat)

# Make a matrix filled with random values.
rand_mat = np.random.random((2,2))
print("Random values matrix = \n", rand_mat)
