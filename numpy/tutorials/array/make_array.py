import numpy as np

# Make a (rank=1) array.
arr = np.array([1, 2, 3])
print(type(arr))
print(arr.shape)
print(arr)

for idx in range(3):
    print("array[%d] = %d" % (idx,arr[idx]))

# Make a (rank=2) array.
mat = np.array([[1, 2, 3],
                [4, 5, 6]])
print(type(mat))
print(mat.shape)
print(mat)
