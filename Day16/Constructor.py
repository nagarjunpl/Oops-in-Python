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

n = Human("Nagarjun",20)

Human.calling(n)  # Alternative way to call the method


