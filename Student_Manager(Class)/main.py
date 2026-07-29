from student_management import Student_Management

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
    continue_flag = input("Do you want to manage students(yes/no):")
    if continue_flag == "yes":
        file_name = input("Input the class file name(class0.txt):")
        student_management = Student_Management(file_name)
        student_management.load_students()
        while True:
            menu()
            key = int(input("What do you want to do:"))
            if key == 1:
                student_management.add_student()
            elif key == 2:
                student_management.del_student()
            elif key == 3:
                student_management.show_student()
            elif key == 4:
                student_management.show_all_student()
            elif key == 5:
                student_management.update_student()
            elif key == 6:
                student_management.save_student()
                break
    elif continue_flag == "no":
        break
    else:
        print("Valid input!")