## 🔹 What is a Module?
A **module** in Python is simply a **file that contains Python code** — like functions, classes, or variables — that you can **reuse** in other programs.

📄 For example, a file named `math.py` or `my_module.py` is a **module**.

---

## 🔹 Why Use Modules?
Modules make your program:
- ✅ Easier to manage and organize.
- ✅ Reusable (use same code in multiple programs).
- ✅ Easier to debug and maintain.

---

## 🔹 Example 1: Creating a Module

Let's say you create a file called **my_module.py**:

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!
```

Now, you can import and use it in another Python file:

```python
Always show details
# main.py
import my_module

print(my_module.greet("Nagarjun"))
```

🟢 Output:

```
Hello, Nagarjun!
```

---

## 🔹 Example 2: Importing Specific Functions

```python
from my_module import greet

print(greet("Spurthi"))
```
---

## 🔹 Example 3: Using Built-in Modules

Python comes with many built-in modules.

Examples:

```python
import math
import random
import datetime
```

✅ Usage:

```python
print(math.sqrt(25))         # 5.0
print(random.randint(1, 5))  # Random number between 1 and 5
print(datetime.datetime.now()) # Current date and time
```
---

🔹 Example 4: Renaming a Module
```python
import math as m
print(m.pi)
```
---

🔹 Example 5: Viewing All Module Functions
```pyhton
import math
print(dir(math))
```
## 🔹 Types of Modules

- Built-in Modules – Provided by Python (like os, sys, math, random).

- User-defined Modules – Created by you.

- External Modules – Installed using pip (like numpy, pandas, flask).

##  🧠 Key Points:

- A module is a .py file containing code.

- You use import to use it.

- You can reuse code across multiple projects.
