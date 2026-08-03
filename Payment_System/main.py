from notification import AppNotification
from notification import EmailNotification
from notification import SMSNotification
from payment import CreditCardPayment
from payment import PayPalPayment
from payment import CashPayment
from order import Order

order1 = Order(
    "001",
    100,
    CreditCardPayment(),
    EmailNotification()
)

order2 = Order(
    "002",
    200,
    PayPalPayment(),
    SMSNotification()
)

order3 = Order(
    "003",
    50,
    CashPayment(),
    AppNotification()
)

order1.checkout()
order2.checkout()
order3.checkout()

order1.change_payment(PayPalPayment())
order1.checkout()