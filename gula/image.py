# Author  : Gu-hwan Bae
# Summary : Miscellaneous utilities for image handling.

import numpy as np
import gula.util as gutil

def getPadding(length):
    '''
    Return a padding if lenght is not power of two.
    '''
    if gutil.isPowerOfTwo(length) == True:
        return 0
    exponent = int(np.log2(length) + 1)
    return (2**exponent) - length

def padImage(image):
    '''
    Return a padded image with zeros.
    '''
    (height, width) = image.shape
    padding = ((0, getPadding(height)), (0, getPadding(width)))
    return np.pad(image, padding, mode='constant')

