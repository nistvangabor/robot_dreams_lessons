from bank_account import BankAccount, InvalidAmountError, InsufficientFundsError
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