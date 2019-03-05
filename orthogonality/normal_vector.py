# Author  : Gu-hwan Bae
# Summary : Find a normal vector perpendicular to the given plane.
#           Find a basis for orthogonal complement.
#           Find a set of orthonormalized vectors.

import gula.orthogonal as gortho
import numpy as np

# Case I : Find a normal vector n perpendicular to Span {V}.

V = np.array([[8, -2, 2],
              [0, 3, 3]]).T

# Arbitrary vector b not onto the plane, Span{V}.
b = np.array([1, -2, 3])
n = gortho.normal(b, V)
print('Normal vector n =', n)


# Case II : Find a basis for orthogonal complement.
# U is a sub-space of W.

U = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0]]).T

W = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]]).T

# B is a basis for orthogonal complement.
B = gortho.orthogonalComplement(U, W)
print('Basis for sub-space U =\n', U)
print('Basis for vector space W =\n', W)
print('Basis for orthogonal complement B =\n', B)



# Case III : Find a set of orthonormalized vectors.

V = np.array([[1, 2, 3],
              [0, 4, 5],
              [0, 0, 6]]).T

Q = gortho.orthonormalize(V)
print('Orthonormalized Q =\n', Q)

'''
The matrix Q is a column orthogonal matrix. And its column vectors are q1, ... qn.

Z = [q1 | ... | qn].T * [q1 | ... | qn]

(qk_star is translarted qk vector.)

The entry of matrix Z is
 Zii = qi_star * qi = norm(qi) = 1.0 (normalized)
 Zij = qi_star * qj = 0 (i != j, qi_star and qj are pendicular.)

So, Z is an identity matrix.

Q.T is an inverse matrix of Q. (Q.T * Q = I)
'''
Z = np.dot(Q.T, Q)
Z[np.abs(Z) < 1e-15] = 0
print('Q.T * Q = Z =\n', Z)

X = np.dot(Q, Q.T)
X[np.abs(X) < 1e-15] = 0
print('Q * Q.T = X =\n', X)
