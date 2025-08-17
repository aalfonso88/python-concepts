from abc import ABC, abstractmethod
import math

class Shape(ABC):   # abstract base class
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):   # required by Shape
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

s = Square(4)
print(s.area())     # ✅ 16
shape = Shape()   # ❌ TypeError: Can't instantiate abstract class
