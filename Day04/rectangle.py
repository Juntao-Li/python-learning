class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * ( self.width + self.height )

if __name__ == "__main__":
    rectangle1 = Rectangle(10, 25)
    print(f"area:{rectangle1.area()}")
    print(f"perimeter:{rectangle1.perimeter()}")