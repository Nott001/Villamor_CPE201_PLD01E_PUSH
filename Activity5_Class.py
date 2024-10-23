class Student:
    def __init__(self):
        # class student
        self.student_name = input("Enter student name: ")
        self.student_course = input("Enter student course: ")
        self.student_number = input("Enter student number: ")
        self.student_acad_year = input("Enter student academic year: ")
        self.current_date = input("Enter current date: ")
        self.all_data = []
        self.total_units = 0


    def collect_student_data(self):
        for _ in range(5):
            student_subject = input("Enter student's subject: ")
            student_section = input(f"Enter section for {student_subject} subject: ")
            units = int(input(f"Enter units for that {student_subject}: "))
            input_data = [student_subject, student_section, units]
            self.all_data.append(input_data)
            self.total_units += units
        return self.total_units, self.all_data

    def display_student_information(self):
        print("Student Information:")
        print(f"Name: {self.student_name}")
        print(f"Course: {self.student_course}")
        print(f"Number: {self.student_number}")
        print(f"Academic Year: {self.student_acad_year}")
        print(f"Date Printed: {self.current_date}")
        print(f"Total Units: {self.total_units}")
        print("Subjects:")
        for data in self.all_data:
            print(f"  Subject: {data[0]}, Section: {data[1]}, Units: {data[2]}")

class Assessment:
    def __init__(self):
        self.adu_chronicle = float(input("Enter Adu chronicle fee: "))
        self.athletic = float(input("Enter ATHLETIC fee: "))
        self.audio_visual_lib = float(input("Enter audio visual library fee: "))
        self.ausg = float(input("Enter AUSG fee: "))
        self.cultural_fee = float(input("Enter cultural fee: "))
        self.energy_cost = float(input("Enter energy cost fee: "))
        self.guidance = float(input("Enter guidance fee: "))
        self.insurance_fee = float(input("Enter insurance fee: "))
        self.learning_man_sys = float(input("Enter Learning management system fee: "))
        self.library_fee = float(input("Enter the library fee: "))
        self.medical_dental = float(input("Enter medical and dental fee: "))
        self.registration = float(input("Enter registration fee: "))
        self.rso = float(input("Enter rso fee: "))
        self.students_activity = float(input("Enter student's activity fee: "))
        self.nurturance = float(input("Enter student nurturance fee: "))
        self.technology_fee = float(input("Enter technology fee: "))
        self.test_papers = float(input("Enter test papers fee: "))
        self.down_payment = float(input("Enter down payment: "))
        self.all_units_fee = 0
        self.assessment_amount = 0
        self.total_due = 0
        self.prelim_payment = 0
        self.midterm_payment = 0
        self.final_payment = 0

    def tuition_fee_lecture(self, total_units):
        self.all_units_fee = total_units * 1551.00

    def computed_value_assessment(self):
        self.assessment_amount = (
            self.all_units_fee +
            self.adu_chronicle + self.athletic + self.audio_visual_lib + self.ausg +
            self.cultural_fee + self.energy_cost + self.guidance + self.insurance_fee +
            self.learning_man_sys + self.library_fee + self.medical_dental + self.registration +
            self.rso + self.students_activity + self.nurturance + self.technology_fee +
            self.test_papers
        )

    def total_due_payment(self):
        self.total_due = self.assessment_amount
        self.prelim_payment = self.total_due / 3
        self.midterm_payment = self.total_due / 3
        self.final_payment = self.total_due / 3

    def display_assessment_details(self):
        print("\nAssessment Details:")
        print(f"Tuition Fee Lecture: {self.all_units_fee}")
        print(f"Total Assessment Amount: {self.assessment_amount}")
        print(f"Down Payment: {self.down_payment}")
        print(f"Total Due: {self.total_due}")
        print(f"Prelim Payment: {self.prelim_payment}")
        print(f"Midterm Payment: {self.midterm_payment}")
        print(f"Final Payment: {self.final_payment}")

student = Student()
student.collect_student_data()
student.display_student_information()

assessment = Assessment()
assessment.tuition_fee_lecture(student.total_units)
assessment.computed_value_assessment()
assessment.total_due_payment()
assessment.display_assessment_details()








