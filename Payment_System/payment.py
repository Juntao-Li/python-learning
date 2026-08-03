from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Pay {amount} by creditcard")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Pay {amount} by paypal")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Pay {amount} in cash")



