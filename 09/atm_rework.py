import os

class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount. It must be greater than zero."
        if amount > self._balance:
            return "Insufficient funds for this withdrawal."
        self._balance -= amount  # Correctly update the protected balance
        return f"Withdrawal successful! Your new balance is: ${self._balance:.2f}"

class ATM:
    def __init__(self, account):
        self.account = account

    def read_pin(self):
        # Simulate reading the PIN from a secure source (e.g., card or secure storage)
        return os.getenv("ACCOUNT_PIN")

    def validate_pin(self):
        entered_pin = input("Please enter your PIN: ")
        correct_pin = self.read_pin()  # Read the PIN from the simulated secure source
        if correct_pin and correct_pin == entered_pin:
            print("PIN accepted.")
            return True
        else:
            print("Incorrect PIN. Please try again.")
            return False

    def display_balance(self):
        print(f"Your current balance is: ${self.account.get_balance():.2f}")

    def withdraw_money(self):
        withdrawal_amount = input("Enter the amount you want to withdraw: $")
        
        # Validate input and convert to float
        try:
            withdrawal_amount = float(withdrawal_amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return

        # Validate withdrawal amount
        if withdrawal_amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            return

        # Proceed with withdrawal
        result = self.account.withdraw(withdrawal_amount)
        print(result)

# Example Usage
if __name__ == "__main__":
    # Set the environment variable for testing
    os.environ["ACCOUNT_PIN"] = "1234"  # For testing purposes
    account = BankAccount(1000.00)  # Starting balance
    atm = ATM(account)

    if atm.validate_pin():
        atm.display_balance()
        atm.withdraw_money()