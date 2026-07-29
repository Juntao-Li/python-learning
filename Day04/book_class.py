class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_info(self):
        print(f"title:{self.title}")
        print(f"author:{self.author}")
        print(f"price:{self.price}")

if __name__ == "__main__":
    book1 = Book("Python", "Guido", 99)
    book1.show_info()