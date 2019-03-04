# Author  : Gu-hwan Bae
# Summary : Examples of orthogonal properties in the linear vector space.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import gula.orthogonal as gortho

def plot3dLine(point, axes, tag):
    n = 100
    coords = [np.linspace(0, p, n) for p in point]
    x = coords[0]
    y = coords[1]
    z = coords[2]
    ax.plot(x, y, z, label=tag)


# Case I : Find a component of b orthogonal to plane, Span{V}.

b = np.array([1, 1, 1])
V = np.array([[1, 0, 0], [0, 1, 0]]).T

h, sigma = gortho.projectionOrthogonal(b, V)

print('The component of b orthogonal to Span{v1, v2}, h =', h)
# b = [v1 | v2 | h] * sigma
print('Sigma =', sigma)

fig = plt.figure()
ax = fig.gca(projection='3d')

plot3dLine(V[:,0], ax, 'v1')
plot3dLine(V[:,1], ax, 'v2')
plot3dLine(h, ax, 'h')

ax.legend()
plt.show()


# Case II : Decomposition.

b = np.array([5, -5, 2])
V = np.array([[8, -2, 2], [4, 2, 4]]).T
H, S = gortho.orthogonalize(V)

print('Orthogonalized generators, H =\n', H)

# Pytagoras theorem in vectors, b, b_orthogonal, b_projection.
# b = b_projection + b_orthogonal (components decomposition)
b_orthogonal, sigma = gortho.projectionOrthogonal(b, H)
b_projection = b - b_orthogonal

print('b =', b)
print('b_ortogonal =', b_orthogonal)
print('b_projection =', b_projection)


# Case III : Find orthogonalized vectors.
b = np.array([5, -5, 2])
V = np.array([[8, -2, 2], [4, 2, 4]]).T
H, S = gortho.orthogonalize(V)

# The column vectors of matrix V are generators of Span{V}.
print('V =\n', V)
# The column vectors of matrix H are generators orthogonalized each other.
# Span {V} = Span {H}
# If matrix H has no null vector, column vectors of H are basis.
print('H =\n', H)
# V = H*S
print('S =\n', S)
print('H * S =\n', np.dot(H,S))
