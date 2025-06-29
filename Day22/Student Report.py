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

    def calculate_average(self):
        total_marks = 0
        for marks in self.__marks.values():
            total_marks += marks
        average = total_marks / len(self.__marks)
        print(f"Average marks for {self.name} (Roll No: {self.roll_no}) : {average}")
        return average

    def is_passed(self):
        has_failed = any(marks<35 for marks in self.__marks.values())
        if has_failed:
            print(f"{self.name} (Roll No: {self.roll_no}) has failed.")
        else:
            print(f"{self.name} (Roll No: {self.roll_no}) has passed.")

    def calculate_grade(self):
        print("Grade : ", end="")
        average = self.calculate_average()
        if  average >= 90:
            print("Grade: A")
        elif average >= 70:
            print("Grade: B")
        elif average >= 50:
            print("Grade: C")
        elif average >= 35:
            print("Grade: D")
        else:
            print("Grade: F")

class StudentReport:
    @staticmethod
    def generate(student: Student):
        student_marks = student.get_marks()
        print(f"Name : {student.name} \t Roll No : {student.roll_no}")

        print("-----Marks-----")
        for subject, marks in student_marks.items():
            print(f"{subject} : {marks}")
            
        print("----------------")

        student.is_passed()
        student.calculate_grade()

a =  Student(1, "Arjun")
a.add_marks("Math", 97)
a.add_marks("Science", 96)
a.add_marks("English", 34) 

StudentReport.generate(a)
