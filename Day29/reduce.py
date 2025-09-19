# Using reduce to sum a list of numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

result = reduce(add, numbers)
print("Sum of numbers:", result)  # Output: Sum of numbers: 15



# Using lambda function with reduce

nums = [1, 2, 3, 4, 5] + numbers
result = reduce(lambda x, y: x + y, nums) # Using lambda function with reduce
print("Sum of numbers using lambda:", result)  # Output: Sum of numbers using lambda


numbers = [10, 30, 25, 100, 5, 40, 120]

res = reduce(lambda a, b: a if a > b else b, numbers) # Using lambda function with reduce
print("Maximum number is:", res)  # Output: Maximum number is: 120