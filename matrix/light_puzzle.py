# Author  : Gu-hwan Bae
# Date    : Sun Jan 29
# Summary : Modeling a light puzzle problem.
#  The goal of the light puzzle is to make all the buttons on.
#  Pressing a button reverses the status of the adjacent button.
#  Each button-states are represented by column vector of matrix.
#  State changes are expressed by linear combination of state vector.

import numpy as np
import gula.galois as gf

class state:
    """
    Modeling a button-state as vector.
    """
    def __init__(self, state):
        self.v = state

    def __add__(self, oth):
        return state(self.v + oth.v)

    def __mul__(self, oth):
        if isinstance(oth, gf.GF2):
            return state(self.v * oth)
        else:
            return None

    def __str__(self):
        (width, height) = self.v.shape
        edge = '-' * (5 * width - 1)
        pretty = edge
        for row in self.v:
            morse = ['*' if bit == gf.GF2(1) else ' ' for bit in row]
            pretty = pretty + '\n' + '| ' + ' | '.join(morse) + ' |'
            pretty = pretty + '\n' + edge
        return pretty

"""
 State vector : State when push the (2,2) button.
 It represent state of light puzzle.
 Like,
 ---------
 | * | * |
 ---------
 | * |   |
 ---------

 '*' represent button is light-on else empty space is light-off.
"""
# Push the right-bottom button
rb = state(np.array([[gf.GF2(1), gf.GF2(1)],
                     [gf.GF2(1), gf.GF2(0)]]))

# Push the left-bottom button.
lb = state(np.array([[gf.GF2(1), gf.GF2(1)],
                     [gf.GF2(0), gf.GF2(1)]]))

# Push the right-top button.
rt = state(np.array([[gf.GF2(1), gf.GF2(0)],
                      [gf.GF2(1), gf.GF2(1)]]))

# Push the left-top button.
lt = state(np.array([[gf.GF2(0), gf.GF2(1)],
                      [gf.GF2(1), gf.GF2(1)]]))

print('State when push the (2,2) button.')
print(rb)

print('State when push the (2,1) button.')
print(lb)

print('State when push the (1,2) button.')
print(rt)

print('State when push the (1,1) button.')
print(lt)

# Each column vector of matrix represents button-state.
state_table = [rb, lb, rt, lt]

print('\n\n')

# Flag vector, GF(2) 4-vector, represents whether button is pressed or not.
# Solution can be expressed by linear combination of state vectors.
flags_A = [gf.GF2(1), gf.GF2(0), gf.GF2(0), gf.GF2(1)]
print('Combination A =', flags_A)
solution_A = np.dot(state_table, flags_A)
print('And its solution =')
print(solution_A)

print('\n\n')

flags_B = [gf.GF2(1), gf.GF2(1), gf.GF2(1), gf.GF2(1)]
print('Combination B =', flags_B)
solution_B = np.dot(state_table, flags_B)
print('And its solution =')
print(solution_B)
print('All buttons are on. We solve the light-puzzle problem!')

