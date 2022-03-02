# Soyut Classes / Abstract Classes
"""
1- We can't use Animal class and create a veraible.
2- We can't call main clas(old) definition to our child class(new).
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod   # Abstractmethod means a pattern. We have a pattern for other class will create.
    def walk(self):
        print("Walk")
    @abstractmethod
    def run(self):
        print("Run")
class Bird(Animal):
    def __init__(self):
        print("Bird")   #We can't call Animal functions. We have to write abstractmethods functions again.
    def walk(self):
        print("Walk")
    def run(self):
        print("Run")

a=Bird()
a.walk()
a.run()