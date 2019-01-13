import numpy as np

# Express Galois Field, GF(2), by object.
class GF2:
    def __init__(self, bit):
        self.bit = bit
    def __add__(self, oth):
        return GF2(0) if self.bit is oth.bit else GF2(1)
    def __sub__(self, oth):
        return self + oth
    def __repr__(self):
        return str(self.bit)
    def __str__(self):
        return str(self.bit)

def getRandomVector(length):
    return np.array([GF2(1) if np.random.rand() > 0.5 else GF2(0) for i in range(length)])

def printGF2Vector(vector):
    print([gf.bit for gf in vector])

# Make a arbitrary plain message as vector.
plain = getRandomVector(8)
# Make a arbitrary key.
key = getRandomVector(8)

print('Plain message =', plain)

# Seperate a plain message and store in two variables.
# Even if someone get a one coded message, he can not
# get the plain message unless get both coded messages.
coded_a = key
coded_b = plain - key


print('Coded message A =', coded_a)
print('Coded message B =', coded_b)

# Plain message is a sum of two coded message.
print('msg A + msg B =', coded_a + coded_b)
