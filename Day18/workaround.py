# Getters And Setters

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self): #getter
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name): # setter
        self.__name = name

n = Student("Arjun", 20)

print(n.get_name())

print(n.get_age())

n.set_name("Nagarjun")

print(n.get_name())


# Method Overriding

class Animal:
    def make_sound(self):
        print("Animal making sound")

class dog(Animal):
    def make_sound(self):
        print("Bark")

a = dog()
a.make_sound()
