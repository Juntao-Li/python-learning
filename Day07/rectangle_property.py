class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        if self.width > 0 and self.height > 0:
            return self.width * self.height
        else:
            return "Width or Height Invalid!"

if __name__ == "__main__":

    rectangle1 = Rectangle(4, 5)

    print(rectangle1.area)

    rectangle2 = Rectangle(0, 5)

    print(rectangle2.area)

    rectangle3 = Rectangle(3, -2)

    print(rectangle3.area)

    rect = Rectangle(5, 10)

    print(rect.area)