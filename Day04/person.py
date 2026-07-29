class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm now {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        print(f"Hi, I'm {self.name} at {self.school}. I'm now {self.age} years old now.")

person1 = Person("Jack", 13)

person1.introduce()

student1 = Student("Jerry", 23, "NEU")

student1.introduce()