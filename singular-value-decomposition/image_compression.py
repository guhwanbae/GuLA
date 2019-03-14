# Author  : Gu-hwan Bae
# Summary : Image compression with SVD. And shows the result of compression
#           with diffrent ranks for reconstructed image.

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

image = misc.face(gray=True).T

u, s, v = np.linalg.svd(image)

rank = s.shape[0]
step = 5
k_rank = np.array([1, 2, 3, 5, 10, 20, 40, 80, 150, 400]).astype('int')

plt.figure('k-rank SVD')

print('Original(Rank = %d)' % rank)
plt.imshow(image.T)
plt.show()

# Show reconstructed image each rank.
for k in k_rank[-1::-1]:
    print('k-rank =', k)
    k_appr = np.dot(u[:,:k]*s[:k], v[:k,:])
    plt.imshow(k_appr.T)
    plt.show()
