"""
Implementujme třídu Vector2
__init__(self, x, y)
__repr__(self) --> "Vector2(x, y)"
.magnitude
__eq__(self, other)
__add__(self, other)
__mul__(self, other) -- pro skaláry, pro vektory jako skalární součin
"""

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector2({}, {})".format(self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if type(other) is Vector2:
            return self.x * other.x + self.y * other.y
        else:
            return Vector2(self.x * other, self.y * other)


print(Vector2(4, 6) * -1)
print(Vector2(4, 6) * Vector2(1, 3))
