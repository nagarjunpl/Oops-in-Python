
# Constructors in Python

In Python, a **constructor** is a special method (`__init__`) that is automatically called when an object of a class is created. Its main purpose is to **initialize the object’s attributes**.

---

## 🔹 Types of Constructors in Python

### 1. Default Constructor
- A constructor **without parameters** (other than `self`).
- Initializes with default values.

```python
class Student:
    def __init__(self):     # default constructor
        self.name = "Unknown"
        self.age = 0

s1 = Student()
print(s1.name, s1.age)   # Output: Unknown 0
```

---

### 2. Parameterized Constructor
- Accepts arguments to initialize object attributes.

```python
class Student:
    def __init__(self, name, age):   # parameterized constructor
        self.name = name
        self.age = age

s1 = Student("Nagarjun", 21)
s2 = Student("arjun", 20)

print(s1.name, s1.age)   # Output: Nagarjun 21
print(s2.name, s2.age)   # Output: arjun 20
```

---

### 3. Constructor with Default Arguments (Flexible Constructor)
- Uses default parameter values.
- Works both with and without arguments.

```python
class Student:
    def __init__(self, name="Unknown", age=0): 
        self.name = name
        self.age = age

s1 = Student()  
s2 = Student("Nagarjun")  
s3 = Student("arjun", 20)

print(s1.name, s1.age)   # Output: Unknown 0
print(s2.name, s2.age)   # Output: Nagarjun 0
print(s3.name, s3.age)   # Output: arjun 20
```

---

## ⚡ Quick Summary
- **Default constructor** → no parameters, initializes with fixed values.  
- **Parameterized constructor** → takes arguments, initializes with given values.  
- **Flexible constructor** → uses default arguments to support both cases.  

---
