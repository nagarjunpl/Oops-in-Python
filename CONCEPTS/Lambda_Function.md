
# ⚡ Lambda Function in Python

A **lambda function** in Python is a short, anonymous function defined using the `lambda` keyword.  
It is used when you need a simple function for a short period of time.

---

## 🧠 Syntax

```python
lambda arguments: expression
```

- Anonymous (no name)
- Can take multiple arguments
- Must contain only **one expression**
- Automatically returns the expression result

---

## ✅ Example 1: Simple Lambda

```python
square = lambda x: x * x
print(square(5))
```

### ✔ Output:
```
25
```

---

## ✅ Example 2: Lambda with Multiple Arguments

```python
add = lambda a, b: a + b
print(add(3, 4))
```

### ✔ Output:
```
7
```

---

## 🎯 Where Are Lambda Functions Used?

Lambda functions are commonly used with:

- `map()`
- `filter()`
- `sorted()`
- As small inline functions

---

## 🧩 Example with map()

```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
```

### ✔ Output:
```
[2, 4, 6, 8]
```

---

## 🧩 Example with filter()

```python
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)
```

### ✔ Output:
```
[2, 4, 6]
```

---

## ⭐ Key Points

- Lambda functions are anonymous  
- Only one expression allowed  
- Useful for short, quick operations  
- Often used inside map(), filter(), sorted()  

