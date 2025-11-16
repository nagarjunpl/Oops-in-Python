# filter()

`filter()` is a built-in Python function used to filter elements from an iterable based on a given condition.

## Syntax
```python
filter(function, iterable)
```

## How it works
- **function**: A function that returns True or False.
- **iterable**: A list, tuple, or any iterable.
- Only elements for which the function returns **True** are kept.

## Example 1: Filter even numbers
```python
nums = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))  # [2, 4, 6]
```

## Example 2: Filter names longer than 5 characters
```python
names = ["Naga", "Raju", "Mahesh", "Kiran Kumar"]
result = filter(lambda n: len(n) > 5, names)
print(list(result))  # ['Mahesh', 'Kiran Kumar']
```

## Example 3: Filter positive numbers
```python
nums = [-2, 0, 3, -4, 5]
positives = filter(lambda x: x > 0, nums)
print(list(positives))  # [3, 5]
```

## filter() vs map()
| Feature | filter() | map() |
|--------|----------|--------|
| Purpose | Select items | Transform items |
| Function returns | True/False | Any value |
| Output size | Smaller or equal | Same size |

## Interview definition
**`filter()` selects elements from an iterable based on a condition and returns only those elements that satisfy the condition.**

