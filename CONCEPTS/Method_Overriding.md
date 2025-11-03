# 🐍 Method Overriding in Python

## 📘 Definition
Method overriding in Python occurs when a **child class** (subclass) defines a **method with the same name as a method in its parent class**.  
When you create an object of the child class, **the child’s method overrides (replaces)** the parent’s method.

---

## 🧠 Why Use Method Overriding?
It allows a subclass to **provide a specific implementation** of a method that is already defined in its parent class.

This is a key part of **Polymorphism** — the ability of different classes to respond differently to the same method call.

---

## ⚙️ Example

```python
class Animal:
    def sound(self):
        return "Animals make sounds"

class Dog(Animal):
    def sound(self):
        return "Dog barks"

# Creating objects
a = Animal()
d = Dog()

print(a.sound())  # Output: Animals make sounds
print(d.sound())  # Output: Dog barks
```

✅ Here,
- The `Dog` class **overrides** the `sound()` method of the `Animal` class.
- When `d.sound()` is called, Python runs the version in the `Dog` class, **not** the one in `Animal`.

---

## ⚡ Key Points
- Overriding only happens in **inheritance**.
- The **method name** and **parameters** must be **the same**.
- The **child class method** replaces the **parent class method** during runtime.
