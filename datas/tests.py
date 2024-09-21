class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the balance")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Create an instance of Account
account = Account("John", 500)

# Accessing public and private methods
account.deposit(200)
print("Balance:", account.get_balance())
account.withdraw(100)
print("Balance:", account.get_balance())