# Author  : Gu-hwan Bae
# Summary : Solving a equation by using triangular matrix properties.

import numpy as np
import gula.triangular as gtriangular

# Case I : Forward substitution
# Solving a linear system, R*b = x, with a lower triangular matrix R.

print('Forward substitution.')

R = np.array([[1, 0, 0],
              [2, 3, 0],
              [4, 5, 6]])
b = np.array([10, 40, 80])

x = gtriangular.forwardSubstitution(R, b)
print('R =\n', R)
print('b =', b)
print('x =', x)
print('R * x', np.dot(R, x))

print('-' * 20)

# Case II : Back substitution
# Solving a linear system, R*b = x, with a upper triangular matrix R.

print('Back substitution.')

R = np.array([[1, 2, 3],
              [0, 4, 5],
              [0, 0, 6]])
b = np.array([2, 3, 5])

x = gtriangular.backSubstitution(R, b)

print('R =\n', R)
print('b =', b)
print('x =', x)
print('R * x =', np.dot(R, x))