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
    if type(u) is gvec.vector and type(v) is gvec.vector:
        if u.domain == v.domain:
            return sum([u.getItem(d) * v.getItem(d) for d in u.domain])
    elif type(u) is gmat.matrix and type(v) is gvec.vector:
        (R, C) = u.domain
        if C == v.domain:
            output = gvec.vector(R, {})
            for c in C:
                output = output + u.col(c) * v.getItem(c)
            return output
    elif type(u) is gmat.matrix and type(v) is gmat.matrix:
        (Ru, Cu) = u.domain
        (Rv, Cv) = v.domain
        if Cu == Rv:
            output = gmat.matrix((Ru, Cv), {})
            for cv in Cv:
                column_vec = dot(u, v.col(cv))
                output.addColumn(cv, column_vec)
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
    if type(arr) is np.ndarray:
        if arr.size is not 0 and type(arr.item(0)) is gf.GF2 :
            return arr

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
