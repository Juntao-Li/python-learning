from library import Library

def menu():
    print("========Library Management System========")
    print("1. Add book")
    print("2. Delete book")
    print("3. Show book")
    print("4. Show all books")
    print("5. Update book")
    print("6. Exit")
    print("=========================================")

library = Library()
library.load_books()

while True:
    menu()
    try:
        key = int(input("What do you want to do:"))
        if key == 1:
            library.add_book()
        elif key == 2:
            library.del_book()
        elif key == 3:
            library.show_book()
        elif key == 4:
            library.show_all_books()
        elif key == 5:
            library.update_book()
        elif key == 6:
            library.save_books()
            break
        else:
            print("Please input number from 1 to 6!")
    except ValueError:
        print("Please input integer!")
