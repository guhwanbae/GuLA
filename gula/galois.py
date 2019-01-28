# Author  : Gu-hwan Bae
# Date    : Sun Jan 28
# Summary : Modeling a Galois field.

class GF2:
    """
    Express Galois Field, GF(2), as object.
    The field's addtion is same as XOR, logical operation.
    And multiplication is same as AND, logical operation.
    """
    def __init__(self, bit):
        self.bit = bit
    def __add__(self, oth):
        return GF2(1) if self.bit is not oth.bit else GF2(0)
    def __sub__(self, oth):
        return self + oth
    def __mul__(self, oth):
        return GF2(1) if self.bit is oth.bit and self.bit is 1 else GF2(0)
    def __repr__(self):
        return str(self.bit)
    def __str__(self):
        return str(self.bit)