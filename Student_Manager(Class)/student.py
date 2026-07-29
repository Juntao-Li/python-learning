class Student:
    def __init__(self, name, sid, math, english, history):
        self.name = name
        self.sid = sid
        self.math = math
        self.english = english
        self.history = history

    def average(self):
        return (self.math + self.english + self.history) / 3

    def __str__(self):
        return f"name:{self.name}\nsid:{self.sid}\nmath:{self.math}\nenglish:{self.english}\nhistory:{self.history}"

if __name__ == "__main__":
    student1 = Student("Jack", "001", 98, 73, 83)
    print(student1)
    print(f"Average score:{student1.average()}")
