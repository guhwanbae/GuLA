# Author  : Gu-hwan Bae
# Date    : Sun Jan 27
# Summary : Vector operators and utilities.

import vecmodel.vector as myvec

def zeros(domain):
    """
    Return a zero vector.
    """
    return myvec.Vector(domain, {}) # It has empty entries.

def multiply(vec, alpha):
    """
    Return a vector elementwise multiplied.
    """
    return myvec.Vector(vec.domain, {d:alpha*val for d, val in vec.func.items()})

def add(u, v):
    if u.domain is v.domain:
        return myvec.Vector(u.domain, {d:v.getItem(d)+u.getItem(d) for d in u.domain})