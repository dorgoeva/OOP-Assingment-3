# Create an account
account = PersonalAccount(101, "Alice")

# Deposit money
account.deposit(200)
account.deposit(100)

# Withdraw money
account.withdraw(50)
account.withdraw(500)  # Should show "Not enough balance!"

# Check balance
print("\nCurrent Balance:", account.get_balance())

# Print transaction history
account.print_transaction_history()
