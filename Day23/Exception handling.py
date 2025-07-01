# Exception handling in Python

a = int(input("Enter A value: "))
b = int(input("Enter B value: "))

try:
    print(a/b)

except Exception as e:
    print("An error occurred:", e)

finally:
    print("This block always executes, regardless of an error.")

# Retry with a new value for B
a = int(input("Enter A value: "))
b = int(input("Enter B value: "))

try:
    print(a/b)

except Exception as e:
    print("An error occurred:", e) 
    print("Please enter valid numbers.") 
    b = int(input("Enter B value: ")) 
    print(a/b)

finally:
    print("This block always executes, regardless of an error.")


