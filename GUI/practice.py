import gui
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk


window = tk.Tk()
window.title("Payroll page")
window.geometry('1920x1080')

# Load the image with Pillow
image = Image.open('C:\\Users\\karlr\\OneDrive\\Documents\\GitHub\\Villamor_CPE201_PLD01E_PUSH\\GUI\\pictures of microsoft\\wallpaper.jpg')
bck_pic = ImageTk.PhotoImage(image.resize((1920, 1080)))
lbl = tk.Label(window, image=bck_pic)
lbl.place(x=1, y=1)

gui_design = gui.design_gui_interface(window)

gui_design.frames(546, 98, 400, 277, '#c8d8e4')
#call for frame 2
gui_design.frames(546, 384, 400, 156, '#c8d8e4')
#call for frame 3
gui_design.frames(546, 549, 400, 156, '#c8d8e4')
#call for frame 4
gui_design.frames(546, 714, 400, 156, '#c8d8e4')
#call for frame 5
gui_design.frames(546, 879, 400, 121, '#c8d8e4')
#call for frame 6
gui_design.frames(1000, 98, 400, 277, '#c8d8e4')
#call for frame 7
gui_design.frames(1000, 384, 400, 189, '#c8d8e4')
#call for frame 8
gui_design.frames(1000, 582, 400, 248, '#c8d8e4')
#call for frame 9
gui_design.frames(1000, 839, 400, 90, '#c8d8e4')


