# Author  : Gu-hwan Bae
# Summary : Modeling orthogonal properties in linear space.

import numpy as np

def projectionAlong(b, v):
    '''
    Return a coefficient of orthogonal projection of b onto v.
    '''
    sigma = (np.dot(b,v)/np.dot(v,v)) if np.dot(v,v) > 1e-20 else 0
    return sigma

def projectionOrthogonal(b, V):
    '''
    Return a vector orthogonalized to column vectors in matrix V.
    The column vectors of input matrix V are linear independent each other.
    The output vector sigma represent a linear combination coefficient
    of column vectors of V and reference vector b.
    b = [v1 | ... | vn | h] * sigma
    '''
    h = b
    (nrows, ncols) = V.shape
    sigma = np.zeros(ncols+1)
    if sigma.size > 0:
        sigma[-1] = 1.0
    for i,v in enumerate(V.T):
        sigma[i] = projectionAlong(h, v)
        h = h - sigma[i]*v
    return h, sigma

def orthogonalize(V):
    '''
    Return a matrix that column is a orthogonalized vector each other.
    The column vectors of input matrix V are generator of Span{V}.
    The output matrix H has null column vector when V has linear dependent vectors.
    The output matrix S is a transform matrix.
    V = H*S.
    '''
    (nrows, ncols) = V.shape
    H = np.zeros(V.shape)
    S = np.zeros((ncols, ncols))
    for i,v in enumerate(V.T):
        h, sigma = projectionOrthogonal(v, H[:,:i])
        H[:,i] = h
        S[:len(sigma),i] += sigma
    return H, S

def findSubsetBasis(V):
    '''
    Return a matrix that column is a basis. The parameter V is a set of generators.
    '''
    return np.array([h for h in orthogonalize(V) if np.linalg.norm(h) > 1e-20])
