# 2. Create a Laptop class with the following:

    # A public attribute brand.
    # A protected attribute _processor.
    # A private attribute __price.
    # A method display_info() that prints all attributes.
    # A method set_price(new_price) to update the private attribute __price.
    # Create a subclass GamingLaptop that tries to access all attributes and override display_info().


class Laptop:
    def __init__(self, brand, processor, price):
        self.brand = brand          # Public Attribute
        self._processor = processor # Protected Attribute
        self.__price = price        # Private Attribute

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Processor: {self._processor}")
        print(f"Price: {self.__price}")

    def set_price(self, new_price):
        self.__price = new_price
        print(f"Updated Price: {self.__price}")

class GamingLaptop(Laptop):
    def __init__(self, brand, processor, price, gpu):
        super().__init__(brand, processor, price)
        self.gpu = gpu  # Additional Attribute for Gaming Laptop

    def display_info(self):
        print(f"Brand: {self.brand}")          # Accessing public attribute
        print(f"Processor: {self._processor}") # Accessing protected attribute
        # print(f"Price: {self.__price}")      # Will raise an AttributeError
        print(f"GPU: {self.gpu}")

# Creating objects
laptop1 = Laptop("Dell", "Intel i5", 70000)
laptop1.display_info()

# Updating price using setter method
laptop1.set_price(75000)

print("\n--- Gaming Laptop ---")
gaming_laptop = GamingLaptop("Asus", "Intel i7", 120000, "NVIDIA RTX 3060")
gaming_laptop.display_info()

# Trying to access protected and private attributes
print("\nAccessing Attributes from outside the class:")
print("Brand (Public):", gaming_laptop.brand)         # Allowed
print("Processor (Protected):", gaming_laptop._processor) # Allowed but not recommended
# print("Price (Private):", gaming_laptop.__price)   # Raises AttributeError

# Accessing private attribute using name mangling
print("Price (Private using Name Mangling):", gaming_laptop._Laptop__price)  # Not recommended
