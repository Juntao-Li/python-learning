class Student:
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        if 0 <= self.__score <= 100:
            return self.__score
        else:
            return "Score Must be Between 0 and 100!"

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            print("Original Score Invalid!")

if __name__ == "__main__":

    student1 = Student(97)

    print(student1.score)

    student1.score = 88

    print(student1.score)

    student2 = Student(135)

    print(student2.score)

    student2.score = 60
