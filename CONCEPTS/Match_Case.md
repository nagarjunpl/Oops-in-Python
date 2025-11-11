
# 🧩 Match-Case in Python

The **match-case** statement in Python is similar to the **switch-case** found in other languages like C or Java.  
It was introduced in **Python 3.10** to simplify checking one value against multiple possible options.

---

## 🧠 Definition
The `match` statement compares a variable’s value with several patterns defined using `case` blocks.  
When a match is found, the corresponding code block runs.

---

## ✅ Example 1: Basic Number Matching
```python
x = int(input("Enter a number: "))

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid number")
```

### 🔹 Explanation:
- `match x:` → checks the value of `x`
- `case 1:` → runs if `x` equals 1
- `case _:` → acts as a **default case** (like `else`)

---

## ✅ Example 2: String Matching
```python
day = "Monday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
```

### 🔹 Explanation:
- The `|` symbol means **“or”**.
- So multiple values can trigger the same case.

---

## ⚙️ Key Points
- Makes code **cleaner** than multiple `if-elif` statements.
- The `_` case works as a **default** case.
- Supports **pattern matching** for complex data types (like tuples and classes).

---

## 💡 Example 3: Pattern Matching with Tuples
```python
point = (2, 3)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X-axis at {x}")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, y):
        print(f"Point at coordinates ({x}, {y})")
```
