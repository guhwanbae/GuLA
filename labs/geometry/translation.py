# Author    :   Gu-hwan Bae
# Summary   :   Modeling a translation. Translation is linear transform on
#               the homogeneouse filed.

import gula.geometry as ggeo
import gula.mat as gmat
import gula.util as gutil

x_hm = ggeo.homogeneousVector([0, 0, 1], dim = 3)
print('Point on 3D Homogeneous coordinates, x =\n', x_hm)

A_hm = ggeo.translation([2, 2, 1], dim = 3)
print('Translation matrix, A =\n', A_hm)

b_hm = gutil.dot(A_hm, x_hm)
print('Translated point on 3D Homogeneous coordinates, A*x = b =\n', b_hm)


A = ggeo.translation([1, 1, 1], dim = 3)
print('Translation matrix, A =\n', A)

B = gmat.listlist2matrix(['x', 'y', 'u'],
                    ['0', '1', '2', '3'],
                    [[0, 1, 2, 5],
                     [0, 1, 2, 0],
                     [1, 1, 1, 1]])
print('The matrix that columns are point vectors, B =\n', B)

X = gutil.dot(A, B)
print('Translated points, A*B = X = \n', X)
