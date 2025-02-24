#2. Overload the + operator for a Vector class.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"Vector({self.x}, {self.y})")

# Usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

v3.display()
