"""
Author  : Gu-hwan Bae
Summary : Pass the message through the noise channel to observe how
    distorted it is. And simulates whether messages passed through
    the noise channel can be restored by using parity check.
"""

import numpy as np
import gula.hammingcode as hc
import gula.galois as gf
import gula.util as gutil

message = 'Hello! GULA is a python package abstracted from linear algebra properties. I will cover a variety of topics in the linear algebra and its applications.'

bits = gutil.str2bits(message)

# Encoding and decoding tests.
print('String =', message)
print('String to bits, bits =', ''.join(str(bit) for bit in bits))
print('Bits to string, string =', gutil.bits2str(bits))

# Tests code word encoding.
# Make a sequence matrix that column vector is 4-vector.
G = hc.getGenerator()
P = hc.bits2matrix(bits)
print('Plain message, P =\n', P)
# The matrix, C, has column vector as code word.
C = np.dot(G, P)
print('Code words matrix, C=\n', C)

# Decoder matrix
R = hc.getDecoder()

# The matrix, D, is decoded message.
D = np.dot(R, C)
print('Decoded message, D =\n', D)
decoded_bits = hc.matrix2bits(D)

print('Decoded bits =', ''.join(str(bit) for bit in decoded_bits))
print('Bits to string, string =', gutil.bits2str(decoded_bits))

# Simulates noise channel model.
C_noised = hc.noiseChannel(C, 0.1)
print('Noised, C_noised =\n', C_noised)

D_noised = np.dot(R, C_noised)
bits_noised = hc.matrix2bits(D_noised)
print('String by decoding code words without parity check.')
print('String =', gutil.bits2str(bits_noised))

E = hc.findErrorMatrix(C_noised)
print('Error matrix by using parity check, E = \n', E)

# Error components are eleminated like under expression.
# E + E = O, zero matrix.
# C_noised = C + E
# C_noised + E = C + E + E = C + O = C
C_denoised = C_noised + E
D_denoised = np.dot(R, C_denoised)
print('Denoised code words, C =\n', C)

bits_denoised = hc.matrix2bits(D_denoised)
print('String by decoding denoised code words.')
print('String =', gutil.bits2str(bits_denoised))

