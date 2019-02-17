# Author  : Gu-hwan Bae
# Summary : Modeling a geometric transformations.

import numpy as np
import gula.vec as gvec
import gula.mat as gmat
import gula.util as gutil

def getCartesianLabel(dim = 3, mode = 'homogeneous'):
    """
    Return a label of cartesian coordinates.
    """
    coords = ['x', 'y', 'z',]
    if mode is 'euclidian':
        label = coords[:dim]
    elif mode is 'homogeneous':
        label = coords[:dim-1]
        label.append('u')
    else:
        return None
    return label

def homogeneousVector(entries = None, dim = 3):
    """
    Return a vector on homogeneous coordinates.
    """
    label = getCartesianLabel(dim, mode = 'homogeneous')
    
    if entries is None:
        entries = [0] * dim
        entries[dim-1] = 1
    return gvec.getVector(label, entries)

def homogeneous2euclidian(p):
    return p[:len(p)-1]

def includedAngle(u, v, mode = 'euclidian'):
    if mode is 'homogeneous':
        u = homogeneous2euclidian(u)
        v = homogeneous2euclidian(v)
    cosang = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    angle = np.arccos(cosang)
    return angle

def scale(factors, dim = 3, mode = 'homogeneous'):
    """
    Return a scaling matrix. Parameter factors is a list contains scale factor.
    """
    label = getCartesianLabel(dim, mode)
    S = gmat.matrix((set(label), set(label)),
                    {(d, d) : scale for d, scale in zip(label, factors)})
    return S

def translation(factors, dim = 3):
    """
    Return a translation matrix. Parameter factors is a list contains shift factor.
    """
    label = getCartesianLabel(dim, mode = 'homogeneous')
    T = gmat.eye(label)
    (R, C) = T.domain
    for r, shift in zip(R, factors):
        T.setItem((r, 'u'), shift)
    return T

def rotation(theta, unit = 'radian', mode = 'homogeneous', centre = (0, 0)):
    """
    Return a rotation matrix on xy coordinates.
    """
    if unit is 'degree':
        theta = np.deg2rad(theta)
    factors = np.array([[np.cos(theta), -np.sin(theta), 0],
                        [np.sin(theta),  np.cos(theta), 0],
                        [0,              0,             1]])
    if mode is 'euclidian':
        label = getCartesianLabel(2, mode)
        R = gmat.listlist2matrix(label, label, factors[:2, :2])
    elif mode is 'homogeneous':
        label = getCartesianLabel(3, mode)
        R = gmat.listlist2matrix(label, label, factors)
        (shift_x, shift_y) = centre
        R.setItem(('x', 'u'), shift_x)
        R.setItem(('y', 'u'), shift_y)
    else:
        return None
    return R

def reflection(ref_axis, dim = 3, mode = 'homogeneous'):
    """
    Return a matrix which flip across specific axis.
    Parameter 'ref_axis' is reference axis of reflection.
    """
    label = getCartesianLabel(dim, mode)
    A = gmat.eye(label)
    if ref_axis is 'origin':
        D = [d for d in label if d is not 'u']
    else:
        D = [d for d in label if d is not 'u' and d is not ref_axis]
    for d in D:
        A.setItem((d, d), -1)
    return A

def reflectAboutPoint(ref_point, dim = 3):
    """
    Return a matrix which flip across specific point on homogeneouse coordinates.
    """
    A = reflection('origin', dim, mode = 'homogeneous')
    T = translation(ref_point, dim)
    T = gutil.dot(T, T)
    return gutil.dot(T, A)

def reflectAboutLine(u, v, dim = 3, mode = 'homogeneous'):
    """
    Return a matrix which flip across the line which across point u and v
    on xy coordinates.
    """
    dir_vec = np.asarray(u) - np.asarray(v)
    x_axis = [0 for d in range(dim)]
    x_axis[0] = 1
    angle = includedAngle(dir_vec, x_axis, mode)
    R = rotation(angle, mode)
    T = reflection('x', dim)
    # First, reflect across the x-axis and then rotate twice about included angle.
    # A = R*R*T
    A = gutil.dot(R, T)
    A = gutil.dot(R, A)
    return A