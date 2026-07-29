class Student:
    count = 0 

    def __init__(self, name, sid, score):
        self.name = name
        self.sid = sid
        self.score = score
        Student.count += 1

    def __str__(self):
        return f"{self.sid} - {self.name}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.sid == other.sid

    def __len__(self):
        return len(self.name)

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def is_pass(score):
        return 60 <= score <= 100

student1 = Student("Tom", "001", 98)
print(student1)

student2 = Student("John", "001", 78)
print(student1 == student2)

student3 = Student("Alice", "002", 54)
print(student1 == student3)
print(student2 == student3)

print(len(student1))
print(len(student2))
print(len(student3))

print(Student.get_count())

print(student1.is_pass(student1.score))
print(student3.is_pass(student3.score))

print(Student.is_pass(55))