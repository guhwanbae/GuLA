# Author  : Gu-hwan Bae
# Summary : Wavelet transform for signal analysis.

import numpy as np

def __haar1d__(data):
    '''
    Transform given data to the unnormalized 1D haar wavelet coefficients.
    '''
    n = data.shape[0]
    s = n
    mean = data
    w = np.zeros(n)
    while s > 1:
        s = s // 2
        even = mean[::2]
        odd = mean[1::2]
        w[s:s*2] = even-odd
        mean = (even+odd) / 2
    w[0] = mean[0]
    return w

def haar(data):
    '''
    Transform given data to the unnormalized haar wavelet coefficients.
    '''
    data = np.asarray(data)
    if data.shape[0] % 2 != 0:
        return None
    return __haar1d__(data)

def haar2d(data):
    '''
    Transform given data to the unnormalized 2D haar wavelet coefficients.
    '''
    (nrows, ncols) = data.shape
    W = np.zeros(data.shape)
    for r in range(nrows):
        W[r] = haar(data[r])
    for c in range(ncols):
        W[:,c] = haar(W[:,c])
    return W

def haar2dinv(W):
    '''
    Inverse unnormalized wavelet coefficients for 2D haar basis
    to the original domain.
    '''
    (nrows, ncols) = W.shape
    data = np.zeros(W.shape)
    for c in range(ncols):
        data[:,c] = gwavelet.haarinv(W[:,c])
    for r in range(nrows):
        data[r] = gwavelet.haarinv(data[r])
    return data

def __haar1d_inverse__(w):
    '''
    Inverse unnormalized wavelet coefficients for 1D haar basis
    to the original domain.
    '''
    n = w.shape[0]
    s = 1
    data = np.zeros(n)
    data[0] = w[0]
    while s < n:
        mean = data[:s]
        diff = w[s:s*2]
        (data[:s*2:2], data[1:s*2:2]) = (2*mean+diff)/2, (2*mean-diff)/2
        s *= 2
    return data

def haarinv(w):
    '''
    Inverse unnormalized wavelet coefficients for haar basis
    to the original domain data.
    '''
    if w.shape[0] % 2 != 0:
        return None
    return __haar1d_inverse__(w)

def suppress(w, threshold):
    '''
    Set entries less than threshold to zero.
    '''
    truncated = np.abs(w) < threshold
    suppressed = w.copy()
    suppressed[truncated] = 0
    return suppressed 

def sparsity(w):
    '''
    Return a sparsity of given coefficients.
    '''
    return 1 - np.count_nonzero(w)/w.shape[0]

def normalizeHaar(w):
    '''
    Return a normalized haar wavelet coefficients.
    '''
    n = w.shape[0]
    s = 1
    w[0] *= np.sqrt(n)
    while s < n:
        w[s:s*2] *= np.sqrt(n/(4*s))
        s *= 2
    return w

def unnormalizedHaar(w):
    '''
    Return a unnormalized haar wavelet coefficients.
    '''
    n = w.shape[0]
    s = 1
    w[0] /= np.sqrt(n)
    while s < n:
        w[s:s*2] /= np.sqrt(n/(4*s))
        s *= 2
    return w
