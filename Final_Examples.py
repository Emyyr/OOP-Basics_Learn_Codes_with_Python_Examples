#Final Project 
"""
OOP: Object Oriented Programing
    -class/object 
    -attributes/methods
    -encapsulation/ abstraciton
    -inheritance
    -overriding/polymorphism
"""
from abc import ABC , abstractmethod

class Shape(ABC):

    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
    @abstractmethod
    def toString(self): pass

class Square(Shape):
    def __init__(self, edge):
        self.__edge = edge # encapsulation private attribute
    def area(self):
        result = self.__edge**2
        print("Square area: ",result)
    def perimeter(self): 
        result = self.__edge*4
        print("Square perimeter: ",result)
    # override and polymorphism
    def toString(self):
        print("Square edge: ",self.__edge)
# child
class Circle(Shape):
    PI = 3.14
    def __init__(self, radius):
        self.__radius = radius
    def area(self): 
        result = self.PI*self.__radius**2 # pi*r^2
        print("Circle area: ",result)
    def perimeter(self): 
        result = 2*self.PI*self.__radius  # 2*pi*r
        print("Circle perimeter: ",result)
    def toString(self):
        print("Circle radius: ",self.__radius)
    

a = Circle(5)
a.area()
a.perimeter()
a.toString()
