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
v_double = gvec.multiply(v, 2)
print('Doubled vector, v_double')
print(v_double)

# Make a new vector, u, that has same domain as v.
u = gvec.vector(v.domain, {'A':5, 'C':10})
print('Vector, u, with same domain as v.')
print(u)

# Add vector v and u by using global procedure, add(v, u).
print('Vector addtion, w = u + v')
w = gvec.add(v, u)
print('Vector, w')
print(w)

# Add vector u to v by using a method.
print('Add vector u to w by using instance method')
w.add(u)
print('Vector, w')
print(w)
