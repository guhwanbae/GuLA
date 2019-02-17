# Author    :   Gu-hwan Bae
# Summary   :   Modeling a scaling. Scaling is linear transform.

import gula.geometry as ggeo
import gula.util as gutil

x = ggeo.homogeneousVector([2, 2, 1], dim = 3)
print('Point on homogeneous, x =\n', x)

A = ggeo.scale([3, 4, 1], dim = 3, mode = 'homogeneous')
print('Scaling matrix, A = \n', A)

b = gutil.dot(A, x)
print('Scaled point, A*x = b = \n', b)
