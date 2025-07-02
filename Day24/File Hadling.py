# Reading a file in Python

file = open("Day24/testing.py", "r")  # Opening the file in read mode

content = file.readline()  # Reading the first line of the file
print(content)

content = file.readlines() # Reading all lines of the file
print(content)

file.close() # Opening a file in write mode to create a new file or overwrite an existing one


# writing to a file
file1 = open("Day24/CreateFile.py", "w")  # Opening the file in write mode

file1.write("print('This is a new file created for testing file handling in Python.')\n")  # Writing to the file

file.close()  # Closing the file


# Appending to a file

file2 = open("Day24/appendfile.py", "a")  # Opening the file in append mode

file2.write("print('After deleting')\n")  # Appending to the file

file2.close()  # Closing the file


# x mode (exclusive creation)

file2 = open("Day24/appendfile.py", "x")  # Opening the file in exclusive creation mode

file2.write("print('After deleting')\n")  # Appending to the file

file2.close()  # Closing the file


# x mode using exception handling
file3 = None  # Initialize file3 to None
try:
    file3 = open("Day24/appendfile.py", "r")
    file3.write("print('Already created')\n")  # Appending to the file

except Exception as e:
    print(f"Error: {e}")

finally:
    if file3:
        file3.close()