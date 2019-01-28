# Author  : Gu-hwan Bae
# Date    : Sun Jan 27
# Summary : Test a vector model and its operations.

import gula.vec as gvec

D = {'A', 'B', 'C'}
func = {'A':1, 'B':2}
v = gvec.vector(D, func)
print('Vector ,v')
print(v)

# Make a zero vector.
z = gvec.zeros(D)
print('Zero vector, z')
print(z)

# Add a mapping expression to vector, v.
print('Set a mapping, C - 3, to the vector')
v.setItem('C', 3)
print(v)

# Doubling a vector, v.
v_double = v * 2  # Elementwise multiplication.
print('Doubled vector, v_double')
print(v_double)

# Make a new vector, u, that has same domain as v.
u = gvec.vector(v.domain, {'A':5, 'C':10})
print('Vector, u, with same domain as v.')
print(u)

# Add vector v and u.
print('Vector addtion, w = u + v')
w = u + v
print(w)

# Subtract vector v and u.
print('Vector subtraction, w = u - v')
w = u - v
print(w)

# Elementwise multiplication, vector v and u.
print('Elementwise multiplication, w = u * v')
w = u * v
print(w)
