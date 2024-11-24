# Polymorphism: - Allow methods in different classes to have the same name but behave differently.

# task
#     1. Create Base class Shape with method area()
#     2. Ctreate two derived class Circle and Rectangle and overriede the area()
#     3. Demonstarte polymorphism by calling area() method.

import math

class Shape():
    def __init__(self):
        pass
    
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius) **2
    
    
class Reactangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
        return (self.length) * (self.width)
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5* (self.base) * (self.height)
    
    
cir1 = Circle(5)
print(cir1.area())

react1 = Reactangle(6, 8)
print(react1.area())

# Polymorphism in action 

shapes = [Circle(8), Reactangle(7, 5), Triangle(8, 9)]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.area()}")
