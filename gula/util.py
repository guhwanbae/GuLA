# Author  : Gu-hwan Bae
# Date    : Sun Jan 28
# Summary : Utilities and operators for matrix and vector.

import gula.vec as gvec
import gula.mat as gmat

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