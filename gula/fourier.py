# Author  : Gu-hwan Bae
# Summary : Fourier transform for 1D signals.

import numpy as np

def __dft__(s, coef=-2j):
    n = s.shape[0]
    if n % 2 != 0:
        return None
    exponents = np.arange(n)
    E = exponents * exponents[:,None]
    W = np.exp((coef * np.pi * E) / n)
    return np.dot(W, s)

def __fft__(s, coef=-2j):
    n = s.shape[0]
    if n < 32 :
        return __dft__(s, coef)
    s_even = __fft__(s[::2], coef)
    s_odd = __fft__(s[1::2], coef)
    w = np.exp((coef*np.pi * np.arange(n)) / n)
    s_first = s_even + w[:n//2] * s_odd
    s_last = s_even + w[n//2:] * s_odd
    return np.concatenate((s_first, s_last), axis=None)

def dft(s):
    s = np.asarray(s)
    n = s.shape[0]
    if n % 2 != 0:
        return None
    return __dft__(s, -2j) / np.sqrt(n)

def dftinv(s):
    s = np.asarray(s)
    n = s.shape[0]
    if n % 2 != 0:
        return None
    return __dft__(s, 2j) / np.sqrt(n)

def fft(s):
    s = np.asarray(s)
    n = s.shape[0]
    if n % 2 != 0:
        return None
    return __fft__(s, -2j) / np.sqrt(n)

def fftinv(s):
    s = np.asarray(s)
    n = s.shape[0]
    if n % 2 != 0:
        return None
    return __fft__(s, 2j) / np.sqrt(n)
