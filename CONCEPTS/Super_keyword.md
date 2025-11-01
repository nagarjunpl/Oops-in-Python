# 🧩 `super()` Keyword in Python

## 📘 What is `super()`?
In Python, the `super()` keyword is used inside a **child class** to **call methods or constructors** from its **parent class**.  
It helps you reuse the parent’s code without directly referring to its name.

---

## 🧠 Why use `super()`?
- To **avoid repeating parent class names** (especially useful when you have multiple inheritance).  
- To make your code **more flexible** and **maintainable**.  
- It ensures **the parent class’s `__init__()`** or other methods are called properly.

---

## 🧩 Example Code

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Child class using super()
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calling parent class constructor
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

## 🧾 Output
```
Rocky makes a sound.
Rocky barks loudly!
```

---

## ✅ Key Points
- `super()` allows access to parent class methods and constructors.  
- It is safer than directly calling `ParentClassName.method(self, ...)`.  
- Commonly used in **inheritance** and **method overriding**.

---

## 🏁 Summary
`super()` helps you **connect** the child and parent classes easily.  
It’s the **preferred way** to call parent methods because it makes your code cleaner, reusable, and easier to maintain.
