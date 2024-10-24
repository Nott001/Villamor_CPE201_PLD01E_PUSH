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

    def get_student_info(self):
        info = []
        info.append("\t\t\tCERTIFICATE OF ENROLLMENT\t\t\t")
        info.append("\t\t\t2nd Semester, 2022-2023\t\t\t")
        info.append(f"NAME\t: {self.student_name:<25} COURSE\t: {self.student_course}")
        info.append(f"STUDENT NO.\t: {self.student_number:<20} ACAD. YEAR\t: {self.student_year}")
        info.append("-------------------------------------------------------------------")
        info.append("SECTION\t\t\t\tSUBJECT                                 UNITS")
        info.append("-------------------------------------------------------------------")
        for data in self.all_data:
            info.append(f"{data[1]:<15} {data[0]:<45} {data[2]}")
        info.append(f"                                       Total Units: {self.total_units}")
        info.append(f"            Date Printed:{self.current_date}")
        return info

    def display_student_data(self):
        for line in self.get_student_info():
            print(line)

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

    def get_assessment_details(self):
        details = []
        details.append("\n")
        details.append("\n")
        details.append("\n")
        details.append("\n")
        details.append("------------------------------------------------")
        details.append("        ASSESSMENT OF FEES               ")
        details.append("|------------------------------------------------|")
        details.append(f"| TUITION FEE LECTURE           {self.all_units_fee:<5} |")
        details.append(f"| AdU CHRONICLE                   {self.adu_chronicle:<5} |")
        details.append(f"| ATHLETIC                        {self.athletic:<5} |")
        details.append(f"| AUDIO-VISUAL LIBRARY            {self.audio_visual_lib:<5} |")
        details.append(f"| AUSG                            {self.ausg:<5} |")
        details.append(f"| CULTURAL FEE                    {self.cultural_fee:<5} |")
        details.append(f"| ENERGY COST, AIRCON CLASSROOM   {self.energy_cost:<5} |")
        details.append(f"| GUIDANCE                        {self.guidance:<5} |")
        details.append(f"| INSURANCE FEE                   {self.insurance_fee:<5} |")
        details.append(f"| LEARNING MANAGEMENT SYSTEM      {self.learning_man_sys:<5} |")
        details.append(f"| LIBRARY FEE                     {self.library_fee:<5} |")
        details.append(f"| MEDICAL AND DENTAL              {self.medical_dental:<5} |")
        details.append(f"| REGISTRATION                    {self.registration:<5} |")
        details.append(f"| RSO                             {self.rso:<5} |")
        details.append(f"| STUDENT ACTIVITIES FEE          {self.students_activity:<5} |")
        details.append(f"| STUDENT NURTURANCE FEE          {self.nurturance:<5} |")
        details.append(f"| TECHNOLOGY FEE                  {self.technology_fee:<5} |")
        details.append(f"| TEST PAPERS                     {self.test_paper:<5} |")
        details.append("|------------------------------------------------|")
        details.append(f"| Assessment Amt.:                {self.assessment_amount:<5} |")
        details.append(f"| Downpayment:                    {self.down_payment:<5} |")
        details.append("|------------------------------------------------|")
        details.append(f"| Total Due:                      {self.total_due:<5} |")
        details.append("|")
        details.append("|")
        details.append("|")
        details.append("|")
        details.append("|------------------------------------------------|")
        details.append("|   Schedule of Payment                 |")
        details.append("|   of outstanding balance              |")
        details.append("|   after downpayment prior to          |")
        details.append("|------------------------------------------------|")
        details.append(f"| PRELIMS                    {self.prelim_payment:<5} |")
        details.append(f"| MIDTERMS                   {self.midterm_payment:<5} |")
        details.append(f"| FINALS                     {self.final_payment:<5} |")
        details.append("|------------------------------------------------|")
        details.append("       THIS IS A TEMPORARY ASSESSMENT")
        return details

    def display_assessment_details(self):
        for line in self.get_assessment_details():
            print(line)

# Instantiate and collect data
student = Student()
student.collect_student_data()
assessment = Assessment()
assessment.tuition_fee_lecture(student.total_units)
assessment.computed_value_assessment()
assessment.total_due_payment()

# Prepare lines for display
student_info = student.get_student_info()
assessment_info = assessment.get_assessment_details()

# Adjust lengths to ensure alignment
max_length = max(len(student_info), len(assessment_info))
student_info += [""] * (max_length - len(student_info))
assessment_info += [""] * (max_length - len(assessment_info))

# Display side by side
for s_line, a_line in zip(student_info, assessment_info):
    print(f"{s_line:<75} {a_line}")










