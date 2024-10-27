from dotenv import load_dotenv()
from atm_rework import BankAccount, ATM

# Example Usage
if __name__ == "__main__":
    # Set the environment variable for testing
    os.environ["ACCOUNT_PIN"] = "1234"  # For testing purposes
    account = BankAccount(1000.00)  # Starting balance
    atm = ATM(account)

    if atm.validate_pin():
        atm.display_balance()
        atm.withdraw_money()