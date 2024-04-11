class BankAccount:
    def __init__(self, name, account_type, balance):
        self.name = name
        self.account_type = account_type
        self._balance = balance

    def set_balance(self, amount):
        if amount < 1000:
            raise ValueError("Minimum balance should be 1000")
        self._balance = amount

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 1000:
            raise ValueError("Insufficient funds. Minimum balance should be 1000")
        self._balance -= amount

# Example usage:
try:
    account = BankAccount("John Doe", "saving", 1500)
    print("Initial balance:", account.get_balance())

    account.withdraw(500)
    print("Balance after withdrawal:", account.get_balance())

    account.deposit(1000)
    print("Balance after deposit:", account.get_balance())

    account.set_balance(2000)  # Setting balance
    print("Balance after setting:", account.get_balance())

except ValueError as e:
    print("Error:", e)
