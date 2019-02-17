# Author  : Gu-hwan Bae
# Date    : Sun Jan 27
# Summary : Modeling a vector.

import numbers

class vector:
    """
    Vector can be expressed as a function that map domain to the corresponding field.
    It describe a vector of the real number field.
    Domain set is represented by a set. And function is represented by a dictionary.
    """
    def __init__(self, label, func, zero=0):
        self.domain = label
        self.func = func
        self.zero = zero

    def getItem(self, key):
        return self.func[key] if key in self.func else self.zero

    def setItem(self, key, val):
        if key in self.domain:
            self.func[key] = val

    def entries(self):
        return [self.func[d] for d in self.domain]

    def __add__(self, oth):
        """
        Elementwise addition.
        """
        output = vector(self.domain, {})
        if isinstance(oth, numbers.Number):
            for d in self.domain:
                output.func[d] = self.getItem(d) + oth
        elif isinstance(oth, vector):
            for d in self.domain:
                output.func[d] = self.getItem(d) + oth.getItem(d)
        else:
            return None
        return output

    def __sub__(self, oth):
        """
        Elementwise subtraction.
        """
        output = vector(self.domain, {})
        if isinstance(oth, numbers.Number):
            output = self + (-oth)
        elif isinstance(oth, vector):
            for d in self.domain:
                output.func[d] = self.getItem(d) - oth.getItem(d)
        else:
            return None
        return output

    def __mul__(self, oth):
        """
        Elementwise multiplication.
        """
        output = vector(self.domain, {})
        if isinstance(oth, numbers.Number):
            for d in self.domain:
                output.func[d] = self.getItem(d) * oth
        elif isinstance(oth, vector):
            for d in self.domain:
                output.func[d] = self.getItem(d) * oth.getItem(d)
        else:
            return None
        return output

    def __str__(self):
        label = 'D | F'
        label = label + '\n' + '-----'
        for d in self.domain:
            label = label + '\n' + str(d) + ' | ' + str(self.getItem(d))
        return label

def zeros(domain):
    """
    Return a zero vector.
    """
    return vector(domain, {}) # It has empty entries.

def getVector(domain, entries):
    """
    Return gula.vec.vector. Parameter domain and entries should be in order.
    """
    func = {d : entry for d, entry in zip(domain, entries)}
    return vector(set(domain), func)
