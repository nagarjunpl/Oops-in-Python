# Decorators in Python

def DecoratorExample(func):     # This is a simple decorator function
    def wrapper():
        print("This is a decorator wrapper function.")
        func()      # Call the original function
        print("Decorator has finished executing.")
    return wrapper    # Decorator function returns the wrapper function

@DecoratorExample     # This line applies the decorator to the function
def say_hello():
    print("Hello, World!")

say_hello()   # This line applies the decorator to the function



# Decorator with parameters

def adding_decorator(addition):
    def wrapper(a = "none", b = "none"):    # Default values for a and b
        a=int(input("Enter a value to add: "))
        b=int(input("Enter b values to add: "))
        print("Result after adding : ", end="")
        addition(a,b)     # Call the original function
    return wrapper       

@adding_decorator     # This line applies the decorator to the function
def add_numbers(a,b):
    print(a + b)

add_numbers()   # This line applies the decorator to the function


def loggger(func):
    def wrapper(a , b):
        print(f"Function '{func.__name__}' called with arguments: {a}, {b}")
        func(a, b)
    return wrapper

@loggger
def add(a, b):
    print(f"Sum: {a + b}")

@loggger
def subtract(a, b):
    print(f"Difference: {a - b}")

@loggger
def multiply(a, b):
    print(f"Product: {a * b}")

add(5, 3)
subtract(10, 4)
multiply(5, 3)

