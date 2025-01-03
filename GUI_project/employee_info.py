import gui_project
import tkinter as tk

window = tk.Tk()
window.title("Employee Information")
window.geometry('860x1080')

gui_design = gui_project.GUIdesign(window)

#frames
gui_design.frames(0, 0, 860, 1080, 'white')
gui_design.frames(19, 137, 807, 149, '#E3E3E3')
gui_design.frames(19, 304, 807, 149, '#E3E3E3')
gui_design.frames(19, 486, 807, 149, '#E3E3E3')
gui_design.frames(19, 668, 807, 308, '#E3E3E3')

#picture
gui_design.image_design(r'C:\Users\karlr\OneDrive\Documents\GitHub\Villamor_CPE201_PLD01E_PUSH\GUI_project\project_pics\profile.png', 19, 71, 140, 130)

#letterboxes
first_name = gui_design.textbox_design(179,170, 24, 1, 'black', 'white', ('Calibri', 10))
middle_name = gui_design.textbox_design(360,170, 24, 1, 'black', 'white', ('Calibri', 10))
last_name = gui_design.textbox_design(540,170, 25, 1, 'black', 'white', ('Calibri', 10))
suffix = gui_design.textbox_design(728,170, 10, 1, 'black', 'white', ('Calibri', 10))
department = gui_design.textbox_design(34,338, 55, 1, 'black', 'white', ('Calibri', 10))
designation = gui_design.textbox_design(432,338, 24, 1, 'black', 'white', ('Calibri', 10))
emp_status = gui_design.textbox_design(34,394, 65, 1, 'black', 'white', ('Calibri', 10))
emp_number = gui_design.textbox_design(605,394, 28, 1, 'black', 'white', ('Calibri', 10))
contact_number = gui_design.textbox_design(34,520, 45, 1, 'black', 'white', ('Calibri', 10))
email = gui_design.textbox_design(364,520, 62, 1, 'black', 'white', ('Calibri', 10))
soc_med = gui_design.textbox_design(364,576, 62, 1, 'black', 'white', ('Calibri', 10))
address_line1 = gui_design.textbox_design(34,702, 109, 1, 'black', 'white', ('Calibri', 10))
address_line2 = gui_design.textbox_design(34,758, 90, 1, 'black', 'white', ('Calibri', 10))
city_municipality = gui_design.textbox_design(34,814, 54, 1, 'black', 'white', ('Calibri', 10))
state_province = gui_design.textbox_design(426,814, 53, 1, 'black', 'white', ('Calibri', 10))
zip_place = gui_design.textbox_design(426,870, 53, 1, 'black', 'white', ('Calibri', 10))
picture_path = gui_design.textbox_design(34,926, 109, 1, 'black', 'white', ('Calibri', 10))

#comboboxes
gender = gui_design.combo_box(409, 230, 16, 'Female', 'Male', 'Unidentified', ('Calibri', 12))
nationality = gui_design.combo_box(568, 230, 9, 'Filipino', 'American', 'Japanese', ('Calibri', 12))
civil_status = gui_design.combo_box(671, 230, 14, 'Married', 'Single', 'Unidentified', ('Calibri', 12))
qualified_status = gui_design.combo_box(615, 338, 21, 'Facebook', 'Instagram', 'Discord', ('Calibri', 12))
other = gui_design.combo_box(34, 576, 37, 'Married', 'Single', 'Unidentified', ('Calibri', 12))
country = gui_design.combo_box(34, 870, 45, 'Philippines', 'America', 'Japan', ('Calibri', 12))

#dateboxes
birthdate = gui_design.date_entry(179, 230, 25, ('Calibri', 12))
paydate = gui_design.date_entry(502, 394, 9, ('Calibri', 12))

#button
choose_file = gui_design.button_design(19, 211, 11, 1, '#E3E3E3', 'black', 'Choose File', 2,  ('Calibri', 9))
save = gui_design.button_design(19, 985, 12, 1, '#0394EE', 'white', 'Save', 0, ('Calibri', 10))
cancel = gui_design.button_design(115, 985, 12, 1, 'white', 'black', 'Cancel', 2,  ('Calibri', 10))

#texts1
gui_design.label_design(63, 21, "SE-RI’S EMPLOYEE PERSONAL INFORMATION", 'white', ('Century Gothic', 24, 'bold'))
gui_design.label_design(177, 149, "First Name", '#E3E3E3', ('Arial', 9))
gui_design.label_design(358, 149, "Middle Name", '#E3E3E3', ('Arial', 9))
gui_design.label_design(538, 149, "Last Name", '#E3E3E3', ('Arial', 9))
gui_design.label_design(726, 149, "Suffix", '#E3E3E3', ('Arial', 9))
#texts2
gui_design.label_design(176, 209, "Date of Birth", '#E3E3E3', ('Arial', 9))
gui_design.label_design(406, 209, "Gender", '#E3E3E3', ('Arial', 9))
gui_design.label_design(565, 209, "Nationality", '#E3E3E3', ('Arial', 9))
gui_design.label_design(668, 209, "Civil Status", '#E3E3E3', ('Arial', 9))
#texts3
gui_design.label_design(32, 317, "Department", '#E3E3E3', ('Arial', 9))
gui_design.label_design(430, 317, "Designation", '#E3E3E3', ('Arial', 9))
gui_design.label_design(613, 317, "Qualified Dep. Status", '#E3E3E3', ('Arial', 9))
gui_design.label_design(32, 373, "Employee Status", '#E3E3E3', ('Arial', 9))
gui_design.label_design(500, 373, "Paydate", '#E3E3E3', ('Arial', 9))
gui_design.label_design(603, 373, "Employee Number", '#E3E3E3', ('Arial', 9))
#texts4
gui_design.label_design(19, 464, "Contact Info", 'white', ('Arial', 10, 'bold'))
gui_design.label_design(32, 499, "Contact No.", '#E3E3E3', ('Arial', 9))
gui_design.label_design(362, 499, "Email", '#E3E3E3', ('Arial', 9))
gui_design.label_design(32, 555, "Other (Social Media)", '#E3E3E3', ('Arial', 9))
gui_design.label_design(362, 555, "Social Media Account ID/No", '#E3E3E3', ('Arial', 9))
#texts5
gui_design.label_design(19, 646, "Address", 'white', ('Arial', 10, 'bold'))
gui_design.label_design(32, 681, "Address Line 1", '#E3E3E3', ('Arial', 9))
gui_design.label_design(32, 737, "Address Line 2", '#E3E3E3', ('Arial', 9))
gui_design.label_design(32, 793, "City/Municipality", '#E3E3E3', ('Arial', 9))
gui_design.label_design(423, 793, "State/Province", '#E3E3E3', ('Arial', 9))
gui_design.label_design(32, 849, "Country", '#E3E3E3', ('Arial', 9))
gui_design.label_design(424, 849, "Zip Code", '#E3E3E3', ('Arial', 9))
gui_design.label_design(32, 905, "Picture Path", '#E3E3E3', ('Arial', 9))
#other texts
gui_design.label_design(95, 214, "No file chosen", '#E3E3E3', ('Arial', 8))

window.mainloop()