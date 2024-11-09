import Activity5_Class
student = Activity5_Class.Student()
student.collect_subject_data()

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

Activity5_Class.Student.get_student_info = get_student_info
Activity5_Class.Student.display_student_data = display_student_data

student.display_student_data()