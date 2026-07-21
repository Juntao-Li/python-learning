class Student:
#初始化
    def __init__(self, name, score):
        self.name = name
        self.score = score

#打印对象
    def __str__(self):
        return f"{self.name} : {self.score}"

#比较对象
    def __lt__(self, other):
        return self.score < other.score

    @property
    def grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "D"
    
s1 = Student("Tom", 60)
s2 = Student("Jack", 100)
print(s1)
print(s1.grade)
print(s1 < s2)

#继承
class GraduateStudent(Student):
    def __init__(self, name, score, major):
        super().__init__(name, score)
        self.major = major
    
g1 = GraduateStudent("Alice", 78, "CS")
print(g1)
print(g1.major)
