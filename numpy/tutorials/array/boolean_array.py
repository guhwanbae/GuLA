import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Matrix(%s) = \n" % mat.dtype, mat)

# Find the even element, and returns a numpy array of boolean types,
# same shape as mat. Each element represents whether that elements of
# mat is even number, mat % 2 == 0. 
print("Find the even number.")
even_idx = (mat % 2 == 0)
print("Boolean matrix(%s) = \n" % even_idx.dtype, even_idx)

# Use boolean array indexing to construct a rank 1 array.
even_nums = mat[even_idx]
print("Even numbers = ", even_nums)

odd_idx = np.logical_not(even_idx)
odd_nums = mat[odd_idx]
print("Odd numbers = ", odd_nums)
