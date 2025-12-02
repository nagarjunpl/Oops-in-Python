# Virtual Environment in Python

## What is a Virtual Environment?

A **virtual environment (venv)** is an isolated Python workspace where
each project can have its own dependencies without affecting other
projects.

------------------------------------------------------------------------

## Why Use a Virtual Environment?

### 1. Avoid Version Conflicts

Each project can use different versions of libraries like Django, Flask,
NumPy, etc.

### 2. Keeps System Clean

Packages install inside the environment, not in system Python.

### 3. Safe and Reproducible Projects

Easier deployment and debugging.

------------------------------------------------------------------------

## How to Create and Use a Virtual Environment

### ✔ Step 1 --- Create

``` bash
python -m venv myenv
```

### ✔ Step 2 --- Activate

**Windows**

``` bash
myenv\Scripts\activate
```

**Mac/Linux**

``` bash
source myenv/bin/activate
```

You will see:

    (myenv)

### ✔ Step 3 --- Install Packages

``` bash
pip install django
```

### ✔ Step 4 --- Deactivate

``` bash
deactivate
```

------------------------------------------------------------------------

## Interview Definition

A **virtual environment** is an isolated Python directory that contains
its own interpreter and libraries, allowing projects to manage
dependencies independently.
