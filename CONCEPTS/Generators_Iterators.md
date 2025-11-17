# Iterators and Generators

## What is an Iterator?

An **iterator** is an object that allows you to iterate through values
one at a time. It must have: - `__iter__()` method - `__next__()` method

### Example

``` python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```

## What is an Iterable?

An **iterable** is anything you can loop over. Examples: list, tuple,
string.

## Iterator vs Iterable

  Feature            Iterable      Iterator
  ------------------ ------------- -------------------------
  Has `__iter__()`   Yes           Yes
  Has `__next__()`   No            Yes
  Loop               Yes           Yes
  Examples           list, tuple   map object, file object

## What is a Generator?

A **generator** is a special iterator created with `yield`.

### Example

``` python
def my_gen():
    yield 1
    yield 2
    yield 3
```

## Generator Expression

``` python
g = (x*x for x in range(5))
print(list(g))
```

## Iterator vs Generator

  Feature      Iterator   Generator
  ------------ ---------- -----------
  Created by   iter()     yield
  Memory       More       Less
  Code         Longer     Short
