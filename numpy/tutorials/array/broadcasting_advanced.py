import numpy as np

v = np.array([1, 2, 3])
w = np.array([4, 5])

# Compute outer product.
# First, reshape v to be a column vector.
# Vector w is treated as a row vector.

# Outer product, (3x1) * (1x2)
#  [1]           [4   5]
#  [2] * [4 5] = [8  10]
#  [3]           [12 15]
mat = np.reshape(v, (3, 1)) * w
print("Outer product = \n", mat)

# Add a vector v to each row of a matrix x.
x = np.array([[1, 2, 3],
              [4, 5, 6]])
# Shape of x = (2, 3) and Shape of v (3,)
n = x + v
print("Matrix N = \n", n)

# 1. Add a vector w to each column of a matrix x.
# First, transpose x then it has shape (3, 2) and can be broadcast
# with w that has shape (2,). And transepose a result yields the final
# result of shape, (2, 3).
m = (x.T + w).T
print("Matrix M = \n", m)
print("Shape of M = ", m.shape)

# 2. Or, Reshape w to be a column vector of shape (2, 1).
# And then, it can be broadcast directly with matrix x.
s = x + np.reshape(w, (2, 1))
print("Matrix S = \n", s)
print("Shape of S = ", s.shape)
