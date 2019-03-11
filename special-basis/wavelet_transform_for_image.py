# Author  : Gu-hwan Bae
# Summary : Wavelet transform for 2D signal analysis.

import gula.wavelet as gwavelet
import gula.image as gimage
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

# Case I : Wavelet transform for example 2D array.

data = np.array([[ 1,  2,  3, 4],
                 [ 5,  6,  7, 8],
                 [ 9, 10, 11, 12],
                 [13, 14, 15, 16]])
W = gwavelet.haar2d(data)
print('W =\n', W)

data_inv = gwavelet.haar2dinv(W)
print('inversed data =\n', data_inv)

# Case II : Wavelet transform for image analysis.

image = misc.face(gray=True)
image = gimage.padImage(image)

plt.figure('Original image')
plt.imshow(image)
plt.show()

'''
Gray scale image that intensity is 8bit can be damaged by overflow.
If you want to avoid this problem, use a wavelet transform with normalization.
'''
W = gwavelet.haar2d(image.astype('float64'))
plt.figure('Wavelet transform')
plt.imshow(W)
plt.show()

image_inv = gwavelet.haar2dinv(W)
plt.figure('Recovery')
plt.imshow(image_inv)
plt.show()

