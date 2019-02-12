# Author  : Gu-hwan Bae
# Date    : Mon Feb 11, 2019
# Summary : Hamming code examples.

import numpy as np
import gula.hammingcode as hc
import gula.util as gutil

G = hc.getGenerator()

# Plain message vector, p
p = gutil.asGF2([1, 1, 0, 1])
print('Plain message, p =', p)

# Code word vector, c
c = np.dot(G, p)
print('Code word, c = G*p =', c)

# Parity check matrix, H
H = hc.getParityChecker()

# Decoder matrix, R
R = hc.getDecoder()
print('Decoded code word, R*c =', np.dot(R, c))

# Error vector, e
e = hc.getErrorWord()
print('Error word, e =', e)

c_noised = c + e
print('c_noised = c + e =', c_noised)

print('H*c_noised = H*e =',np.dot(H, c_noised))

ep = hc.findErrorWord(c_noised)
print('Error word, ep =', ep)

c_denoised = c_noised + ep
print('c_denoised = c_noised + e =', c_denoised)

print('Deocded code word, d = R*c_denoised =', np.dot(R, c_denoised))

c_noised = gutil.asGF2([1, 0, 1, 1, 0, 1, 1])
print('H*e =', np.dot(H, c_noised))

e = hc.findErrorWord(c_noised)
print('Error word, e =', e)
# Error vector was eliminated like under representation.
# c + e + e = c (because e + e = 0 in GF(2))
c_denoised = c_noised + e

print('Decoded code word, R*c_denoised =', np.dot(R, c_denoised))

# The matrix, C, that column is a noised code word.
C = gutil.asGF2([[1, 0, 0],
                 [0, 0, 0],
                 [1, 1, 0],
                 [1, 1, 1],
                 [0, 0, 0],
                 [1, 0, 0],
                 [1, 1, 1]])

print('Code words, C =\n', C)

# The matrix, E, that column is a error word.
E = hc.findErrorMatrix(C)
print('Error words, E =\n', E)

D = C + E
print('Denoised code word, D =\n', D)

print('Decoded code words = R*(C+E) =\n', np.dot(R, D))
