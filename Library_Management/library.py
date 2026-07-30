from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):

        title = input("Input the title:")
        author = input("Input the author:")
        isbn = input("Input the isbn:")
        is_borrowed = False

        book = Book(title, author, isbn, is_borrowed)

        self.books.append(book)

    def del_book(self):
        isbn = input("Input the isbn:")
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("Delete succussfully!")
                break
        else:
            print("Book not found!")

    def update_book(self):
        isbn = input("Input the isbn:")
        for book in self.books:
            if book.isbn == isbn:
                while True:
                    print("1.Title")
                    print("2.Author")
                    print("3.Is_borrowed")
                    print("4.Exit")
                    try:
                        key = int(input("What do you want to change:"))
                        if key == 1:
                            book.title = input("Input the title:")
                        elif key == 2:
                            book.author = input("Input the author:")
                        elif key == 3:
                            if not book.is_borrowed:
                                book.borrow_book()
                                print("Borrowed succussfully!")
                            elif book.is_borrowed:
                                book.return_book()
                                print("Returned succussfully!")
                        elif key == 4:
                            break
                        else:
                            print("Please input the number from 1 to 4!")
                    except ValueError:
                        print("Please input the integer from 1 to 4!")

    def save_books(self):
        try:
            with open ("library.txt", "w") as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.isbn},{book.is_borrowed}\n")
        except FileNotFoundError:
            print("File not found!")

    def load_books(self):
        try:
            with open ("library.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    is_borrowed = data[3] == "True"
                    book = Book(data[0], data[1], data[2], is_borrowed)
                    self.books.append(book)
        except FileNotFoundError:
            print("File not found!")

    def show_book(self):
        isbn = input("Input the isbn:")
        for book in self.books:
            if book.isbn == isbn:
                print("-"*42)
                print(book)
                print("-"*42)
                break
        else:
            print("Book not found!")

    def show_all_books(self):
        print("-"*42)
        for book in self.books:
            print(book)
            print("-"*42)
