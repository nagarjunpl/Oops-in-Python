
# 🏗️ Python Frameworks

A **framework** is a structured environment that provides the foundation for building applications.  
The **framework controls the program flow**, and you just define parts of it.

## ✅ Example:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

app.run()
```

Here, **Flask** controls how your app runs — you just define what happens at certain routes.

## 🔹 Popular Python Frameworks
| Category | Framework | Description |
|-----------|------------|-------------|
| Web Development | Flask, Django, FastAPI | Build web apps and APIs |
| Machine Learning | TensorFlow, PyTorch | Build AI/ML models |
| GUI Development | Tkinter, Kivy | Create desktop/mobile apps |
| Testing | PyTest, Robot Framework | Automate software testing |

## ⚙️ Key Points
- Frameworks provide **structure** and **control flow**.
- You fill in specific parts (routes, models, etc.).
- They are **less flexible**, but **faster for development**.
