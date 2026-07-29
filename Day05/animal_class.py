class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("Check stamina")

class Dog(Animal):
    def move(self):
        super().move()
        print(f"{self.name} is running.")

class Bird(Animal):
    def move(self):
        super().move()
        print(f"{self.name} is flying.")

animal1 = Animal("animal1")
animal1.move()

dog1 = Dog("Lucky")
dog1.move()

bird1 = Bird("Love")
bird1.move()
