class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        if self.__balance >= 0:
            return self.__balance
        else:
            return "Balance Invalid!"

    def deposit(self):
        try:
            value = int(input("Input the number of money you want to deposit:"))
            if value <= 0:
                print("Input the number of money more than 0!")
            else:
                self.__balance += value
        except ValueError:
            print("Please input integer!")

ba = BankAccount(100)

print(ba.balance)

ba.deposit()

print(ba.balance)