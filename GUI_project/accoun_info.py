import gui_project
import tkinter as tk

window = tk.Tk()
window.title("Account Information")
window.geometry('860x540')

gui_design = gui_project.GUIdesign(window)

#frames
gui_design.frames(0, 0, 860, 540, 'white')
gui_design.frames(22, 153, 807, 282, '#E3E3E3')

#textboxes
first_name = gui_design.textbox_design(204,193, 16, 1, 'black', '#D0D0D0', ('Calibri', 10))
middle_name = gui_design.textbox_design(327,193, 18, 1, 'black', '#D0D0D0', ('Calibri', 10))
last_name = gui_design.textbox_design(464,193, 16, 1, 'black', '#D0D0D0', ('Calibri', 10))
suffix = gui_design.textbox_design(587,193, 16, 1, 'black', '#D0D0D0', ('Calibri', 10))
department = gui_design.textbox_design(710,193, 14, 1, 'black', '#D0D0D0', ('Calibri', 10))

designation = gui_design.textbox_design(45,267, 33, 1, 'black', '#D0D0D0', ('Calibri', 10))
username = gui_design.textbox_design(287,267, 29, 1, 'black', 'white', ('Calibri', 10))
password = gui_design.textbox_design(501,267, 33, 1, 'black', 'white', ('Calibri', 10))

confirm_password = gui_design.textbox_design(45,341, 33, 1, 'black', 'white', ('Calibri', 10))
user_type = gui_design.textbox_design(287,341, 29, 1, 'black', 'white', ('Calibri', 10))
user_status = gui_design.textbox_design(501,341, 21, 1, 'black', 'white', ('Calibri', 10))
emp_number = gui_design.textbox_design(659,341, 21, 1, 'black', 'white', ('Calibri', 10))

#labels
gui_design.label_design(29, 30, "User Account Information", 'white', ('Arial', 24, ''))
gui_design.label_design(203,169, "First Name", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(326,169, "Middle Name", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(463,169, "Last Name", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(586,169, "Suffix", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(709,169, "Department", '#E3E3E3', ('Arial', 10, ''))

gui_design.label_design(43,245, "Designation", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(285,245, "Username", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(499,245, "Password", '#E3E3E3', ('Arial', 10, ''))

gui_design.label_design(43,319, "Confirm Password", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(285,319, "User Type", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(499,319, "User Status", '#E3E3E3', ('Arial', 10, ''))
gui_design.label_design(657,319, "User Status", '#E3E3E3', ('Arial', 10, ''))

#buttons
update = gui_design.button_design(191, 387, 12, 1, '#1B76FF', 'white', 'Update', 0,  ('Arial', 10))
delete = gui_design.button_design(297, 387, 12, 1, '#F1A72F', 'black', 'Delete', 0,  ('Arial', 10))
cancel = gui_design.button_design(403, 387, 12, 1, '#E3E3E3', 'black', 'Cancel', 1,  ('Arial', 10))

#insert image
gui_design.image_design(r'C:\Users\karlr\OneDrive\Documents\GitHub\Villamor_CPE201_PLD01E_PUSH\GUI_project\project_pics\profile.png', 28, 83, 154, 135)

window.mainloop()