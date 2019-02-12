# Author  : Gu-hwan Bae
# Date    : Sun Jan 28
# Summary : Utilities and operators for matrix and vector.

import numpy as np
import gula.vec as gvec
import gula.mat as gmat
import gula.galois as gf

def cartesianProduct(set_a, set_b):
    return [(a, b) for a in set_a for b in set_b]

def dot(u, v):
    """
    Return a dot product output between matrices and vectors.
    Specially, Multiplication between matrix and vector is represented by
    linear combination of column vectors of matrix that scalar multiplied
    by coressponding element of vector, v[c].
    """
    if isinstance(u, gvec.vector) and isinstance(v, gvec.vector):
        print('vec-vec')
        if u.domain is v.domain:
            return sum([u.getItem(d) * v.getItem(d) for d in u.domain])
    elif isinstance(u, gmat.matrix) and isinstance(v, gvec.vector):
        (row, col) = u.domain
        if col is v.domain:
            output = gvec.vector(row, {})
            for c in col:
                output = output + u.col(c) * v.getItem(c)
            return output
    return None

def listlist2mat(listlist):
    listlist = np.asarray(listlist)
    (row, col) = listlist.shape
    R = set(str(r) for r in range(row))
    C = set(str(c) for c in range(col))
    return gmat.matrix((R, C),
                       {(str(r), str(c)) : listlist[r][c] for r in range(row) for c in range(col)})

def asGF2(arr):
    """
    Return a numpy array that elements are converted to GF(2).
    """
    src = np.asarray(arr)
    ones_indice = (src == 1)
    output = np.full(src.shape, gf.GF2(0))
    output[ones_indice] = gf.GF2(1)
    return output

def gf2toint(gf2array):
    """
    Convert numpy array in GF(2) to a integer list.
    """
    return [1 if n == gf.GF2(1) else 0 for n in gf2array]

def str2bits(string):
    """
    Return a bit list decoded from utf-8 string.
    """
    mask = [1 << n for n in range(8)]
    bits = [1 if ord(s) & b else 0 for s in string for b in mask]
    return bits

def bits2str(bits):
    """
    Return a string encoded from a bit list.
    """
    B = np.asarray(bits).reshape(-1, 8)
    mask = np.array([1 << n for n in range(8)])
    return ''.join(chr(enc) for enc in sum((B*mask).T))
