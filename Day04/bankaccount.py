class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Balance not enough!")
        else:
            self.balance = self.balance - amount

    def show_balance(self):
        print(f"Owner:{self.owner}")
        print(f"Balance:{self.balance}")

if __name__ == "__main__":
    bankaccount1 = BankAccount("Jack", 50)
    bankaccount1.withdraw(100)
    bankaccount1.show_balance()
    bankaccount1.deposit(100)
    bankaccount1.show_balance()
    bankaccount1.withdraw(50)
    bankaccount1.show_balance()
    