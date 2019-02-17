# Author    :   Gu-hwan Bae
# Summary   :   Denotation of euclidian and homogeneous coordinates.

import gula.geometry as ggeo
import gula.vec as gvec
import gula.util as gutil

x_eu = gvec.getVector(['x', 'y'], [12, 30])
A_eu = ggeo.scale([1, 2], dim = 2, mode = 'euclidian')

print('Point on 2D Euclidian, x =\n', x_eu)
print('Scaling matrix, A =\n', A_eu)

b_eu = gutil.dot(A_eu, x_eu)
print('Scaled point on 2D Euclidian, A*x = b =\n', b_eu)

x_hm = ggeo.homogeneousVector([1, 1, 1], dim = 3)
A_hm = ggeo.scale([1, 2, 1], dim = 3, mode = 'homogeneous')
print('Point on Homogeneous, x =\n', x_hm)
print('Scaling matrix, A =\n', A_hm)

b_hm = gutil.dot(A_hm, x_hm)
print('Scaled point on Homogeneous, A*x = b =\n', b_hm)

