# Initialization of values
final_grade = 0

# Input of variables
student_name = input("Enter student name:")
final_quizzes = float(input("Enter student's final quizzes:"))
final_assignments_research = float(input("Enter student's final assignments/research:"))
final_project = float(input("Enter student's final project:"))
final_exam = float(input("Enter student's final exam:"))

# Calculating the final grade with the formula:
final_grade = (0.30*final_quizzes) + (0.10*final_assignments_research) + (0.40*final_exam) + (0.20*final_project)

# Deciding the equivalent grade remark of a student's final grade (No grade should exceed 100%)
if final_grade > 100:
    remark = str("THE FINAL GRADE EXCEEDS 100")
elif 98 <= final_grade <= 100:
    remark = 4.00
elif final_grade >= 95:
    remark = 3.75
elif final_grade >= 92:
    remark = 3.50
elif final_grade >= 89:
    remark = 3.25
elif final_grade >= 86:
    remark = 3.00
elif final_grade >= 83:
    remark = 2.75
elif final_grade >= 80:
    remark = 2.50
elif final_grade >= 77:
    remark = 2.25
elif final_grade >= 74:
    remark = 2.00
elif final_grade >= 71:
    remark = 1.75
elif final_grade >= 68:
    remark = 1.50
elif final_grade >= 64:
    remark = 1.25
elif final_grade >= 63:
    remark = 1.00
else:
    remark = 0.00

# Displaying the values of the variables and the remark.
print(f"Student Name: {student_name}")
print(f"Final quizzes: {final_quizzes}")
print(f"Final research/assignments: {final_assignments_research}")
print(f"Final projects: {final_project}")
print(f"Final exams: {final_exam}")
print(f"Final grade: {final_grade}")
print(f"Grading remark: {remark}")
