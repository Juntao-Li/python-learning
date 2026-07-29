from student_operator import *

students = load_students()

def menu():
    print("========Student Management System========")
    print("1. Add student")
    print("2. Delete student")
    print("3. Show student")
    print("4. Show all students")
    print("5. Update student")
    print("6. Exit")
    print("=========================================")

while True:
    menu()
    num = int(input("Input number you want to do:"))
    if num == 1:
        add_student(students)
    elif num == 2:
        del_student(students)
    elif num == 3:
        show_student(students)
    elif num == 4:
        show_all_student(students)
    elif num == 5:
        update_student(students)
    elif num == 6:
        save_students(students)
        break
    else:
        print("Error, please input the right number!")



