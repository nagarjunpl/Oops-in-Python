
# Constructors in Python

In Python, a **constructor** is a special method that is automatically called when an object of a class is created.  
Its main purpose is to **initialize the object’s attributes** (i.e., give them default or initial values).  

The constructor method in Python is defined using `__init__`.

---

## ✅ Syntax of Constructor
```python
class ClassName:
    def __init__(self, parameters):
        # initialization code
```

- `__init__` → special method (called automatically during object creation).  
- `self` → represents the current instance of the class (must always be the first parameter).  
- `parameters` → values passed when creating an object.  

---

## ✅ Example
```python
class Student:
    def __init__(self, name, age):   # constructor
        self.name = name            # initializing attribute
        self.age = age

# Creating objects
s1 = Student("Nagarjun", 21)
s2 = Student("arjun", 20)

print(s1.name, s1.age)  # Output: Nagarjun 21
print(s2.name, s2.age)  # Output: arjun 20
```

### Step by Step:
1. `s1 = Student("Nagarjun", 21)` is executed.  
2. Python automatically calls `__init__` with `self = s1`, `name = "Nagarjun"`, `age = 21`.  
3. Inside `__init__`, attributes `self.name` and `self.age` are created for the object.  
4. Now, the object has its own data.  

---

## ✅ Key Points
- A class can have only **one `__init__` constructor**, but you can use default arguments to make it flexible.  
- If no constructor is defined, Python provides a **default constructor** that does nothing.  
- The constructor runs **once per object** (when it is created).  



