#1.Create an abstract class Animal with an abstract method make_sound(). Implement subclasses Dog and Cat with their own sound.

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")

class Cat(Animal):
    def make_sound(self):
        print("meow meow")

c1 = Cat()  
c1.make_sound() 

d1 = Dog()
d1.make_sound()