from bank import BankAccount, InsufficientFundsError


class SavingsAccount(BankAccount):
    """A bank account that also earns interest. Inherits from BankAccount."""

    def __init__(self, account_number, owner, balance=0, interest_rate=0):
        """Set up a savings account, including its annual interest rate (%)."""
        # super().__init__ runs BankAccount's initializer, which sets
        # account_number, owner and balance for us
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Add one year of interest to the balance and return the interest."""
        # A rate of 5 means 5%, so divide by 100 to get 0.05
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return interest

    def __str__(self):
        """Return the BankAccount description plus the interest rate."""
        # super().__str__() reuses the parent's text instead of rewriting it
        return f"{super().__str__()}, Interest Rate: {self.interest_rate}%"


if __name__ == "__main__":
    # Create a savings account for Bob: $1000 balance, 5% interest rate
    savings = SavingsAccount(67890, "Bob", 1000, 5)
    print("Created savings account:")
    print(savings)

    # Test 1: inherited deposit method
    print("\n--- Deposit test ---")
    savings.deposit(500)
    print("After depositing $500:")
    print(savings)

    # Test 2: inherited withdraw method
    print("\n--- Withdrawal test ---")
    new_balance = savings.withdraw(200)
    print(f"After withdrawing $200, new balance: ${new_balance:.2f}")
    print(savings)

    # Test 3: apply interest, showing the account before and after
    print("\n--- Interest test ---")
    print("Before applying interest:")
    print(savings)
    interest = savings.apply_interest()
    print(f"Interest earned: ${interest:.2f}")
    print("After applying interest:")
    print(savings)

    # Test 4: attempt to overdraw (inherited check raises our custom error)
    print("\n--- Overdraw test ---")
    try:
        savings.withdraw(5000)
    except InsufficientFundsError as error:
        print(f"Error: {error}")