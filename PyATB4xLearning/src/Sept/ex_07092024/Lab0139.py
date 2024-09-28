# OOPS
# class - blueprint(collection of attribute[data variable] and behaviour[method])
# object - Instance of a class
# Encapsulation - public, _protected, __private
# Inheritance - Single, multiple, multilevel, hierarchical, hybrid
# Polymorphism - method overriding, method overloading(x)
# self, super(), __init__ (constractor - calls by default when the object is created)

# Abstraction
# Hide the details and show what is required
# This in class level, it is basically an incomplete method which needs to be completed and then can be used

# Car -> with key __private, tyers - public
# Car -> multiple - Engine, Gearbox
# Car -> driver -> Engine, Gearbox ?

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):     # incomplete class, if any other calls has to inherit then it has to be completed
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog("PP")
dog.sound()