# 🐍 Inheritance in Python

## 📘 What is Inheritance?
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class to **use the properties and methods** of another class.  
It helps in **code reusability**, **readability**, and **maintaining a hierarchy** between classes.

---

## 🧩 Example Code

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks loudly!")

# Creating object
dog1 = Dog("Rocky", "Labrador")

# Accessing parent and child methods
dog1.sound()   # from Animal class
dog1.bark()    # from Dog class
```

---

## 🧠 Output

```
Rocky makes a sound.
Rocky barks loudly!
```

---

## ✅ Key Points
- The **Dog** class inherits attributes and methods from the **Animal** class.  
- The child class can **extend** or **override** the parent’s behavior.  
- Inheritance improves **code reuse** and reduces redundancy.

---

## 🏁 Summary
Inheritance allows one class to derive behavior from another.  
In this example, `Dog` inherits from `Animal`, showing how a child class can use and extend features of a parent class.
