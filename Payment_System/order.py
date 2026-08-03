class Order:
    def __init__(self, order_id, amount, payment, notification):
        self.order_id = order_id
        self.amount = amount
        self.payment = payment
        self.notification = notification

    def checkout(self):
        print(f"Order Id:{self.order_id}")
        self.payment.pay(self.amount)
        self.notification.send(f"Order {self.order_id} Completed.")

    def change_payment(self, payment):
        self.payment = payment
        
        
