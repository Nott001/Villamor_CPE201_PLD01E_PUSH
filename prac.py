class Student:

    # Initialization
    def __init__(self):

        # Getting the Values of Student Information
        self.student_name = input("Enter Student Name: ")
        self.student_course = input("Enter Student Course: ")
        self.student_number = input("Enter Student Number: ")
        self.academic_year = input("Enter Academic Year: ")
        self.date_printed = input("Enter Date of Printed: ")
        self.subject_info = []

    # Getting Student Subjects and Units
    def student_subjects(self):
        for i in range(5):
            print(f"Subject {i + 1}")
            section = input("Enter Section: ")
            subject = input("Enter Subject: ")
            unit = int(input("Enter Unit: "))
            self.subject_info.append((section, subject, unit))

    def sum_units(self):
        return sum(unit for _, _, unit in self.subject_info)


class AssessmentFee:
    def __init__(self, student):
        self.student = student
        self.total_units = 0
        self.tuition = 0

    def tuition_fee(self):
        self.total_units = self.student.sum_units()
        self.tuition = self.total_units * 1500.00
        return self.tuition

    def display(self):
        print(self.tuition_fee())


students = Student()
students.student_subjects()
students.sum_units()

assessment = AssessmentFee(students)
assessment.tuition_fee()
assessment.display()