# Author  : Gu-hwan Bae
# Date    : Sun Jan 28
# Summary : Encription by using Galois field.

import numpy as np
import gula.galois as gf

def randGF2Vec(length):
    output = np.full(length, gf.GF2(1))
    coords = np.random.randint(low=0, high=length, size=int(length/2))
    output[coords] = gf.GF2(0)
    return output

length = 8
# Make a arbitrary plain message as vector.
P = randGF2Vec(length)
# Make a arbitrary key.
K = randGF2Vec(length)

print('Plain message')
print('P =', P)

# Seperate a plain message and store in two variables.
# Even if someone get a one coded message, he can not
# get the plain message unless get both coded messages.
A = K
B = P - K

print('Coded message A')
print('A = Key =', A)

print('Coded message B')
print('B = P - Key =', B)

# Plain message is a sum of two coded message.
print('Plane message can be decoded by added two coded message.')
print('A + B = P =', A + B)

