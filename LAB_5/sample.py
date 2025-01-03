import Activity5_Class

student_information = Activity5_Class.Student()
student_information.collect_subject_data()
student_assesment = Activity5_Class.Assessment()


def display_data():
    print(f"student name: {student_information.student_name}")
    print(f"total units: {student_information.total_units}")
    print(f"total due: {student_assesment.total_due}")



display_data()


