# Author  : Gu-hwan Bae
# Date    : Mon Feb 11, 2019
# Summary : Hamming code functionalities.

import numpy as np
import gula.galois as gf
import gula.util as gutil

def getGenerator():
    """
    Return a generator matrix in GF(2).
    """
    G = gutil.asGF2([[1, 1, 0, 1],
                     [1, 0, 1, 1],
                     [1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
    return G 

def getDecoder():
    """
    Return a decoder matrix in GF(2).
    """
    R = gutil.asGF2([[0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 1]])
    return R

def getParityChecker():
    """
    Return a parity check matrix in GF(2).
    """
    H = gutil.asGF2([[1, 0, 1, 0, 1, 0, 1],
                     [0, 1, 1, 0, 0, 1, 1],
                     [0, 0, 0, 1, 1, 1, 1]])
    return H

def getErrorWord(error_ratio = 0.5):
    """
    Generate a error vector according to uniform probability distribution, (error_ratio, 1 - error_ratio). 
    """
    e = np.full(7, gf.GF2(0))
    if np.random.rand() > (1 - error_ratio):
        error_index = np.random.randint(7)
        e[error_index] = gf.GF2(1)
    return e

def findErrorWord(c):
    """
    If error exist, return a 7-vector in GF(2) which error occurred entry is 1.
    Otherwise, return a zero 7-vector.
    """
    H = getParityChecker()
    # Parity error vector, pe
    pe = np.dot(H, c)
    index = -1
    for n in range(3):
        if pe[n] == gf.GF2(1):
            index = index + 2**n
    e = np.full(7, gf.GF2(0))
    if index == -1:
        return e
    else:
        e[index] = gf.GF2(1)
        return e

def findErrorMatrix(mat_code_words):
    """
    Return a matrix which column is a noised code word.
    The input parameter is matrix that column is error word as 7-vector.
    """
    S = np.asarray(mat_code_words)
    (nrow , ncol) = S.shape
    return np.array([findErrorWord(S[:,c]) for c in range(ncol)]).T

def bits2matrix(bits, nrow = 4):
    return gutil.asGF2(bits).reshape(-1, nrow).T

def matrix2bits(matrix, order='F'):
    """
    Return bit list flatten in column major.
    Parameter oder 'F' means 'Fotran style', column major.
    """
    return gutil.gf2toint(np.asarray(matrix).flatten(order))