#1.Create a Car class with attributes brand, model, and year. Add a method display_info() to print car details.

class Car:  
    def __init__(self, brand, model, year):
        self.brand = brand   #attributes
        self.model = model
        self.year = year

    def display_info(self):  #method
        print(f"car details are:{self.brand},{self.model},{self.year}")

c1= Car("TATA","Nexon",2023)   #object
c1.display_info()   #method call via object