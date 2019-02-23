# Author  : Gu-hwan Bae
# Summary : Get a row echelon form.

import gula.solve as gsolve
import numpy as np

# Case I
# All rows are linear independent. rank(M) = 3, null(M) = 0
M = np.array([[1, 2, 3],
              [1, 2, 4],
              [3, 7, 4]])

G = gsolve.gaussian.getRowEchelonForm(M)

# Matrix G has three basis.
print('>> Echelon form matrix =\n', G)

# Case II
# First and second row are linear dependent. rank(M) = 2, null(M) = 1
M = np.array([[1, 2, 4],
              [1, 2, 4],
              [3, 7, 4]])

G = gsolve.gaussian.getRowEchelonForm(M)

# Matrix G has two basis.
print('>> Echelon form matrix =\n', G)

# Case III
# Rows are standart generator of R3 field. rank(M) = 3, null(M) = 0
M = np.array([[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]])

G = gsolve.gaussian.getRowEchelonForm(M)

# Matrix G has three basis.
print('>> Echelon form matrix =\n', G)

# Case IV
# All rows are linear are linear dependent. rank(M) = 1, null(M) = 2
M = np.array([[2, 2, 2],
              [4, 4, 4],
              [6, 6, 6]])

G = gsolve.gaussian.getRowEchelonForm(M)

# Matrix G has three basis.
print('>> Echelon form matrix =\n', G)
