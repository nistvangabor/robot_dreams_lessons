from abc import ABC, abstractmethod

# Abstract class
class PaymentProcessor(ABC):
    @abstractmethod
    def initialize_payment(self, amount: float):
        """Initialize the payment process for the given amount."""
        pass

    @abstractmethod
    def process_payment(self):
        """Process the payment."""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str):
        """Refund a payment using the transaction ID."""
        pass

# Subclass for Credit Card Payment
class CreditCardProcessor(PaymentProcessor):
    def __init__(self):
        self.amount = 0.0
        self.transaction_id = ""

    def initialize_payment(self, amount: float):
        self.amount = amount
        print(f"CreditCardProcessor: Initialized payment of ${self.amount:.2f}.")

    def process_payment(self):
        self.transaction_id = "CC" + str(int(self.amount * 1000))  # Simple mock transaction ID
        print(f"CreditCardProcessor: Processed payment of ${self.amount:.2f}. Transaction ID: {self.transaction_id}")

    def refund_payment(self, transaction_id: str):
        if transaction_id == self.transaction_id:
            print(f"CreditCardProcessor: Refunded payment of ${self.amount:.2f}. Transaction ID: {transaction_id}")
        else:
            print(f"CreditCardProcessor: Refund failed. Transaction ID {transaction_id} not found.")

# Subclass for PayPal Payment
class PayPalProcessor(PaymentProcessor):
    def __init__(self):
        self.amount = 0.0
        self.transaction_id = ""

    def initialize_payment(self, amount: float):
        self.amount = amount
        print(f"PayPalProcessor: Initialized payment of ${self.amount:.2f}.")

    def process_payment(self):
        self.transaction_id = "PP" + str(int(self.amount * 1000))  # Simple mock transaction ID
        print(f"PayPalProcessor: Processed payment of ${self.amount:.2f}. Transaction ID: {self.transaction_id}")

    def refund_payment(self, transaction_id: str):
        if transaction_id == self.transaction_id:
            print(f"PayPalProcessor: Refunded payment of ${self.amount:.2f}. Transaction ID: {transaction_id}")
        else:
            print(f"PayPalProcessor: Refund failed. Transaction ID {transaction_id} not found.")

# Subclass for Bitcoin Payment
class BitcoinProcessor(PaymentProcessor):
    def __init__(self):
        self.amount = 0.0
        self.transaction_id = ""

    def initialize_payment(self, amount: float):
        self.amount = amount
        print(f"BitcoinProcessor: Initialized payment of ${self.amount:.2f}.")

    def process_payment(self):
        self.transaction_id = "BTC" + str(int(self.amount * 1000))  # Simple mock transaction ID
        print(f"BitcoinProcessor: Processed payment of ${self.amount:.2f}. Transaction ID: {self.transaction_id}")

    def refund_payment(self, transaction_id: str):
        if transaction_id == self.transaction_id:
            print(f"BitcoinProcessor: Refunded payment of ${self.amount:.2f}. Transaction ID: {transaction_id}")
        else:
            print(f"BitcoinProcessor: Refund failed. Transaction ID {transaction_id} not found.")

# Usage
def main():
    payment_processors = [
        CreditCardProcessor(),
        PayPalProcessor(),
        BitcoinProcessor()
    ]

    # Initialize and process payments
    for processor in payment_processors:
        processor.initialize_payment(100.0)  # Initialize with $100
        processor.process_payment()
        processor.refund_payment(processor.transaction_id)  # Refund the payment

if __name__ == "__main__":
    main()