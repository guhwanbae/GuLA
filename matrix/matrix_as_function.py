# Author  : Gu-hwan Bae
# Date    : Wed Jan 30
# Summary : Matrix is a function which maps the column field to the
#           row field. Column field is a domain of this function and
#           row field is a codomain.

import gula.vec as gvec
import gula.mat as gmat
import gula.util as gutil

"""
R is row label of matrix.
C is column label of matrix.
"""
R = {'a', 'b'}
C = {'#', '@', '?'}

A = gmat.matrix((R, C), {d:i+1 for i,d in enumerate(gutil.cartesianProduct(R, C))})
print('Matrix A=')
print(A)

x = gvec.vector(C, {c:1 for c in C})
print('Vector x=')
print(x)

"""
Set(Label) C is a domain of function.
Set R is a co-domain of function.
So, RxC matrix is model of (C->R) function.
"""

print('Dot product, A*x=b')
print('Vector b=')
print(gutil.dot(A, x))

"""
(x->M*x) is function of (C->R).
The domain of vector b is range of above function.
"""

