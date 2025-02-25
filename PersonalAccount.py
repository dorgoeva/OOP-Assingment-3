class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0  # Initial balance is 0
        self.transactions = []  

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            transaction = Amount(amount, "DEPOSIT")
            self.transactions.append(transaction)
            print(f"Deposited ${amount}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount 
            transaction = Amount(amount, "WITHDRAWAL")
            self.transactions.append(transaction)
            print(f"Withdrew ${amount}")
        else:
            print("Not enough balance!")

    def print_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance}"
