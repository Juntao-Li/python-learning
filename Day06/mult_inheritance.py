class Flyable:
    def fly(self):
        print("Fly")

class Swimmable:
    def swim(self):
        print("Swim")

class Animal:
    def eat(self):
        print("Eat")

class Duck(Animal, Flyable, Swimmable):
    pass

duck = Duck()

duck.eat()
duck.fly()
duck.swim()

print(Duck.mro())

class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass


class D(B, A):
    pass

C().show()
D().show()

class C(A, B):
    def show(self):
        print("C", end = "")
        super().show()

C().show()



