# Part 4 — OOP and single inheritance
# Focus on writing classes and creating objects independently.
# Question 13: Student class
# Create a class Student with:
# ●	A constructor that accepts name, roll number, and marks.
# ●	A method display_details() that prints all details.
# ●	A method check_result() that returns "Pass" if marks are at least 40, otherwise "Fail".
# Create three objects and display their results.


class Person:
    def __init__(self, name, rollNum):
        self.name = name
        self.rollNum = rollNum

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.rollNum}")


class Student(Person):
    def __init__(self, name, rollNum, marks):
        super().__init__(name, rollNum)
        self.marks = marks

    def display_details(self):
        super().display_details()
        print(f"Marks: {self.marks}")

    def check_result(self):
        return "Pass" if self.marks >= 40 else "Fail"

student1 = Student("Ed", "Std001", 65)
student2 = Student("Edd", "Std002", 30)
student3 = Student("Eddy", "Std003", 75)

print("Student Details and Results")
for student in (student1, student2, student3):
    print()
    student.display_details()
    print(f"Result: {student.check_result()}")
