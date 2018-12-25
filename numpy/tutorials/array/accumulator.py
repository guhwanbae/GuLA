import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Matrix = \n", mat)

print("Sum of all elements = ", np.sum(mat))
print("Sum of each column = ", np.sum(mat, axis=0))
print("Sum of each row = ", np.sum(mat, axis=1))
