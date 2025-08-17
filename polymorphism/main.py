import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Square(4), Circle(3), Triangle(6, 2)]

for shape in shapes:
    print(shape.area())  # Each class runs its own version of area()
