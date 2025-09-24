# Abstraction in Python  

## What is Abstraction?
- **Abstraction** is the concept of **hiding the complex implementation details** of a system and **showing only the necessary features** to the user.  
- It helps in **reducing complexity** and **increasing efficiency** in software development.  

Think of it like driving a car:  
- You **use the steering wheel, pedals, and buttons** (the interface).  
- You **don’t need to know how the engine works internally** (hidden complexity).  

---

## In Python (Object-Oriented Programming)
- Abstraction is achieved using **abstract classes** and **methods**.  
- Python provides the `abc` module for defining **abstract base classes**.

---

## Example of Abstraction
```python
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method (no implementation)

# Subclass must implement abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started!")

# Using the classes
my_car = Car()
my_car.start_engine()  # Output: Car engine started!

my_bike = Bike()
my_bike.start_engine()  # Output: Bike engine started!
```

---

## Key Points
- **Hides internal details** and **exposes only the necessary functionality**.  
- Helps in **managing complexity** in large systems.  
- Achieved using **abstract classes** and **interfaces**.  
- Users interact with **methods/functions**, not the inner workings.  

---

💡 Analogy:
- Think of your **smartphone**: you use apps by clicking icons, but you don’t need to know how each app is coded internally. That’s abstraction in real life.
