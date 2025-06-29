# Student Report Generation

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    