# Author  : Gu-hwan Bae
# Date    : Sun Jan 27
# Summary : Matrix modeling, and its own operations, utilities.

def cartesianProduct(set_a, set_b):
    return [(a, b) for a in set_a for b in set_b]

class Matrix:
    """
    Modeling a matrix as python class. It has tuple, in constructor as label,
    to represent indice of row and column domain. And matrix class represent
    a entries by dictionary. It can be represented by sparse matrix.
    """
    def __init__(self, label, func):
        self.domain = label
        self.func = func

    def getItem(self, key):
        return self.func[key] if key in self.func else 0

    def setItem(self, key, value):
        (rows, cols) = self.domain
        indice = cartesianProduct(rows, cols)
        if key not in indices:
            return None
        self.func[key] = value

    def row(self, index):
        """
        Return entries of row vector.
        """
        (rows, cols) = self.domain
        if index not in rows:
            return []
        domain = cartesianProduct(set(index), cols)
        entries = [self.getItem(key) for key in domain]
        return entries

    def col(self, index):
        """
        Return entries of column vector.
        """
        (rows, cols) = self.domain
        if index not in cols:
            return []
        domain = cartesianProduct(rows, set(index))
        entries = [self.getItem(key) for key in domain]
        return entries

    def __str__(mat):
        (rows, cols) = mat.domain
        rows = sorted(rows)
        cols = sorted(cols)
        indice = cartesianProduct(rows, cols)
        label = '    ' + ' '.join(cols)
        for index in rows:
            entries = mat.row(index)
            label = label + '\n'
            label = label + str(index) + ' | ' + ' '.join(str(elem) for elem in entries)
        return label

def eye(indices):
    """
    Return a identical matrix.
    """
    n = len(indices)
    if n < 1:
        return None
    func = {key:1 for key in cartesianProduct(indices, indices) if key[0] is key[1]}
    return Matrix((indices, indices), func)
