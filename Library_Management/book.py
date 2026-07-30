class Book:
    def __init__(self, title, author, isbn, is_borrowed):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"Title:{self.title}\nAuthor:{self.author}\nIsbn:{self.isbn}\nIs_borrowed:{self.is_borrowed}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn

    def borrow_book(self):
        if self.is_borrowed:
            print("The book has been borrowed!")
        else:
            self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            print("The book dosen't need to be returned!")
        else:
            self.is_borrowed = False

if __name__ == "__main__":
    book1 = Book("Python", "Guido", 1001, True)
    book2 = Book("Python", "Guido", 1002, False)

    print(book1)
    print("")
    book1.return_book()
    print(book1)
    print("")

    print(book2)
    print("")
    book2.borrow_book()
    print(book2)
    print("")
    
    print(book1 == book2)

    print(type(book1.is_borrowed))
