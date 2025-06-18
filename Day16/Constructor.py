# Constructor

class Human:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print(f"{self.name} is walking")

n = Human("Nagarjun")
n.walk()  # Output: nagarjun is walking
print(n.name)  # Output: nagarjun


# Constructor with default values
class Human:
    def __init__(self, name,age=0): # Default value for age
        self.name = name
        self.age = age
    
    def calling(self):
        print(f"{self.name} age is {self.age} ")


# Creating multiple objects

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(f"Laptop Brand: {self.brand}, Model: {self.model}")

laptop1 = Laptop("Dell", "XPS 13")
laptop2 = Laptop("Apple", "MacBook Pro")

laptop1.display()  # Output: Laptop Brand: Dell, Model: XPS 13
laptop2.display()  # Output: Laptop Brand: Apple, Model: MacBook Pro
