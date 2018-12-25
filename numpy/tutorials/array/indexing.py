import numpy as np

# Create a matrix(rank=2, shape=(3x4))
mat = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print("Matrix = \n", mat)

# Use slicing to pull out the subarray.
# Get the first 2 rows and colum #2 and #3.
sub = mat[:2, 1:3]
print("Sub array of above matrix = \n", sub)

element = mat[0, 1]
print("Element(row #1, column #2) = ", element)

# Modify the element.
mat[0, 1] = -5
print("Modify the element as -5")

# Sub array is a reference handle('view') of the original matrix.
print("Matrix = \n", mat)
print("Sub array = \n", sub)

sub[0, 0] = -7
print("Modify the element of sub array.")
print("Matrix = \n", mat)
print("Sub array = \n", sub)
