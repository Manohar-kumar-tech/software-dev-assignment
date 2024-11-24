# Abstraction: - hides the internal details and shows only the essential features of an object or system. Why? to simplify complex system and focus on what an object does rather than how it does it.
# e.g. think of car - you know how to drive it (accelerate, brake, steer) without knowing the engine's internal mechanics
#  the steering wheels, pedals and dashboard represent "Abstarction", hiding internal complexities of the car engine.
# in Code abstarction is achieve through abstract class or interface in programming

from abc import ABC, abstractmethod
# Abstarct class
class Shape(ABC):
    # force sublclass to specific implementaion of area()
    @abstractmethod
    def area(self):          
        pass   
    
    # force sublclass to specific implementaion of area()
    @abstractmethod
    def perimeter(self):
        pass


# Concrete class
class Reactangle(Shape):
    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        super().perimeter()
        return 2 * (self.height + self.width)
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    
shapes = [Reactangle(8,6), Circle(7)]
for shape in shapes:
    print(f"Area of {shape.__class__.__name__} is {shape.area()} and primeter is {shape.perimeter()}")