# Demonstrating the use of iterators in Python

numbers = [1, 2, 3]

# Using iter() to create an iterator from the list
it = iter(numbers)

print(next(it))  # Output: 1
print(next(it))  # Output: 2
print(next(it))  # Output: 3
# print(next(it))  # Raises StopIteration error


# Custom iterator class
class MyNumbers:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        num = self.start
        self.start -= 1
        return num
    
my_num = MyNumbers(5)

for i in my_num:
    print(i)