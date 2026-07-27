def add_student(students):
    while True:
        sid = input("Input the sid of the student(000):")
        for student in students:
            if student["sid"] == sid:
                print("This id has already existed!")
                break
        else:
            break

    name = input("Input the name of student:")
    while True:
        try:
            math = int(input("Input the score of Math:"))
            english = int(input("Input the score of English:"))
            history = int(input("Input the score of History:"))
            break
        except ValueError:
            print("The score you input must be integer")

    student = {
        "sid" : sid,
        "name" : name,
        "Math" : math,
        "English" : english,
        "History" : history
    }
    students.append(student)
    return

def del_student(students):
    sid = input("Input the sid of the student you want to delete:")
    for student in students:
        if student["sid"] == sid:
            students.remove(student)
            print("Delete successfully!")
            break
    else:
        print("Student not found!")

def show_student(students):
    sid = input("Input the sid of student you want to see:")
    for student in students:
        if student["sid"] == sid:
            for key, value in student.items():
                print(f"{key} : {value}")
            return
    else:
        print("Student not found")

def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            line = f"{student['sid']},{student['name']},{student['Math']},{student['English']},{student['History']}\n"
            file.write(line)
        return

def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                student = {
                    "sid": data[0],
                    "name": data[1],
                    "Math": int(data[2]),
                    "English": int(data[3]),
                    "History": int(data[4])
                    }
                students.append(student)
    except FileNotFoundError:
        print("File not found! Starting with an empty list.")
    return students

def show_all_student(students):
    for student in students:
        print("-"*41)
        print(f"name:{student['name']}")
        print(f"sid:{student['sid']}")
        print(f"Math:{student['Math']}")
        print(f"English:{student['English']}")
        print(f"History:{student['History']}")
    print("-"*41)

def update_student(students):
    sid = input("Input the sid of the student you want to update:")
    for student in students:
        if student["sid"] == sid:
            while True:
                print("1.name")
                print("2.Math")
                print("3.English")
                print("4.History")
                print("5.Done")
                key = int(input("What do you want to change:"))
                if key == 1:
                    student["name"] = input("Input the student's name:")
                elif key == 2:
                    student["Math"] = int(input("Input the score of Math"))
                elif key == 3:
                    student["English"] = int(input("Input the score of English:"))
                elif key == 4:
                    student["History"] = int(input("Input the score of History:"))
                elif key == 5:
                    break