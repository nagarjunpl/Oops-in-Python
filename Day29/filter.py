# Using filter() to filter even numbers from a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(n):
    return n % 2 == 0
    
res = filter(is_even, nums)

print("Even numbers:", list(res))  # Output: Even numbers: [2, 4, 6, 8, 10]



# Using lambda function with filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x > 5, numbers) # Using lambda function with filter
print(list(result))  # Output: [6, 7, 8, 9, 10]