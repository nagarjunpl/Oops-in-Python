# 🧩 Abstract Class in Python

## 📘 Definition
An **abstract class** in Python is a class that **cannot be instantiated directly** — it’s meant to be a **blueprint for other classes**.  
It defines **abstract methods** (methods without implementation) that **must** be implemented by its subclasses.

---

## 🧠 Why Use Abstract Classes?
They are used when you want to **enforce a common structure** for all subclasses.  
For example, if multiple classes share the same method names but have **different implementations**, an abstract class ensures they all define those methods.

---

## 🧰 How to Create an Abstract Class
In Python, abstract classes are defined using the `abc` (Abstract Base Class) module.

---

## ⚙️ Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass   # No implementation — subclasses must define this method

class Dog(Animal):
    def sound(self):
        return "Dog barks"

class Cat(Animal):
    def sound(self):
        return "Cat meows"

# a = Animal()  # ❌ Error: Can't instantiate abstract class
d = Dog()
c = Cat()

print(d.sound())  # Output: Dog barks
print(c.sound())  # Output: Cat meows
```

✅ **Explanation:**
- `Animal` is an **abstract class**.
- The `sound()` method is **abstract** and must be implemented by subclasses (`Dog`, `Cat`).
- Trying to create an object of `Animal` directly will cause an **error**.

---

## ⚡ Key Points
- Abstract classes are defined using `from abc import ABC, abstractmethod`.
- You **cannot create** objects of abstract classes.
- Subclasses **must** implement all abstract methods.
- Helps ensure **code consistency** across related classes.
