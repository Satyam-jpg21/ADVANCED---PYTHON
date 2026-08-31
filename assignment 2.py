from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")


# Concrete Strategy 2
class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Debit Card.")


# Concrete Strategy 3
class UpiPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using UPI.")


# Context Class
class PaymentProcessor:

    def __init__(self):
        self.strategy = None

    def set_payment_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):

        if self.strategy is None:
            print("Please select a payment method first.")
        else:
            self.strategy.pay(amount)


def main():

    processor = PaymentProcessor()

    while True:

        print("\n========== PAYMENT MENU ==========")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "4":
            print("Thank You!")
            break

        amount = float(input("Enter Payment Amount: "))

        if choice == "1":
            processor.set_payment_strategy(CreditCardPayment())

        elif choice == "2":
            processor.set_payment_strategy(DebitCardPayment())

        elif choice == "3":
            processor.set_payment_strategy(UpiPayment())

        else:
            print("Invalid Choice!")
            continue

        processor.process_payment(amount)


if __name__ == "__main__":
    main()