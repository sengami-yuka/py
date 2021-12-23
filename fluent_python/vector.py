import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):  # python 3
        return bool(self.x or self.y)

    def __nonzero__(self):  # python 2.7
        return bool(self.x or self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v = Vector(3, 4)
print abs(v)
print bool(v)
print bool(Vector())
print v * 3
print v + Vector(1, 3)
