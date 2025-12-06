class BankAccount:
    def __init__(self):
        self.__balance = 0      # Private attribute (encapsulated)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.__balance += amount
        print("amount depsited")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        print("amount withdrawn")

    def get_balance(self):
        return self.__balance   # Controlled access


omer = BankAccount()

print(omer.get_balance())
omer.deposit(1000)
omer.withdraw(500)
print(omer.get_balance())
