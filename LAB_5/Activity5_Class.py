class Student:
    def __init__(self):
        self.student_name = input("Enter student name: ")
        self.student_course = input("Enter student course: ")
        self.student_number = input("Enter student number: ")
        self.student_year = input("Enter student academic year: ")
        self.current_date = input("Enter current date: ")
        self.all_data = []
        self.total_units = 0

    def collect_subject_data(self):
        for i in range(5):
            student_subject = input("Enter student's subject: ")
            student_section = input(f"Enter student's section for {student_subject}: ")
            subject_units = int(input(f"Enter units for {student_subject}: "))
            student_data = [student_subject, student_section, subject_units]
            self.all_data.append(student_data)
            self.total_units += subject_units
        return self.all_data, self.total_units


class Assessment:
    def __init__(self):
        self.adu_chronicle = float(input("Enter Adu chronicle fee: "))
        self.athletic = float(input("Enter Athletic fee: "))
        self.audio_visual_lib = float(input("Enter audio-visual library fee: "))
        self.ausg = float(input("Enter AUSG fee: "))
        self.cultural_fee = float(input("Enter cultural fee: "))
        self.energy_cost = float(input("Enter energy cost fee: "))
        self.guidance = float(input("Enter guidance fee: "))
        self.insurance_fee = float(input("Enter insurance fee: "))
        self.learning_man_sys = float(input("Enter Learning management system fee: "))
        self.library_fee = float(input("Enter the library fee: "))
        self.medical_dental = float(input("Enter medical and dental fee: "))
        self.registration = float(input("Enter registration fee: "))
        self.rso = float(input("Enter RSO fee: "))
        self.students_activity = float(input("Enter student's activity fee: "))
        self.nurturance = float(input("Enter student nurturance fee: "))
        self.technology_fee = float(input("Enter technology fee: "))
        self.test_paper = float(input("Enter test paper fee: "))
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
        self.assessment_amount = (self.all_units_fee + self.adu_chronicle + self.athletic + self.audio_visual_lib +
                                  self.ausg + self.cultural_fee + self.energy_cost + self.guidance + self.insurance_fee +
                                  self.learning_man_sys + self.library_fee + self.medical_dental + self.registration +
                                  self.rso + self.students_activity + self.nurturance + self.technology_fee +
                                  self.test_paper)

    def total_due_payment(self):
        self.total_due = self.assessment_amount + self.down_payment
        self.prelim_payment = self.total_due / 3
        self.midterm_payment = self.total_due / 3
        self.final_payment = self.total_due / 3



