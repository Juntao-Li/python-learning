class Student:
    # 姓名, 学号, 三门课程成绩
    def __init__(self, name, num, scores):
        self.name = name
        self.num = num
        self.scores = scores

    # 输出学生信息
    def __str__(self):
        return f"{self.num} : {self.name}"
    
    @property
    # 计算平均分
    def average(self):
        total = 0
        for scores in self.scores:
            total += scores
        average_score = total / len(self.scores)
        return average_score

    @property
    # 判断是否及格
    def is_pass(self):
        pass_flag = 0
        for scores in range(len(self.scores)):
            if self.scores[scores] < 60:
                pass_flag += 1
        if pass_flag == 0:
            return True
        else:
            return False

Tom = Student(
    "Tom",
    "001",
    [90, 88, 95]
)
print(Tom.average)
print(Tom.is_pass)
print(Tom)