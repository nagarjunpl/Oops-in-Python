# Abstraction

class Car:
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def drive(self):
        print("Car is driving")

car = Car()
car.start()  # Output: Car started
car.drive()  # Output: Car is driving
car.stop()   # Output: Car stopped


# abstraction with methods
l = [1, 2, 3, 4, 5]

l.append(7) # Adding an element to the list
l.insert(2, 6) # Inserting an element at a specific position
print(l)


# Encapsulation

class ATM:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def balance(self):
        print(self.__balance)
    
npl = ATM(1000)

print(npl.balance())  # Output: 1000


class Database:
    def __init__(self):
        self.storage = {}  # Public variable

    def write(self, key, value):
        self.storage[key] = value  # Public method to write data

    def read(self, key):
        print(self.storage.get(key, "Key not found"))
    
db = Database()

db.write("name", "Nagarjun")  # Writing data to the database
db.read("name")  
