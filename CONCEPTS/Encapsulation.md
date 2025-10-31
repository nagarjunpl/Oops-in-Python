
# 🐍 Encapsulation in Python

**Encapsulation** in Python (and in Object-Oriented Programming) means **binding data and methods together into a single unit** — usually a **class** — and **restricting direct access** to some parts of that object.  

It helps to **protect data** from accidental modification and keeps your code **organized, secure, and easier to maintain**.

---

## 🧠 Simple Definition  
Encapsulation = **Data hiding + Data protection**

---

## 💡 Example Without Encapsulation

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Nagarjun", 85)
print(s1.marks)   # Anyone can access and change marks
s1.marks = 30     # Changing directly
print(s1.marks)
```

👉 Here, anyone can change `marks` from **outside** the class — this is **not safe**.

---

## 💡 Example With Encapsulation

```python
class Student:
    def __init__(self, name, marks):
        self.__name = name      # private variable
        self.__marks = marks    # private variable

    def get_marks(self):
        return self.__marks     # getter method

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

s1 = Student("Nagarjun", 85)
print(s1.get_marks())   # Accessing through getter

s1.set_marks(95)        # Modifying safely through setter
print(s1.get_marks())

s1.set_marks(120)       # Invalid input → blocked
```

---

## 🧩 Explanation

- `__marks` → double underscore makes it **private** (cannot be accessed directly)  
- `get_marks()` → **getter method** (used to view data)  
- `set_marks()` → **setter method** (used to modify data safely)

---

## ⚙️ Advantages of Encapsulation

✅ Protects data (can’t be modified directly)  
✅ Makes code easier to maintain and debug  
✅ Controls how data is accessed or changed  
✅ Increases modularity and reusability  

---

## 🔐 Access Modifiers in Python

| Type | Syntax | Access |
|------|---------|---------|
| **Public** | `name` | Accessible from anywhere |
| **Protected** | `_name` | Accessible within the class and subclasses |
| **Private** | `__name` | Accessible only inside the class |

---
