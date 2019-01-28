# Author  : Gu-hwan Bae
# Date    : Sun Jan 27
# Summary : Test a matrix modeling class and its utilities.

import gula.mat as gmat

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