employee_number_box = gui_design.textbox_design(440, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
department_box = gui_design.textbox_design(649, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


rate_hour_basic_box = gui_design.textbox_design(858, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
no_hrs_cutoff_basic_box = gui_design.textbox_design(1067, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
income_cutoff_basic_box = gui_design.textbox_design(440, 330, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


rate_hour_honor_box = gui_design.textbox_design(858, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
no_hrs_cutoff_honor_box = gui_design.textbox_design(1067, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
income_cutoff_honor_box = gui_design.textbox_design(440, 3301, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


rate_hour_other_box = gui_design.textbox_design(858, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
no_hrs_cutoff_other_box = gui_design.textbox_design(1067, 262, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
income_cutoff_other_box = gui_design.textbox_design(440, 330, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


gross_income_box = gui_design.textbox_design(1067, 330, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
net_income_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


first_name_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
middle_name_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
surname_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
qualified_dependents_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
paydate_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
employee_status_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
designation_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


sss_cont_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
philhealth_cont_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
pagibig_cont_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
income_tax_cont_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


sss_loan_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
pagibig_loan_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
faculty_savings_dep_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
faculty_savings_loan_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
salary_loan_box = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))
other_loans_box= gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))


total_deductions = gui_design.textbox_design(1,1, 1, 1, 'black', 'white', ('Arial', 11, 'bold'))

#small label designs
emp_num_text = gui_design.label_design(232, 410, 'Employee Number:','#c8d8e4', ('Arial', 11, 'bold'))
search_emp_text = gui_design.label_design(1, 1, 'Search Employee:', '#c8d8e4', ('Arial', 11, 'bold'))
department_text = gui_design.label_design(232, 410, 'Department:', '#c8d8e4', ('Arial', 11, 'bold'))
rate_hour_basic_text = gui_design.label_design(232, 410, 'Rate / Hour:', '#c8d8e4', ('Arial', 11, 'bold'))
num_hrs_cutoff_basic_text = gui_design.label_design(232, 410, 'No. of Hours / Cut Off:', '#c8d8e4', ('Arial', 11, 'bold'))
income_cutoff_basic_text = gui_design.label_design(232, 410, 'Income / Cut Off:', '#c8d8e4', ('Arial', 11, 'bold'))
rate_hour_hon_text = gui_design.label_design(232, 410, 'Rate / Hour:', '#c8d8e4', ('Arial', 11, 'bold'))
num_hrs_cutoff_hon_text = gui_design.label_design(232, 410, 'No. of Hours / Cut Off:', '#c8d8e4', ('Arial', 11, 'bold'))
income_cutoff_hon_text = gui_design.label_design(232, 410, 'Income / Cut Off:', '#c8d8e4', ('Arial', 11, 'bold'))
rate_hour_other_text = gui_design.label_design(232, 410, 'Rate / Hour:', '#c8d8e4', ('Arial', 11, 'bold'))
num_hrs_cutoff_other_text = gui_design.label_design(232, 410, 'No. of Hours / Cut Off:', '#c8d8e4', ('Arial', 11, 'bold'))
income_cutoff_other_text = gui_design.label_design(232, 410, 'Income / Cut Off:', '#c8d8e4', ('Arial', 11, 'bold'))
gross_income_text = gui_design.label_design(232, 410, 'GROSS INCOME:', '#c8d8e4', ('Arial', 11, 'bold'))
net_income_text = gui_design.label_design(232, 410, 'NET INCOME:', '#c8d8e4', ('Arial', 11, 'bold'))
fristname_text = gui_design.label_design(232, 410, 'Firstname:', '#c8d8e4', ('Arial', 11, 'bold'))
mid_name_text = gui_design.label_design(232, 410, 'Middle Name:', '#c8d8e4', ('Arial', 11, 'bold'))
surname_text = gui_design.label_design(232, 410, 'Surname:', '#c8d8e4', ('Arial', 11, 'bold'))
civilstat_text = gui_design.label_design(232, 410, 'Civil Status:', '#c8d8e4', ('Arial', 11, 'bold'))
qualified_dep_text = gui_design.label_design(232, 410, 'Qualified Dependents \n Status:', '#c8d8e4', ('Arial', 11, 'bold'))
paydate_text = gui_design.label_design(232, 410, 'Paydate:', '#c8d8e4', ('Arial', 11, 'bold'))
employee_stat_text = gui_design.label_design(232, 410, 'Employee Status:', '#c8d8e4', ('Arial', 11, 'bold'))
designation_text = gui_design.label_design(232, 410, 'Designation:', '#c8d8e4', ('Arial', 11, 'bold'))
sss_cont_text = gui_design.label_design(232, 410, 'SSS Contribution:', '#c8d8e4', ('Arial', 11, 'bold'))
Phil_cont_text = gui_design.label_design(232, 410, 'PhilHealth Contribution:', '#c8d8e4', ('Arial', 11, 'bold'))
pagibig_cont_text = gui_design.label_design(232, 410, 'Pagibig Contribution:', '#c8d8e4', ('Arial', 11, 'bold'))
income_tax_cont_text = gui_design.label_design(232, 410, 'Income Tax Contribution', '#c8d8e4', ('Arial', 11, 'bold'))
sss_loan_text = gui_design.label_design(232, 410, 'SSS Loan:', '#c8d8e4', ('Arial', 11, 'bold'))
pagibig_loan_text = gui_design.label_design(232, 410, 'Pagibig Loan:', '#c8d8e4', ('Arial', 11, 'bold'))
fac_savings_dep_text = gui_design.label_design(232, 410, 'Faculty Savings Deposit:', '#c8d8e4', ('Arial', 11, 'bold'))
Fac_savings_loan_text = gui_design.label_design(232, 410, 'Faculty Savings Loan:', '#c8d8e4', ('Arial', 11, 'bold'))
salary_loan_text = gui_design.label_design(232, 410, 'Salary Loan:', '#c8d8e4', ('Arial', 11, 'bold'))
other_loans_text = gui_design.label_design(232, 410, 'Other Loans:', '#c8d8e4', ('Arial', 11, 'bold'))
total_deduc_text = gui_design.label_design(232, 410, 'Total Deductions:', '#c8d8e4', ('Arial', 11, 'bold'))

#medium big labels
emp_basic_info_text = gui_design.label_design(232, 410, 'EMPLOYEE BASIC INFO:', '#c8d8e4', ('Arial', 11, 'bold'))
emp_basic_income_text = gui_design.label_design(232, 410, 'BASIC INCOME:', '#c8d8e4', ('Arial', 11, 'bold'))
emp_hon_income_text = gui_design.label_design(232, 410, 'HONORARIUM INCOME:', '#c8d8e4', ('Arial', 11, 'bold'))
emp_other_income_text = gui_design.label_design(232, 410, 'OTHER INCOME:', '#c8d8e4', ('Arial', 11, 'bold'))
emp_summary_income_text = gui_design.label_design(232, 410, 'SUMMARY INCOME:', '#c8d8e4', ('Arial', 11, 'bold'))
emp_reg_deductions_text = gui_design.label_design(232, 410, 'REGULAR DEDUCTIONS:', '#c8d8e4', ('Arial', 11, 'bold'))
emp_other_deduc_text = gui_design.label_design(232, 410, 'OTHER DEDUCTIONS:', '#c8d8e4', ('Arial', 11, 'bold'))
emp_deductions_summary_text = gui_design.label_design(232, 410, 'DEDUCTION SUMMARY:', '#c8d8e4', ('Arial', 11, 'bold'))

#large labels
emp_title_text = gui_design.label_design(232, 410, "SERI'S CHOICE PAYROLL", '#c8d8e4', ('Arial', 11, 'bold'))

#different buttons
search_button = gui_design.button_design(1, 1, 30, '#c8d8e4')
gross_income_button = gui_design.button_design(1, 1, 30, '#c8d8e4')
save_button = gui_design.button_design(1, 1, 30, '#c8d8e4')
update_button = gui_design.button_design(1, 1, 30, '#c8d8e4')
next_button = gui_design.button_design(1, 1, 30, '#c8d8e4')

#insert of image
employee_image = gui_design.image_design('C:\\Users\\karlr\\OneDrive\\Documents\\GitHub\\Villamor_CPE201_PLD01E_PUSH\\GUI\\pictures of microsoft\\profile.png', 222, 110, 200, 180)

n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width = 30, height = 1, textvariable = n)
combo_field1['values'] = (' Single', ' Married ', ' Widow', ' Legally Separated', ' Annulled')
combo_field1.place(x=858, y=330)
combo_field1.current()

window.mainloop()