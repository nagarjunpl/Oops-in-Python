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
