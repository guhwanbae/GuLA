import numpy as np

# Numpy choose the datatype as int64
x = np.array([1, 2])
print("array x = ", x, " datatype = ", x.dtype)

# Numpy choose the datatype as float64
y = np.array([1.0, 2.0])
print("array y = ", y, " datatype = ", y.dtype)

# Force initializing with a particular datatype
z = np.array([1, 2], dtype=np.float64)
print("array z = ", z, " datatype = ", z.dtype)

