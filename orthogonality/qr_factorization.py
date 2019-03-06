# Author  : Gu-hwan Bae
# Summary : Find the QR factorization and solving a linear equation.

import numpy as np
import gula.qr as gQR

# Case I : QR decomposition. Find the QR factorization, QR = A.

print('Find the QR factorization.')

# Col A is linear independent.
A = np.array([[1, 1, 0],
              [1, 1, 1],
              [0, 1, 1]])

Q, R = gQR.decomposition(A)
print('A =\n', A)
print('Q =\n', Q)
print('R =\n', R)
print('QR =\n', np.dot(Q, R))


print('-' * 20)

# Case II : Solving a linear equation with a coefficient matrix A which has
# linearly independent column vectors.

print('Solving a linear equation.')

A = np.array([[1, 1, 0],
              [1, 1, 1],
              [0, 1, 1]])
b = np.array([2, 3, 5])

x = gQR.solve(A, b)

print('A =\n', A)
print('b =', b)
print('x =', x)
print('A*x =', np.dot(A, x))
