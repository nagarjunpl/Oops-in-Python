# 🐍 Polymorphism in Python

## 📘 What is Polymorphism?
**Polymorphism** means **"many forms"**.  
In Python, polymorphism allows **different classes** to have methods **with the same name** but **different implementations**.

It helps write **flexible and reusable code**, where the same function name can behave differently depending on the object that calls it.

---

## 🧠 Example 1 — Same Method Name in Different Classes

```python
class Dog:
    def sound(self):
        print("Dog barks!")

class Cat:
    def sound(self):
        print("Cat meows!")

# Using polymorphism
for animal in (Dog(), Cat()):
    animal.sound()
```

### 🧾 Output:
```
Dog barks!
Cat meows!
```

---

## 🧠 Example 2 — Polymorphism with Inheritance

```python
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks!")

class Cat(Animal):
    def sound(self):
        print("Cat meows!")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()
```

### 🧾 Output:
```
Dog barks!
Cat meows!
Some generic animal sound
```

---

## ✅ Key Points
- Polymorphism means **same function name, different behavior**.  
- It makes code **cleaner**, **easier to extend**, and **more flexible**.  
- Commonly used in **method overriding** (in inheritance).  
- Helps write functions that can work with **objects of different types**.

---

## 🏁 Summary
Polymorphism allows one interface to be used for different data types.  
It’s one of the main pillars of **Object-Oriented Programming (OOP)** — making programs more dynamic and easier to scale.
