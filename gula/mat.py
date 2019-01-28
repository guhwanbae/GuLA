# Author  : Gu-hwan Bae
# Date    : Sun Jan 28
# Summary : Modeling a matrix.

import gula.vec as gvec
import gula.util as gutil

class matrix:
    """
    Modeling a matrix as python class. It has tuple, in constructor as label,
    to represent indice of row and column domain. And matrix class represent
    a entries by dictionary. It can be represented by sparse matrix.
    """
    def __init__(self, label, func, zero=0):
        self.domain = label
        self.func = func
        self.zero = zero

    def getItem(self, key):
        return self.func[key] if key in self.func else self.zero

    def setItem(self, key, val):
        (row, col) = self.domain
        if key not in gutil.cartesianProduct(row, col):
            return None
        self.func[key] = val

    def entries(self, d, mode='row'):
        """
        Return entries of row vector or column set sorted by laxicogrhapical.
        Parameter 'd' is element of row or column set.
        mode : str{'row', 'col'} optional
            'row'
                The output is a row vector.
            'col'
                The output is a column vector.
        """
        (row, col) = self.domain
        if mode is 'row' and d in row:
            domain = gutil.cartesianProduct(set(d), sorted(col))
        elif mode is 'col' and d in col:
            domain = gutil.cartesianProduct(set(d), sorted(row))
        else:
            return None
        return [self.getItem(d) for d in domain]

    def row(self, r):
        """
        Return a row vector.
        Parameter 'r' is element of column set.
        """
        (row, col) = self.domain
        if r not in row:
            return None
        return gvec.vector(col, {c:self.func[(r,c)] for c in col if (r,c) in self.func})

    def col(self, c):
        """
        Return a column vector.
        Parameter 'c' is element of column set.
        """
        (row, col) = self.domain
        if c not in col:
            return None
        return gvec.vector(row, {r:self.func[(r,c)] for r in row if (r,c) in self.func})

    def __str__(mat):
        (row, col) = mat.domain
        row = sorted(row)
        col = sorted(col)
        indice = gutil.cartesianProduct(row, col)
        label = '    ' + ' '.join(col)
        for index in row:
            entries = mat.entries(index, mode='row')
            label = label + '\n'
            label = label + str(index) + ' | ' + ' '.join(str(elem) for elem in entries)
        return label

def eye(row):
    """
    Return a identical matrix.
    """
    if len(row) < 1:
        return None
    func = {(r,c):1 for (r,c) in gutil.cartesianProduct(row, row) if r is c}
    return matrix((row, row), func)
