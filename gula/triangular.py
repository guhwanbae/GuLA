# Author  : Gu-hwan Bae
# Summary : Applications by using a triangular matrix.

import numpy as np

def forwardSubstitution(R, b):
    '''
    Return a solution of a linear system, R * x = b,
    with a lower triangular matrix R.
    '''
    (nrows, ncols) = R.shape
    x = np.zeros(ncols)
    for i,r in enumerate(R):
        diag = r[i]
        diff = np.dot(x[:i], r[:i])
        x[i] = (b[i] - diff) / diag
    return x

def backSubstitution(R, b):
    '''
    Return a solution of a linear system, R * x = b,
    with upper triangular matrix R.
    '''
    # Flip the matrix R to make lower triangular form. 
    x = forwardSubstitution(R[::-1,::-1], b[::-1])
    return x[::-1]

def solve(R, b, mode='upper'):
    '''
    Return a solution of a linear system, R * x = b,
    with a triangular matrix R.
    '''
    if mode == 'upper':
        return backSubstitution(R, b)
    else:
        return forwardSubstitution(R, b)
