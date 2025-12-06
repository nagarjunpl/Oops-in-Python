# Context Manager in Python

A **Context Manager** in Python is a construct that helps manage resources such as files, database connections, or network connections safely and efficiently.

It ensures that resources are **properly opened** and **automatically cleaned up** after use — even if an error occurs.

---

## ✅ Simple Definition
A **context manager** sets up something before a block of code runs and cleans it up automatically when the block finishes.

You use it with the **`with` keyword**.

---

## 📌 Why Use Context Managers?
- Prevent resource leaks
- Make code cleaner and safer
- Automatically handle setup and teardown
- Especially useful for files, locks, and network resources

---

## ✔️ Example: File Handling
```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### What happens?
- File opens
- Code inside the `with` block executes
- File closes automatically — even if an error occurs

---

## 🛠 Creating a Custom Context Manager (Using Class)
```python
class MyContext:
    def __enter__(self):
        print("Entering context...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context...")

with MyContext():
    print("Inside the block")
```

---

## 🔑 Key Points
- Uses `with` keyword
- Uses two special methods:
  - `__enter__()` → runs at the start
  - `__exit__()` → runs at the end
- Makes resource management clean and error-free

---

## 🧠 Short Definition
A context manager is a tool that **manages setup and cleanup actions automatically** using the `with` keyword.
