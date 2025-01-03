import gui_project
import tkinter as tk

window = tk.Tk()
window.title("Payroll page")
window.geometry('1920x1080')

gui_design = gui_project.GUIdesign(window)

#Addition of white colored frame
gui_design.frames(550, 0, 853, 1080, 'white')
gui_design.frames( 582, 157, 210, 190, 'grey')

#textbox
employee_number_box = gui_design.textbox_design(767, 361, 23, 1, 'black', 'white', ('Calibri', 10))
department_box = gui_design.textbox_design(767, 423, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

rate_hour_basic_box = gui_design.textbox_design(767, 490, 23, 1, 'black', 'white', ('Calibri', 10))
no_hrs_cutoff_basic_box = gui_design.textbox_design(767, 519, 23, 1, 'black', 'white', ('Calibri', 10))
income_cutoff_basic_box = gui_design.textbox_design(767, 549, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

rate_hour_honor_box = gui_design.textbox_design(767, 627, 23, 1, 'black', 'white', ('Calibri', 10))
no_hrs_cutoff_honor_box = gui_design.textbox_design(767, 656, 23, 1, 'black', 'white', ('Calibri', 10))
income_cutoff_honor_box = gui_design.textbox_design(767, 685, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

rate_hour_other_box = gui_design.textbox_design(767, 765, 23, 1, 'black', 'white', ('Calibri', 10))
no_hrs_cutoff_other_box = gui_design.textbox_design(767, 794, 23, 1, 'black', 'white', ('Calibri', 10))
income_cutoff_other_box = gui_design.textbox_design(767, 823, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

gross_income_box = gui_design.textbox_design(767, 901, 23, 1, 'black', 'white', ('Calibri', 10))
net_income_box = gui_design.textbox_design(767,930, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

first_name_box = gui_design.textbox_design(1172,151, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
middle_name_box = gui_design.textbox_design(1172,184, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
surname_box = gui_design.textbox_design(1172,217, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
civil_stats_box = gui_design.textbox_design(1172,250, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
qualified_dependents_box = gui_design.textbox_design(1172,283, 23, 1, 'black', 'white', ('Calibri', 10))
paydate_box = gui_design.textbox_design(1172,325, 23, 1, 'black', 'white', ('Calibri', 10))
employee_status_box = gui_design.textbox_design(1172,358, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
designation_box = gui_design.textbox_design(1172,391, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

sss_cont_box = gui_design.textbox_design(1172,490, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
philhealth_cont_box = gui_design.textbox_design(1172,519, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
pagibig_cont_box = gui_design.textbox_design(1172,549, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))
income_tax_cont_box = gui_design.textbox_design(1172,578, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

sss_loan_box = gui_design.textbox_design(1172,658, 23, 1, 'black', 'white', ('Calibri', 10))
pagibig_loan_box = gui_design.textbox_design(1172,691, 23, 1, 'black', 'white', ('Calibri', 10))
faculty_savings_dep_box = gui_design.textbox_design(1172,724, 23, 1, 'black', 'white', ('Calibri', 10))
faculty_savings_loan_box = gui_design.textbox_design(1172,757, 23, 1, 'black', 'white', ('Calibri', 10))
salary_loan_box = gui_design.textbox_design(1172,790, 23, 1, 'black', 'white', ('Calibri', 10))
other_loans_box= gui_design.textbox_design(1172,823, 23, 1, 'black', 'white', ('Calibri', 10))

total_deductions = gui_design.textbox_design(1172,901, 23, 1, 'black', '#D4D4D4', ('Calibri', 10))

#small label designs
emp_num_text = gui_design.label_design(602, 360, 'Employee Number:','white', ('Calibri', 10))
search_emp_text = gui_design.label_design(602, 393, 'Search Employee:', 'white', ('Calibri', 10))
department_text = gui_design.label_design(602, 424, 'Department:', 'white', ('Calibri', 10))
rate_hour_basic_text = gui_design.label_design(602, 489, 'Rate / Hour:', 'white', ('Calibri', 10))
num_hrs_cutoff_basic_text = gui_design.label_design(602, 518, 'No. of Hours / Cut Off:', 'white', ('Calibri', 10))
income_cutoff_basic_text = gui_design.label_design(602, 547, 'Income / Cut Off:', 'white', ('Calibri', 10))
rate_hour_hon_text = gui_design.label_design(602, 626, 'Rate / Hour:', 'white', ('Calibri', 10))
num_hrs_cutoff_hon_text = gui_design.label_design(602, 655, 'No. of Hours / Cut Off:', 'white', ('Calibri', 10))
income_cutoff_hon_text = gui_design.label_design(602, 684, 'Income / Cut Off:', 'white', ('Calibri', 10))
rate_hour_other_text = gui_design.label_design(602, 764, 'Rate / Hour:', 'white', ('Calibri', 10))
num_hrs_cutoff_other_text = gui_design.label_design(602, 793, 'No. of Hours / Cut Off:', 'white', ('Calibri', 10))
income_cutoff_other_text = gui_design.label_design(602, 822, 'Income / Cut Off:', 'white', ('Calibri', 10))
gross_income_text = gui_design.label_design(602, 900, 'GROSS INCOME:', 'white', ('Calibri', 10))
net_income_text = gui_design.label_design(602, 929, 'NET INCOME:', 'white', ('Calibri', 10))
fristname_text = gui_design.label_design(1015, 150, 'Firstname:', 'white', ('Calibri', 10))
mid_name_text = gui_design.label_design(1015, 183, 'Middle Name:', 'white', ('Calibri', 10))
surname_text = gui_design.label_design(1015, 216, 'Surname:', 'white', ('Calibri', 10))
civilstat_text = gui_design.label_design(1015, 249, 'Civil Status:', 'white', ('Calibri', 10))
qualified_dep_text = gui_design.label_design(1015, 282, 'Qualified Dependents:', 'white', ('Calibri', 10))
emp_status_text = gui_design.label_design(1015, 300, 'Status:', 'white', ('Calibri', 10))
paydate_text = gui_design.label_design(1015, 324, 'Paydate:', 'white', ('Calibri', 10))
employee_stat_text = gui_design.label_design(1015, 357, 'Employee Status:', 'white', ('Calibri', 10))
designation_text = gui_design.label_design(1015, 390, 'Designation:', 'white', ('Calibri', 10))
sss_cont_text = gui_design.label_design(1015, 489, 'SSS Contribution:', 'white', ('Calibri', 10))
Phil_cont_text = gui_design.label_design(1015, 518, 'PhilHealth Contribution:', 'white', ('Calibri', 10))
pagibig_cont_text = gui_design.label_design(1015, 547, 'Pagibig Contribution:', 'white', ('Calibri', 10))
income_tax_cont_text = gui_design.label_design(1015, 576, 'Income Tax Contribution', 'white', ('Calibri', 10))
sss_loan_text = gui_design.label_design(1015, 657, 'SSS Loan:', 'white', ('Calibri', 10))
pagibig_loan_text = gui_design.label_design(1015, 690, 'Pagibig Loan:', 'white', ('Calibri', 10))
fac_savings_dep_text = gui_design.label_design(1015, 723, 'Faculty Savings Deposit:', 'white', ('Calibri', 10))
Fac_savings_loan_text = gui_design.label_design(1015, 756, 'Faculty Savings Loan:', 'white', ('Calibri', 10))
salary_loan_text = gui_design.label_design(1015, 789, 'Salary Loan:', 'white', ('Calibri', 10))
other_loans_text = gui_design.label_design(1015, 822, 'Other Loans:', 'white', ('Calibri', 10))
total_deduc_text = gui_design.label_design(1015, 900, 'Total Deductions:', 'white', ('Calibri', 10))

#medium big labels
emp_basic_info_text = gui_design.label_design(584, 125, 'EMPLOYEE BASIC INFO:', 'white', ('Calibri', 13, 'bold'))
emp_basic_income_text = gui_design.label_design(584, 455, 'BASIC INCOME:', 'white', ('Calibri', 13, 'bold'))
emp_hon_income_text = gui_design.label_design(584, 586, 'HONORARIUM INCOME:', 'white', ('Calibri', 13, 'bold'))
emp_other_income_text = gui_design.label_design(584, 723, 'OTHER INCOME:', 'white', ('Calibri', 13, 'bold'))
emp_summary_income_text = gui_design.label_design(584, 861, 'SUMMARY INCOME:', 'white', ('Calibri', 13, 'bold'))
emp_reg_deductions_text = gui_design.label_design(996, 455, 'REGULAR DEDUCTIONS:', 'white', ('Calibri', 13, 'bold'))
emp_other_deduc_text = gui_design.label_design(996, 618, 'OTHER DEDUCTIONS:', 'white', ('Calibri', 13, 'bold'))
emp_deductions_summary_text = gui_design.label_design(996, 861, 'DEDUCTION SUMMARY:', 'white', ('Calibri', 13, 'bold'))

#large labels
emp_title_text = gui_design.label_design(775, 57, "LPU'S CHOICE PAYROLL", 'white', ('OldEnglish.ttf', 25, 'bold'))

#different buttons
search_button = gui_design.button_design(767, 393, 10, 1, '#EE1E1E','white', 'SEARCH', 1, ('Calibri', 10))
gross_income_button = gui_design.button_design(992, 930, 13, 1, '#0085F1', 'white', 'GROSS INCOME', 1, ('Calibri', 10))
net_income_button = gui_design.button_design(1093, 930, 13, 1, '#0085F1', 'white', 'NET INCOME', 1, ('Calibri', 10))
save_button = gui_design.button_design(1194, 930, 7, 1, '#1C8E81', 'white', 'SAVE', 1, ('Calibri', 10))
update_button = gui_design.button_design(1253, 930, 7, 1, '#1C8E81', 'white', 'UPDATE', 1, ('Calibri', 10))
next_button = gui_design.button_design(1311, 930, 7, 1, '#D7B600', 'black', 'NEW', 1, ('Calibri', 10))

#insert of image
employee_image = gui_design.image_design(r'C:\Users\karlr\OneDrive\Documents\GitHub\Villamor_CPE201_PLD01E_PUSH\GUI_project\project_pics\profile.png', 585, 160, 200, 180)

window.mainloop()