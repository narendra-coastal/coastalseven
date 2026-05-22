class Student:

    def __init__(self):
        self.__marks = 0   # private variable

    # setter method
    def set_marks(self, marks):
        self.__marks = marks

    # getter method
    def get_marks(self):
        return self.__marks


# object creation
s = Student()

# setting value
s.set_marks(95)

# getting value
print("Marks:", s.get_marks())

# simple example
class Mobile:

    def __init__(self):
        self.__password = "1234"

    def show_password(self):
        print(self.__password)

m = Mobile()
m.show_password()