# 🍴 Menu Driven Program in Python

## 📘 Definition
A **menu-driven program** is a program that allows the user to choose from a list of options (a *menu*) to perform specific tasks.  
It repeatedly shows a menu, takes user input, performs the selected operation, and continues until the user decides to exit.

---

## 🧠 Why Use Menu-Driven Programs?
They make programs **interactive and user-friendly** — especially useful for beginners, console-based apps, and systems with multiple choices like:
- Calculator
- ATM simulation
- Student management system

---

## ⚙️ Example 1: Simple Calculator (Menu-Driven Program)

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed"

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting program... Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Please select again.")
```

---

## 🧩 Explanation
- The program displays a menu with choices.
- It uses a **loop** (`while True`) to run continuously.
- Based on user input, the program performs operations using **if-elif-else**.
- The loop exits when the user selects **Exit (choice 5)**.

---

## ⚡ Key Points
- Menu-driven programs are **interactive** and **loop-based**.
- They use **functions** for modularity.
- **User input** determines which operation runs.
- **Loops and conditionals** are the core building blocks.
