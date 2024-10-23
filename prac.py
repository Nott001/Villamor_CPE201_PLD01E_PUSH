class Student:
    def __init__(self):
        self.student_name = input("Enter student name: ")
        self.student_course = input("Enter student course: ")
        self.student_number = input("Enter student number: ")
        self.student_year = input("Enter student academic year: ")
        self.current_date = input("Enter current date: ")
        self.all_data = []
        self.total_units = 0

    def collect_student_data(self):
        for i in range(5):
            student_subject = input("Enter student's subject: ")
            student_section = input(f"Enter student's section for {student_subject}: ")
            subject_units = int(input(f"Enter units for {student_subject}: "))
            student_data = [student_subject, student_section, subject_units]
            self.all_data.append(student_data)
            self.total_units += subject_units
        return self.all_data, self.total_units

    def display_student_data(self):
        print("\t\t\tCERTIFICATE OF ENROLLMENT\t\t\t")
        print("\t\t\t2nd Semester, 2022-2023\t\t\t")
        print(f"NAME\t: {self.student_name}", end="")
        print(f"\t\tCOURSE\t: {self.student_course}")
        print(f"STUDENT NO.\t: {self.student_number}", end="")
        print(f"\t\tACAD. YEAR\t: {self.student_year}")
        print("-----------------------------------------------------------------")
        print("SECTION\t\t\t\t\t\tSUBJECT\t\t\t\t\t\tUNITS")
        print("-----------------------------------------------------------------")
        for data in self.all_data:
            print(f"{data[0]}\t\t\t\t{data[1]}\t\t\t\t{data[2]}")

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
            self.rso + self.students_activity + self. nurturance + self.technology_fee +
            self.test_paper)

    def total_due_payment(self):
        self.total_due = self.assessment_amount + self.down_payment
        self.prelim_payment = self.total_due / 3
        self.midterm_payment = self.total_due / 3
        self.final_payment = self.total_due / 3

    def display_assessment_details(self):
        print("-----------------------------------------")
        print("|\t\tASSESSMENT OF FEES\t\t")
        print("|-----------------------------------------")
        print(f"|TUITION FEE LECTURE\t\t{self.all_units_fee}")
        print(f"|AdU CHRONICLE\t\t{self.adu_chronicle}")
        print(f"|ATHLETIC\t\t{self.athletic}")
        print(f"|AUDIO-VISUAL LIBRARY\t\t{self.audio_visual_lib}")
        print(f"|AUSG\t\t{self.ausg}")
        print(f"|CULTURAL FEE\t\t{self.cultural_fee}")
        print(f"|ENERGY COST,AIRCON CLASSROOM\t\t{self.energy_cost}")
        print(f"|GUIDANCE\t\t{self.guidance}")
        print(f"|INSURANCE FEE\t\t{self.insurance_fee}")
        print(f"|LEARNING MANAGEMENT SYSTEM\t\t{self.learning_man_sys}")
        print(f"|LIBRARY FEE\t\t{self.library_fee}")
        print(f"|MEDICAL AND DENTAL\t\t{self.medical_dental}")
        print(f"|REGISTRATION\t\t{self.registration}")
        print(f"|RSO\t\t{self.rso}")
        print(f"|STUDENT ACTIVITIES FEE\t\t{self.students_activity}")
        print(f"|STUDENT NURTURANCE FEE\t\t{self.nurturance}")
        print(f"|TECHNOLOGY FEE\t\t{self.technology_fee}")
        print(f"|TEST PAPERS\t\t{self.test_paper}")
        print("|------------------------------------")
        print(f"|Assessment Amt.:\t\t{self.assessment_amount}")
        print(f"|Downpayment:\t\t{self.down_payment}")
        print("|------------------------------------")
        print("|\t\tSchedule of Payment\t\t\t \n\t\tof outstanding balance\t\t \n\t\tafter downpayment"
              "prior to\t\t:")
        print(f"|PRELIMS\t\t{self.prelim_payment}")
        print(f"|MIDTERMS\t\t{self.midterm_payment}")
        print(f"|FINALS\t\t{self.final_payment}")
        print("|------------------------------------")
        print("\t\tTHIS IS A TEMPORARY ASSESSMENT\t\t")

student = Student()
student.collect_student_data()
student.display_student_data()

assessment = Assessment()
assessment.tuition_fee_lecture(student.total_units)
assessment.computed_value_assessment()
assessment.total_due_payment()
assessment.display_assessment_details()

