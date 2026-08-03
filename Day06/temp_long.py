class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Printer:
    def print_book(self, book):
        print(f"title:{book.title}")
        print(f"author:{book.author}")

class BookReader:
    def __init__(self, book):
        self.book = book

    def read(self):
        print(f"title:{self.book.title}")
        print(f"author:{self.book.author}")

book = Book("Python", "Guido")

Printer().print_book(book)

BookReader(book).read()