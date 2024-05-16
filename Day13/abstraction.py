# abstraction (추상화)
from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2


# rectangle, triangle

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

class rectangle(ABC):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2