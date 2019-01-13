# Vector can be expressed as a function that map domain to the corresponding field.
# class Vector describe a vector of the real number field.
class Vector:
    def __init__(self, labels, function):
        self.D = labels # Domain Set
        self.f = function # Dictionary describe a function

    def setItem(self, d, val):
        self.f[d] = val

    def getItem(self, d):
        return self.f[d] if d in self.f else 0

    def figure(self):
        for d in self.D:
            print('%s in domain -> %d in codomain' % (d, self.f[d])) if d in self.f else 0

    def add(self, u):
        if self.D is u.D:
            for d in self.D:
                self.f[d] = self.f[d] + u.getItem(d)


domain = {'A', 'B', 'C'}
function = {'A':1, 'B':2}
v = Vector(domain, function)
v.figure()

def zero_vec(D):
    return Vector(D, {}) # It has empty dictionary.

# Make a zero vector.
z = zero_vec(domain)
z.figure()

v.setItem('C', 3)
print("v['B'] =", v.getItem('B'))
print("v['D'] =", v.getItem('D'))

def scalar_mul(v, alpha):
    return Vector(v.D, {d:alpha*val for d, val in v.f.items()}) # Elementwise multiply

# Doubling
v_double = scalar_mul(v, 2)
v_double.figure()

def add(v, u):
    if v.D is u.D:
        return Vector(v.D, {d:v.getItem(d)+u.getItem(d) for d in v.D})

# Make a new vector, u.
u = Vector(v.D, {'A':5, 'C':10})
# Add vector v and u by using global procedure, add(v, u).
w = add(v, u)
w.figure()

# Add vector u to v by using a method.
w.add(u)
w.figure()
