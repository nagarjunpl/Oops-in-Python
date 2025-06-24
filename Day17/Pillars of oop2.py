# Inheritance

class user:
    def __init__(self, username):
        self.username = username
        
    def login(self):
        print(f"{self.username} Logged in")

class admin(user): # inherit the user class
    def delete(self):
        print("Admin deleted the user")

np = admin("Arjun")

np.login()
np.delete()

# Multiple Inheritance
class Family:
    def __init__(self, username):
        self.username = username

class parent(Family):
    def par(self):
        print("Parent")

class Child(parent):
    def child(self):
        print("child")

s = Child("Gowda")

s.par()
s.child()


# Polymorphism

class Notification:
    def send(self):
        print("NOTIFICATION SENT")

class EmailNotification(Notification):
    def send(self):
        print("EMAIL SENT")

class SMSNotification(Notification):
    def send(self):
        print("SMS SENT")

n1 = Notification()
n2 = EmailNotification()
n3 = SMSNotification()

n1.send()  # Output: NOTIFICATION SENT
n2.send()  # Output: EMAIL SENT
n3.send()  # Output: SMS SENT

# Polymorphism with payment system
class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ₹{amount}")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ₹{amount} with 2% fee")
        total = amount + (amount * 0.02)
        print(f"Total charged: ₹{total:.2f}")    

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ₹{amount} with ₹15 fixed fee")
        total = amount + 15
        print(f"Total charged: ₹{total:.2f}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ₹{amount} with no extra fee")
        print(f"Total charged: ₹{amount:.2f}")

# Creating objects
p1 = CreditCardPayment()
p2 = PayPalPayment()
p3 = UPIPayment()

# Calling the overridden method
p1.process_payment(1000)
p2.process_payment(1000)
p3.process_payment(1000)
