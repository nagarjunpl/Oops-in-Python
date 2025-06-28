# Banking System Menu Driven Program

class Account:
    def __init__(self, account_id, holder_name):
        self.account_id = account_id
        self.holder_name = holder_name
        self._balance = 0  # encapsulation

    def check_balance(self):
        print(f"Balance: ₹{self._balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        self._balance += amount
        print(f"Deposit successful. Updated Balance: ₹{self._balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated Balance: ₹{self._balance:.2f}")
        else:
            print("Insufficient balance.")

    def __str__(self):
        return f"Account ID: {self.account_id}, Holder: {self.holder_name}, Balance: ₹{self._balance:.2f}"


class CurrentAccount(Account):  # Polymorphism
    def withdraw(self, amount):
        over_draft_limit = 1000
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if self._balance + over_draft_limit >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated Balance: ₹{self._balance:.2f}")
        else:
            print("Withdrawal amount exceeds overdraft limit.")

