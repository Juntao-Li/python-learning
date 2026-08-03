class EmailNotification:
    def send(self, message):
        print(message)

class SMSNotification:
    def send(self, message):
        print(message)

class AppNotification:
    def send(self, message):
        print(message)

if __name__ == "__main__":
    message = f"Order Completed."

    EmailNotification().send(message)
    SMSNotification().send(message)
    AppNotification().send(message)
