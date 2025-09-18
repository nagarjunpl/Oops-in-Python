# Using map to apply a function to each item in an iterable

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

res = map(square, numbers)
print(list(res))  # Output: [1, 4, 9, 16, 25]



# Using lambda function with map
nums = [1, 2, 3, 4, 5]
result = map(lambda x: x * x, nums) # Using lambda function with map
print(list(result))  # Output: [1, 4, 9, 16, 25]


# Using map with multiple iterables
a = [1, 2, 3]
b = [1, 2, 0]

result = map(lambda x, y: x + y, a, b) # Using lambda function with map
print(list(result))  # Output: [2, 4, 3]