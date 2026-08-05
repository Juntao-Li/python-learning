class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def show_name(self):
        return self.__name

if __name__ == "__main__":
    
    person1 = Person("Jack")

    print(person1.show_name)