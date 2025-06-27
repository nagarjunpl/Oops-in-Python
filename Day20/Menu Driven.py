# Simple Calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def menu():
    print("### Simple Calculator")
    
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")
    print("5. Quit")

while True:
    menu()

    choice = int(input("Enter your choice : "))

    if choice in {1,2,3,4}:
        a = int(input("Enter value of A : "))
        b = int(input("Enter value of B : "))

    if choice == 1:
        print("Result = ",add(a,b))

    elif choice == 2:
        print("Result = ",sub(a,b))

    elif choice == 3:
        print("Result = ",mul(a,b))

    elif choice == 4:
        print("Result = ",div(a,b))

    elif choice == 5 :
        print("Quitting...")
        break

    else:
        print("Invalid choice. Try again!!!")