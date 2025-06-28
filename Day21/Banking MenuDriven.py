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


class Bank:
    def __init__(self, name, city):
        self.__name = name
        self.__city = city
        self.__accounts = {}

    def create_account(self, account_id, holder_name, acc_type):
        if account_id in self.__accounts:
            print("Account ID already exists.")
            return None

        if acc_type == "savings":
            new_account = SavingsAccount(account_id, holder_name)
        elif acc_type == "current":
            new_account = CurrentAccount(account_id, holder_name)
        else:
            print("Invalid account type.")
            return None

        self.__accounts[account_id] = new_account
        print("Account creation successful.")
        return new_account

    def get_account(self, account_id):
        if account_id not in self.__accounts:
            print("Account not found.")
            return None
        acc = self.__accounts[account_id]
        print(f"\nAccount Details:\n{acc}")
        return acc


# ---- Main Menu Driven Program ----

npl = Bank("Nagarjun Bank of India", "Mandya")

while True:
    print("\n--- Welcome to Nagarjun Bank ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Calculate Interest (Savings Only)")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        acc_id = input("Enter Account ID: ")
        name = input("Enter Holder Name: ")
        acc_type = input("Enter Account Type (savings/current): ").lower()
        npl.create_account(acc_id, name, acc_type)

    elif choice == '2':
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if acc:
            amt = input("Enter amount to deposit: ")
            if amt.replace('.', '', 1).isdigit():
                acc.deposit(float(amt))
            else:
                print("Invalid input. Enter a number.")

    elif choice == '3':
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if acc:
            amt = input("Enter amount to withdraw: ")
            if amt.replace('.', '', 1).isdigit():
                acc.withdraw(float(amt))
            else:
                print("Invalid input. Enter a number.")

    elif choice == '4':
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if acc:
            acc.check_balance()

    elif choice == '5':
        acc_id = input("Enter Account ID: ")
        acc = npl.get_account(acc_id)
        if isinstance(acc, SavingsAccount):
            acc.calculate_interest()
        else:
            print("Interest calculation only for savings accounts.")

    elif choice == '6':
        print("Thank you for banking with Nagarjun Bank. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
