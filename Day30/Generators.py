# Generators are a simple and powerful tool for creating iterators.
def gen(x):
    yield x * 2

g = gen(5)

for i in g:
    print(i)



# Example of a simple generator function
def simple_gen():
    yield 1
    yield 2
    yield 3
    yield 4

g = simple_gen()

for i in g:
    print(i)


# Example of a generator function with a loop
def simple_gen2(x1):
    for i in range(x1):
        yield i

g = simple_gen2(5)

n = 0
for i in g:
    if n > 2:
        break
    print(i)
    n += 1



# Example of using sys.getsizeof to show memory efficiency of generators
import sys

# Example of a generator expression
gl = (x * x for x in range(1, 11))
print(sys.getsizeof(gl))  # Size of the generator object
for i in gl:
    print(i)


# Infinite generator example
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_numbers()
for _ in range(10):
    print(next(gen))