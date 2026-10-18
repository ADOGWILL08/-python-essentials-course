class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the account balance."""
    pass


class BankAccount:
    """A simple bank account that tracks an owner and a balance."""

    def __init__(self, account_number, owner, balance=0):
        """Set up a new account with its starting values."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account. Only positive amounts are allowed."""
        # Reject zero or negative deposits by raising an error
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Remove money from the account if there are enough funds."""
        # Reject zero or negative withdrawal amounts
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        # Reject withdrawals bigger than the balance (overdraft) using
        # our custom exception instead of a plain ValueError
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: cannot withdraw ${amount:.2f} "
                f"from account {self.account_number}."
            )
        self.balance -= amount
        return self.balance

    def __str__(self):
        """Return a readable description of the account."""
        return (
            f"Account {self.account_number} - Owner: {self.owner}, "
            f"Balance: ${self.balance:.2f}"
        )


if __name__ == "__main__":
    # Create an account for Alice with a starting balance of $500
    account = BankAccount(12345, "Alice", 500)
    print("Created account:")
    print(account)

    # Test 1: successful deposit
    print("\n--- Deposit test ---")
    account.deposit(200)
    print("After depositing $200:")
    print(account)

    # Test 2: successful withdrawal
    print("\n--- Withdrawal test ---")
    new_balance = account.withdraw(150)
    print(f"After withdrawing $150, new balance: ${new_balance:.2f}")
    print(account)

    # Test 3: attempt to overdraw (should raise our custom exception)
    print("\n--- Overdraw test ---")
    try:
        account.withdraw(10000)
    except InsufficientFundsError as error:
        print(f"Error: {error}")

    # Test 4: attempt a negative deposit (should raise and catch an error)
    print("\n--- Invalid deposit test ---")
    try:
        account.deposit(-50)
    except ValueError as error:
        print(f"Error: {error}")