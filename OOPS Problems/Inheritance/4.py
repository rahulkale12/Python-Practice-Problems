#4.Create a base class Animal and derive Dog and Cat from it.


class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):         #Hierarchical Inheritance    
    def make_sound(self):
        print("Bark!")

class Cat(Animal):         #Hierarchical Inheritance 
    def make_sound(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()
