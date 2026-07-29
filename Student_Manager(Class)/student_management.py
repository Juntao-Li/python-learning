from student import Student

class Student_Management:
    def __init__(self, file_name):
        self.students = []
        self.file_name = file_name

    def load_students(self):
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                student = Student(data[0], data[1], int(data[2]), int(data[3]), int(data[4]))
                self.students.append(student)

    def add_student(self):
        name = input("Input the name:")
        while True:
            sid = input("Input the sid(000):")
            for student in self.students:
                if sid == student.sid:
                    print("SID existed!")
                    break
            else:
                break

        while True:
            try:
                math = int(input("Input the score of math:"))
                english = int(input("Input the score of english:"))
                history = int(input("Input the score of history:"))
                break
            except ValueError:
                print("Must be integer!")
        student = Student(name, sid, math, english, history)
        self.students.append(student)

    def save_student(self):
        with open(self.file_name, "w") as file:
            for student in self.students:
                file.write(f"{student.name},{student.sid},{student.math},{student.english},{student.history}\n")

    def update_student(self):
        sid = input("Input the sid of student you want to update:")
        for student in self.students:
            if sid == student.sid:
                while True:
                    print("1.name")
                    print("2.math score")
                    print("3.english score")
                    print("4.history score")
                    print("5.exit")
                    num = int(input("What do you want to change:"))
                    if num == 1:
                        student.name = input("Input the name:")
                    elif num == 2:
                        student.math = int(input("Input the math score:"))
                    elif num == 3:
                        student.english = int(input("Input the english score:"))
                    elif num == 4:
                        student.history = int(input("Input the history score:"))
                    elif num == 5:
                        break

    def show_student(self):
        sid = input("Input the sid of student you want to show:")
        for student in self.students:
            if sid == student.sid:
                print(f"name:{student.name}\nsid:{student.sid}\nmath:{student.math}\nenglish:{student.english}\nhistory:{student.history}")

    def show_all_student(self):
        print("-" * 42)
        for student in self.students:
            print(f"name:{student.name}\nsid:{student.sid}\nmath:{student.math}\nenglish:{student.english}\nhistory:{student.history}")
            print("-" * 42)

    def del_student(self):
        sid = input("Input the sid of the student you want to delete:")
        for student in self.students:
            if student.sid == sid:
                self.students.remove(student)
                print("Delete successfully!")
                break
        else:
            print("Student not found!")

if __name__ == "__main__":
    student_management1 = Student_Management("class1.txt")
    student_management1.load_students()
    student_management1.add_student()
    student_management1.del_student()
    student_management1.save_student()
    student_management1.show_all_student()
    student_management1.update_student()
    student_management1.show_all_student()
    student_management1.save_student()