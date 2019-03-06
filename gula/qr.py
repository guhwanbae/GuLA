# Author  : Gu-hwan Bae
# Summary : QR decoposition and its applications.

import numpy as np
import gula.orthogonal as gortho
import gula.triangular as gtriangular

def decomposition(A):
    '''
    Return a QR factorization, QR = A.
    Q is a column orthogonal matrix. And R is a upper triangular matrix.
    '''
    Q, R = gortho.orthonormalize(A)
    # If matrix A has row vectors are linear dependent, it can not be factorized.
    # Ohterwise Col A is linear independent, Col Q is same as Col A.
    if A.shape[1] != Q.shape[1]:
        return None
    return Q, R

def solve(A, b):
    '''
    Return a solution of a linear equation by using QR decomposition.
    If Col A is linear independent, the input matrix A can be factorized,
    QR = A.
    The linear equation representation, A * x = b, is same as QR * x = b.
    And transposed Q is inverse matrix of Q. So, R * x = Q.T * b.
    '''
    Q, R = decomposition(A)
    b_tilde = np.dot(Q.T, b)
    return gtriangular.backSubstitution(R, b_tilde)
