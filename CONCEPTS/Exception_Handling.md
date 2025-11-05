# ⚠️ Exception Handling in Python

## 📘 Definition
**Exception Handling** in Python is a way to **handle errors gracefully** so that a program doesn’t crash when something goes wrong.  
It allows developers to **detect, handle, and recover** from runtime errors using special keywords.

---

## 🧠 Why Use Exception Handling?
Without exception handling, a single runtime error (like dividing by zero or opening a missing file) can **terminate the program abruptly**.  
With exception handling, you can:
- Display a meaningful error message  
- Continue program execution  
- Prevent crashes

---

## 🧩 Common Error Example

```python
# Without exception handling
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(a / b)  # ❌ Error if user enters b = 0
```
If the user enters `0`, Python throws a `ZeroDivisionError`.

---

## ✅ Using `try` and `except`

```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
```

### 🧾 Explanation
- Code inside `try` is executed first.  
- If an error occurs, the flow moves to `except` instead of crashing.  

---

## ⚙️ Handling Multiple Exceptions

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
```

You can handle **different types of errors** using multiple `except` blocks.

---

## 🔁 Using `else` and `finally`

```python
try:
    x = int(input("Enter a number: "))
    print("Result:", 10 / x)
except ZeroDivisionError:
    print("Division by zero not allowed.")
else:
    print("No errors occurred!")
finally:
    print("Program execution complete.")
```

### 🔍 Explanation
- **`else`** → runs if there is **no exception**.  
- **`finally`** → runs **every time**, whether an error occurs or not.  

---

## ⚡ Key Points
- Use **`try`** → for code that may raise an error.  
- Use **`except`** → to handle the error.  
- Use **`else`** → for code that runs if there’s **no error**.  
- Use **`finally`** → for cleanup operations (like closing files or releasing resources).  
- Helps make programs **robust and user-friendly**.  

---

## 💡 Example in Real Life
Imagine an ATM machine. If you enter an invalid PIN, it doesn’t crash — it shows “Invalid PIN, try again.”  
That’s **exception handling** in action!
