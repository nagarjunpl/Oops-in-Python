   A **custom exception** in Python is an error defined by the user, not a built-in one like ValueError or ZeroDivisionError.

👉 Sometimes, built-in exceptions don’t describe the specific problem in your program — so you create your own exception class using inheritance.

---
## 🔹 Syntax:
```python
class MyCustomError(Exception):
    pass
```
---
## 🔹 Example:
```python
class AgeTooLowError(Exception):
    """Raised when age is below 18"""
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooLowError("You must be 18 or older to vote.")
    else:
        print("You are eligible to vote.")
except AgeTooLowError as e:
    print("Error:", e)
```
---
## 🔹 Output:
```
Enter your age: 15
Error: You must be 18 or older to vote.
```
## 🔹 Explanation:

- You define a class that inherits from Exception.

- You raise it using the raise keyword.

- You can catch it with except.

