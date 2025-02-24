#5.Demonstrate a mix of single and multiple inheritance.


class Engine:
    def start(self):
        print("Engine started!")

class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle, Engine):      #Hybrid Inheritance
    def drive(self):
        print("Car is being driven...")


car = Car()
car.start()
car.move()
car.drive()
