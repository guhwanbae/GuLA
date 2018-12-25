import numpy as np

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)

print("Matrix x = \n", x)
print("Vector v = ", v)
# Note this! Matrix y has uninitialized elements!
# print("Matrix y = \n", y)
print("Shape of y = ", y.shape)

# 1. Add the vector v to each row of the matrix x with an explicit loop.
#    When matrices are very large, computing an explicit loop in python
#    could be slow.
for i in range(4) :
    y[i, :] = x[i, :] + v

print("Matrix y =\n", y)

# 2. Using a stacked copy of v.
vv = np.tile(v, (4, 1))
print("Stack 4 copies of vector v = \n", vv)
z = x + vv
print("Matrix z =\n", z)

# 3. Using a broadcasting.
#    Numpy broadcasting allows to perform this computation without
#    actually creating multiple copies of vector v.
# Add v to each row of x using broadcasting.
w = x + v
print("Matrix w =\n", w)
