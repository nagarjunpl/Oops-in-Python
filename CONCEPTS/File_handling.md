# 📂 File Handling in Python

## 🔹 What is File Handling?
**File handling** in Python allows you to **create, read, write, and delete files**.  
It is an essential part of Python because it lets you **store data permanently** — unlike variables, which are temporary.

---

## 🔹 Why is File Handling Important?
- To **store data** permanently.
- To **read or modify** external data (like text files, logs, or configuration files).
- To **save program outputs** for later use.

---

## 🔹 Basic File Operations

| Mode | Description |
|------|--------------|
| `'r'` | Read (default) – opens file for reading, gives error if file doesn’t exist |
| `'w'` | Write – creates new file or overwrites existing file |
| `'a'` | Append – adds data to the end of the file |
| `'x'` | Create – creates a new file, gives error if file already exists |
| `'b'` | Binary mode (useful for images, audio, etc.) |
| `'t'` | Text mode (default) |

---

## 🔹 Syntax:
```python
file = open("filename.txt", "mode")
# perform operations
file.close()
```

---

## 🔹 Example 1: Writing to a File
```python
file = open("example.txt", "w")
file.write("Hello, this is a test file.")
file.close()
print("File written successfully.")
```

---

## 🔹 Example 2: Reading from a File
```python
file = open("example.txt", "r")
content = file.read()
print("File content:", content)
file.close()
```

---

## 🔹 Example 3: Using `with` Statement (Best Practice)
```python
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```
✅ You don’t need to close the file manually when using `with`.

---

## 🔹 Example 4: Appending to a File
```python
with open("example.txt", "a") as file:
    file.write("\nThis line is appended.")
```

---

## 🔹 Example 5: Reading Line by Line
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

## 🔹 Key Points:
- Always close the file (or use `with`).
- Handle exceptions using `try-except` when working with files.
- Use correct file modes for reading, writing, or appending.
