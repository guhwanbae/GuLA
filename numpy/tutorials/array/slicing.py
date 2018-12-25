import numpy as np

# Make a matrix(rank=2, shape=(3x4))
mat = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Matrix = \n", mat)

# Rank 1 view of the first row of matrix.
row_r1 = mat[0, :]
# Rank 2 view of the first row of matrix.
row_r2 = mat[0:1, :]

# Mixing integer indexing with slices yields an array of lower rank.
print("row_r1 = ", row_r1, ", shape = ", row_r1.shape)
# While using 'only slices' yields an array of 'the same rank' as the original.
print("row_r2 = ", row_r2, ", shape = ", row_r2.shape)
