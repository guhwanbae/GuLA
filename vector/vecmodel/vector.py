# Author  : Gu-hwan Bae
# Date    : Sun Jan 27
# Summary : Vector modeling

# Vector can be expressed as a function that map domain to the corresponding field.
# class Vector describe a vector of the real number field.
class Vector:
    """
    Vector can be expressed as a function that map domain to the corresponding field.
    It describe a vector of the real number field.
    Domain set is represented by a set. And function is represented by a dictionary.
    """
    def __init__(self, label, func):
        self.domain = label
        self.func = func

    def getItem(self, key):
        return self.func[key] if key in self.func else 0

    def setItem(self, key, value):
        if key in self.domain:
            self.func[key] = value

    def add(self, other):
        if self.domain is other.domain:
            for d in self.domain:
                self.func[d] = self.func[d] + other.getItem(d)
                
    def __str__(self):
        label = 'D | F'
        label = label + '\n' + '-----'
        for d in self.domain:
            label = label + '\n' + str(d) + ' | ' + str(self.getItem(d))
        return label