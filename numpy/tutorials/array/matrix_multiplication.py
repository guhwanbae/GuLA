import numpy as np

mat_x = np.array([[1, 2], [3, 4]])
mat_y = np.array([[5, 6], [7, 8]])

vec_v = np.array([9, 10])
vec_w = np.array([11, 12])

print("Matrix X = \n", mat_x)
print("Matrix Y = \n", mat_y)

print("Vector v = ", vec_v)
print("Vector w = ", vec_w)

# Inner product of vectors by using an instance method of array.
print("[Inner product] v dot w = ", vec_v.dot(vec_w))
# Or use the numpy module.
# np.dot(vec_v, vec_w)

# Product a matrix and vector.
# Note this! Vector v is treated as a column vector.
# Mat_x(2x2) * Vec_v(2x1)
print("[Product Matrix, Vector] X*v = ", mat_x.dot(vec_v))
# np.dot(mat_x, vec_v)

# Note this! Vector v is treated as a row vector.
# Vec_v(1x2) * Mat_x(2x2)
print("[Product Matrix, Vector] v*X = ", vec_v.dot(mat_x))
# Or use the numpy module.
# np.dot(vec_v, mat_x)

# Product matrices.
print("[Product matrices] X*Y = \n", mat_x.dot(mat_y))
# Or use the numpy module.
# np.dot(mat_x, mat_y)
print("[Product matrices] Y*X = \n", mat_y.dot(mat_x))
