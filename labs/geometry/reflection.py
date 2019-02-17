# Author    :   Gu-hwan Bae
# Summary   :   Modeling a reflection across a reference axis, origin,
#               specific point or line. Scaling is linear transform.

import numpy as np
import gula.geometry as ggeo
import gula.vec as gvec
import gula.mat as gmat
import gula.util as gutil

# Reflect across a reference axis.
x = ggeo.homogeneousVector([2, 2, 1], dim = 3)
print('Point on homogeneous, x =\n', x)

A = ggeo.reflection('y', dim = 3, mode = 'homogeneous')
print('The matrix, A, which reflect across by y-axis, A =\n', A)

b = gutil.dot(A, x)
print('Reflected point, A*x = b =\n', b)

# Reflect across a origin point.
x = ggeo.homogeneousVector([2, 2, 1], dim = 3)
print('Point on homogeneous, x =\n', x)

A = ggeo.reflection(ref_axis = 'origin', dim = 3, mode = 'homogeneous')
print('The matrix, A, which reflect across origin point, A =\n', A)

b = gutil.dot(A, x)
print('Reflected point, A*x = b =\n', b)

# Reflect across a specific point.
x = ggeo.homogeneousVector([2, 2, 1], dim = 3)
print('Point on homogeneous, x =\n', x)

A = ggeo.reflectAboutPoint([1, 1, 1], dim = 3)
print('The matrix, A, which reflect across a specific point, (1, 1). A =\n', A)

b = gutil.dot(A, x)
print('Reflected point, A*x = b =\n', b)

# Reflect across a specific line.
x = ggeo.homogeneousVector([2, 1, 1], dim = 3)
print('Point on homogeneous, x =\n', x)

# Two points which are acrossed by a reference line on homogeneous coordinate.
u = [2, 1, 1]
v = [0, 0, 1]
A = ggeo.reflectAboutLine(u, v, dim = 3, mode = 'homogeneous')
print('The matrix, A, which reflect across a line through point u and v. A =\n', A)

b = gutil.dot(A, x)
print('Reflected point, A*x = b =\n', b)
