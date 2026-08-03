from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        print(f"paid ${amount} ", end = "")

class CreditCardPayment(Payment):
    def pay(self, amount):
        super().pay(amount)
        print("by credit card")

class PayPalPayment(Payment):
    def pay(self, amount):
        super().pay(amount)
        print("by PayPal")


class CashPayment(Payment):
    def pay(self, amount):   
        super().pay(amount)
        print("in cash")

payments = [
    CreditCardPayment(),
    PayPalPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(100)