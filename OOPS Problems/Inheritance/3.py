#3.Create a base class Vehicle, a subclass Car, and a subclass ElectricCar inheriting from Car.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):                       #multilevel inheritance
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print(f"Model: {self.model}")

class ElectricCar(Car):                           #multilevel inheritance
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def show_battery(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")


tesla = ElectricCar("Tesla", "Model S", 100)
tesla.show_brand()
tesla.show_model()
tesla.show_battery()
