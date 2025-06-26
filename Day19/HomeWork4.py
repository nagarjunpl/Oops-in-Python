# Creating a class

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def display(self):
        print(f"{self.brand} brand price is {self.price}")

n1 = Mobile("Samsung", 50000)
n2 = Mobile("iPhone", 80000)

n1.display()
n2.display()


# Method Definition

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"{self.name} has scored {self.marks} marks")

a = Student("Arjun", 97)

a.display()


# adding a default parameters

class Student:
    def __init__(self, name, marks=80): # default parameter
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"{self.name} has scored {self.marks} marks")

a = Student("Arjun")

a.display()


# Encapsulation

class BankAccount:
    def __init__(self, acc_no, balance):
        self.__acc_no = acc_no
        self.__balance = balance

    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposit successful - Balance {self.__balance}")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient funds")
            return
        self.__balance -= amount
        print(f"Withdraw successful - Balance {self.__balance}")

a = BankAccount(123445, 1000)

a.check_balance()
a.deposit(2000)
a.withdraw(1000)


# Inheritance

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Bike(Vehicle): # Inheriting
    def __init__(self, name):
        self.name = name

    def ride(self):
        print("Riding")

s = Bike("RE")

s.start()
s.ride()


# Polymorphism

class shape:
    def calc_area(self):
        print("Calculatig area")

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        super().calc_area()
        print(f"Area of Circle : {(22/7)*self.radius*self.radius}")

class Rectangle(shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calc_area(self):
        super().calc_area()
        print(f"Area of Rectangle : {self.l*self.b}")

c = Circle(5)
r = Rectangle(5, 10)

c.calc_area()
r.calc_area()


# Getters and Setters

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)
    
    def set_balance(self, update_balance):
        if update_balance<0:
            print("ERROR : Balance cannot be negative value")
            return
        self.__balance = update_balance
        print(self.__balance)

b = BankAccount(500)

b.get_balance()
b.set_balance(-1)
