class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initializes the account_balance with an optional initial balance.
        Defaults to zero if no value is provided.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the amount if funds are sufficient.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")