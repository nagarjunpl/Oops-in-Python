
# 🎀 Python Decorators – Simple Explanation

A **decorator** in Python is a special function that adds extra features to another function **without modifying its original code**.

---

## 🧠 Why Do We Use Decorators?

Decorators help in:

- Logging
- Authentication
- Timing functions
- Validating inputs
- Adding extra behavior to functions

All **without editing the actual function**.

---

## 🧩 Basic Example

```python
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
```

---

## 🎁 Applying the Decorator

```python
@my_decorator
def greet():
    print("Hello!")

greet()
```

### ✔ Output:
```
Before function runs
Hello!
After function runs
```

---

## 🧩 Decorator with Arguments

```python
def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print(a / b)

divide(10, 0)
```

---

## ⭐ Key Points

- Decorators wrap a function inside another function  
- `@decorator_name` is just shorthand  
- Used heavily in Flask, Django, and API development  
- Useful for adding repeated logic cleanly  
