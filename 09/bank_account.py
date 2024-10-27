import datetime

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class InvalidAmountError(Exception):
    """Custom exception for invalid transaction amounts."""
    pass

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder  # Account holder's name
        self.account_number = account_number  # Unique account number
        self._balance = balance               # Starting balance (protected attribute)
        self._transactions = []               # List to store transaction history

    def deposit(self, amount):
        """Add money to the account and log the transaction."""
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self._balance += amount
        self._record_transaction("Deposit", amount)
        return True  # Indicate success

    def withdraw(self, amount):
        """Withdraw money from the account and log the transaction."""
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self._balance -= amount
        self._record_transaction("Withdrawal", amount)
        return True  # Indicate success

    def get_balance(self):
        """Display the current balance."""
        return f"Current balance: ${self._balance:.2f}"

    def _record_transaction(self, transaction_type, amount):
        """Private method to record each transaction."""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self._transactions.append(transaction)

    def get_transaction_history(self):
        """Display all recorded transactions."""
        if not self._transactions:
            return "No transactions available."
        
        history = f"Transaction history for {self.account_holder} (Account: {self.account_number}):\n"
        for transaction in self._transactions:
            history += (f"{transaction['date']} - {transaction['type']}: "
                        f"${transaction['amount']:.2f}\n")
        return history

# Example Usage
if __name__ == "__main__":
    # Create a new bank account with an initial balance
    account = BankAccount("John Doe", "123456789", balance=500.00)
    
    # Perform transactions with exception handling
    try:
        print(account.get_balance())            # Display initial balance
        if account.deposit(200):
            print("Deposit successful!")        # Check for success
        if account.withdraw(700):                # Attempt to withdraw more than balance
            print("Withdrawal successful!")      # Check for success
    except InvalidAmountError as e:
        print(f"Transaction error: {e}")
    except InsufficientFundsError as e:
        print(f"Transaction error: {e}")
    
    print(account.get_balance())                # Display final balance
    print(account.get_transaction_history())     # Display transaction history