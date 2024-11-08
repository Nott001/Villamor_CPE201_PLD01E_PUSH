import Activity5_Class

# Instantiate and collect data
student = Activity5_Class.Student()
student.collect_subject_data()
assessment = Activity5_Class.Assessment()

def get_student_info(self):
    info = []
    info.append("\t\t\t\t\t\t\t\t\t\t\tCERTIFICATE OF ENROLLMENT")
    info.append(f"NAME  : {self.student_name:<85} STUDENT NO.: {self.student_number}")
    info.append(f"COURSE: {self.student_course:<85} ACAD. YEAR : {self.student_year}")
    info.append("-------------------------------------------------------------------")
    info.append("SECTION\t\t\t\tSUBJECT                                 UNITS")
    info.append("-------------------------------------------------------------------")
    for data in self.all_data:
        info.append(f"{data[1]:<15} {data[0]:<45} {data[2]}")
    info.append(f"                                             Total Units: {self.total_units}")
    lines_needed = 43 - len(info)
    info.extend([""] * lines_needed)
    info.append("-----------------------------------------------------------------")
    info.append(f"                      Date Printed:{self.current_date}")
    info.append("-----------------------------------------------------------------")
    return info

def display_student_data(self):
    for line in self.get_student_info():
        print(line)

def get_assessment_details(self):
    details = []
    details.append("\n")
    details.append("\n")
    details.append("\n")
    details.append("------------------------------------------------")
    details.append("        ASSESSMENT OF FEES               ")
    details.append("------------------------------------------------")
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
    details.append("|--|---------------------------------|-----------|")
    details.append("|  |      Schedule of Payment        |")
    details.append("|  |    of outstanding balance       |")
    details.append("|  |  after downpayment prior to     |")
    details.append(f"|  |PRELIMS                    {self.prelim_payment:<5} |")
    details.append(f"|  |MIDTERMS                   {self.midterm_payment:<5} |")
    details.append(f"|  |FINALS                     {self.final_payment:<5} |")
    details.append("|--|---------------------------------|-----------|")
    details.append("|      *There will be a 6% supercharge p.a")
    details.append("|              for late payment")
    details.append("|------------------------------------------------|")
    details.append("|       THIS IS A TEMPORARY ASSESSMENT")
    details.append("|------------------------------------------------|")
    return details

def display_assessment_details(self):
    for line in self.get_assessment_details():
        print(line)

# Add these methods to the respective classes dynamically
Activity5_Class.Student.get_student_info = get_student_info
Activity5_Class.Student.display_student_data = display_student_data
Activity5_Class.Assessment.get_assessment_details = get_assessment_details
Activity5_Class.Assessment.display_assessment_details = display_assessment_details

# Display student and assessment information
student_info = student.get_student_info()
assessment_info = assessment.get_assessment_details()

# Adjust lengths to ensure alignment
max_length = max(len(student_info), len(assessment_info))
student_info.extend([""] * (max_length - len(student_info)))
assessment_info.extend([""] * (max_length - len(assessment_info)))

# Display side by side
for s_line, a_line in zip(student_info, assessment_info):
    print(f"{s_line:<65} {a_line}")










