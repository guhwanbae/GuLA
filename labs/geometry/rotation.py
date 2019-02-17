# Author    :   Gu-hwan Bae
# Summary   :   Modeling a rotation. Rotation is linear transform.

import gula.geometry as ggeo
import gula.util as gutil

x = ggeo.homogeneousVector([1, 0, 1], dim = 3)
print('Point on homogeneous, x =\n', x)

A = ggeo.rotation(45, unit='degree')
print('The matrix, A, which rotate 45 degrees counter-clockwise, A = \n', A)

b = gutil.dot(A, x)
print('Rotated point, A*x = b = \n', b)
