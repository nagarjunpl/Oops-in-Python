# 🧩 Getters and Setters in Python

## 📘 What are Getters and Setters?
In **Object-Oriented Programming (OOP)**, **getters** and **setters** are special methods used to **access** and **modify** the values of private attributes in a class.

They help in **data encapsulation** — protecting the internal state of an object from accidental modification.

---

## 🧠 Why use them?
- To **control how data is accessed or updated**.  
- To **validate** data before changing it.  
- To **hide** internal variables from direct modification.  
- To maintain **data consistency**.

---

## 🧩 Example 1 — Without Getters and Setters

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Object creation
s1 = Student("Nagarjun", 90)

# Direct access (not safe)
print(s1.grade)   # 90
s1.grade = -10    # invalid, but allowed
print(s1.grade)   # -10 ❌
```

> The grade can be set to an invalid value — this is not safe.

---

## 🧩 Example 2 — Using Getters and Setters

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade   # private variable

    # Getter method
    def get_grade(self):
        return self.__grade

    # Setter method
    def set_grade(self, grade):
        if grade >= 0:
            self.__grade = grade
        else:
            print("Invalid grade! Grade must be positive.")

# Object creation
s1 = Student("Nagarjun", 90)

# Access using getter and setter
print(s1.get_grade())   # ✅ 90
s1.set_grade(-10)       # ❌ Invalid
s1.set_grade(95)        # ✅ Updated
print(s1.get_grade())   # ✅ 95
```

---

## 🧾 Output:
```
90
Invalid grade! Grade must be positive.
95
```

---

## ✅ Key Points
- Getters → used to **get** the value of a private variable.  
- Setters → used to **set** or **update** a private variable safely.  
- Protects data using **encapsulation**.  
- Private variables are written with **double underscores (`__`)**.

---

## 🧠 Example 3 — Using `@property` (Pythonic way)

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        if value >= 0:
            self.__grade = value
        else:
            print("Invalid grade! Must be positive.")

s1 = Student("Nagarjun", 85)
print(s1.grade)   # calls getter
s1.grade = -10    # calls setter → Invalid
s1.grade = 95     # calls setter → Valid
print(s1.grade)
```

---

## 🧾 Output:
```
85
Invalid grade! Must be positive.
95
```

---

## 🏁 Summary
- **Getters and Setters** control access to class attributes.  
- Help maintain **encapsulation and data validation**.  
- The `@property` decorator is the **Pythonic** and **cleaner** approach.
