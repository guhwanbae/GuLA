import numpy as np

point = np.array([0, 0, 1], dtype=np.float64)
print("Shape of vector p = ", point.shape)

# Translation matrix
t_mat = np.array([
    [1, 0, 0.25],
    [0, 1, 0.75],
    [0, 0, 1]], dtype=np.float64)
print("Shape of matrix T = ", t_mat.shape)

print("Translation matrix, T = \n", t_mat)
print("The homogeneous point, vector p = \n", point)

shifted_point = t_mat.dot(point)
print("The shifted point = \n", shifted_point)
