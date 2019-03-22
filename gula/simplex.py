# Author  : Gu-hwan Bae
# Summary : Simple two phase simplex method which maximize a linear object
#           funtion of linear program.

import numpy as np

def _initial_tableau_(c, A, b):
    '''
    Return a initial tableau, standard form.
    tableau = |  A I b |
              | -c 0 0 |
    Vector c is coefficients of objective function.
    Matrix A is coefficients of constrain inequilities.
    Vector b is non-negative constants.
    Matrix I is identical which represent coefficients of slack variables.
    '''
    ncons = A.shape[0]
    nvars = len(c)
    tableau = np.zeros((ncons+1, nvars+ncons+2))
    tableau[:ncons, :nvars] = A
    tableau[-1, :nvars] = -c
    tableau[:,nvars:-1] = np.eye(ncons+1)
    tableau[:-1,-1] = b
    return (nvars, ncons, tableau)

def _is_optimal_(tableau):
    '''
    Return a true if all objective coefficients are greater than zero.
    Otherwise false.
    '''
    if np.min(tableau[-1,:-1]) >= 0:
        return True
    else:
        return False

def _pivot_row_(tableau):
    '''
    Return a index of next non-basis index which has a minimum objective coefficient.
    '''
    m = np.min(tableau[-1,:-1])
    if m <= 0:
        return np.where(tableau[-1,:-1] == m)[0][0]
    else:
        return None

def _pivot_(tableau):
    '''
    Return a pair, indices of next basis and non-basis by pivoting.
    '''
    next_nonbasis_idx = _pivot_row_(tableau)
    ratio = tableau[:-1, -1] / tableau[:-1,next_nonbasis_idx]
    non_neg_min = np.min(ratio[ratio > 0])
    next_basis_idx = np.where(ratio == non_neg_min)[0][0]
    return next_basis_idx, next_nonbasis_idx

def _eliminate_row_(row, col, tableau):
    '''
    Eliminate rows in the tableau based on the target row.
    '''
    entry = tableau[row][col]
    target_row = tableau[row] / entry
    for idx, coef in enumerate(tableau[:,col]):
        if idx != row:
            tableau[idx] -= target_row*coef

def maxlinprog(c, A, b, max_iter=30):
    '''
    Maximize a linear objective function to linear equality and non-negative
    constraints using the two phase simplex method.
    Vector c is coefficients of objective function.
    Matrix A is coefficients of constrain inequalities.
    Vector b is constants of in inequalities.
    '''
    (nvars, ncons, tableau) = _initial_tableau_(c, A, b)
    # At first, slack variables are non-basis solutions.
    nonbasis_label = [slack_idx for slack_idx in range(nvars,nvars+ncons)]
    n = 0
    is_find_optimal = False

    while n < max_iter and _is_optimal_(tableau) is not True:
        next_basis_idx, next_nonbasis_idx = _pivot_(tableau)
        nonbasis_label[next_basis_idx] = next_nonbasis_idx
        _eliminate_row_(next_basis_idx, next_nonbasis_idx, tableau)

    if _is_optimal_(tableau):
        variables = np.zeros(nvars)
        for idx in nonbasis_label:
            if idx < nvars:
                variables[idx] = tableau[idx,-1]
        optimal_value = tableau[-1,-1]
        return variables, optimal_value
    else:
        return None
