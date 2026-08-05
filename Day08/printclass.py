class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} | {self.author} | ${self.price}"

    def __repr__(self):
        return self.__str__()

book = Book("Python", "Tom", 59.9)

print(book)

books = [
    Book("Python", "Tom", 59.9),
    Book("Java", "Jack", 69.9)
]

print(books)