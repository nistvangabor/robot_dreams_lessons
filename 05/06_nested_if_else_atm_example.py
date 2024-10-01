# Initial account balance
account_balance = 500.00
correct_pin = 1234

pin = input("Please enter your PIN: ")

if pin == correct_pin:
    print("PIN accepted.")
    print(f"Your current balance is: ${account_balance:.2f}")

    withdrawal_amount = float(input("Enter the amount you want to withdraw: $"))

    if withdrawal_amount > 0:
        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f"Withdrawal successful! Your new balance is: ${account_balance:.2f}")
        else:
            print("Insufficient funds for this withdrawal.")
    else:
        print("Invalid amount. Please enter a positive number.")
else:
    print("Incorrect PIN. Please try again.")


# ha így is marad idő, akkor tároljuk a pin kódot .env file-ban