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


# taking input from user

class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        print(f"Laptop Brand: {self.brand}, Model: {self.model}")

# Taking input from the user
brand1 = input("Enter brand of first laptop: ")
model1 = input("Enter model of first laptop: ")

brand2 = input("Enter brand of second laptop: ")
model2 = input("Enter model of second laptop: ")

laptop1 = Laptop(brand1, model1)
laptop2 = Laptop(brand2, model2)

laptop1.display()
laptop2.display()
n = Human("Nagarjun",20)

Human.calling(n)  # Alternative way to call the method
