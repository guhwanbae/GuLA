# Author  : Gu-hwan Bae
# Date    : Sun Jan 27
# Summary : Test a matrix modeling class and its utilities.

import gula.mat as gmat
import gula.vec as gvec
import gula.util as gutil

M = gmat.matrix(({'a','b'},{'@','#'}),
                {('a','@'):1,
                 ('a','#'):2,
                 ('b','@'):3,
                 ('b','#'):4})

print('Matrix, M, 2x2')
print(M)

I = gmat.eye({'x','y','z'})
print('Identical matrix, I, 3x3')
print(I)

print('Row vectors of Matrix M')
(row, col) = M.domain
for r in row:
    print('Row vector, r =', r)
    print(M.row(r))
for c in col:
    print('Column vector, c =', c)
    print(M.col(c))

A = gmat.matrix(({'x', 'y'}, {'a', 'b', 'c'}),
                {('x','a'):1.,
                 ('x','b'):2.,
                 ('x','c'):3.,
                 ('y','a'):4.,
                 ('y','b'):5.,
                 ('y','c'):6.})
print('2x3 Matrix, A')
print(A)

(row, col) = A.domain
x = gvec.vector(col, {'a':.1, 'b':.2, 'c':.3})
print('R-3 Vector, x')
print(x)

b = gutil.dot(A, x)
print('Multiplying matrix and vector, Ax = b')
print('Output vector, b')
print(b)