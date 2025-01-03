import gui_project
import tkinter as tk

window = tk.Tk()
window.title("Login page")
window.geometry('1920x1080')

gui_design = gui_project.GUIdesign(window)

#Background
gui_design.image_design(r'C:\Users\karlr\OneDrive\Documents\GitHub\Villamor_CPE201_PLD01E_PUSH\GUI_project\project_pics\galax2.png', 0, 0, 1920, 1080)

#labels
gui_design.label_design(627, 140, "Log in", '#B5BBCC', ('Arial', 50, ''))
gui_design.label_design(627, 240, "Need an account?", '#B5BBCC', ('Arial', 14, ''))
gui_design.label_design(627, 320, "Username or Email", '#B5BBCC', ('Arial', 15, 'bold'))
gui_design.label_design(627, 440, "Password", '#B5BBCC', ('Arial', 15, 'bold'))
gui_design.label_design(1645, 30, "Language", 'white', ('Arial', 11))

#textboxes
username = gui_design.textbox_design(627,365, 45, 1, 'black', 'white', ('Calibri', 13))
password = gui_design.textbox_design(627,485, 45, 1, 'black', 'white', ('Calibri', 13))

#buttons
need_account = gui_design.button_design(795, 240, 17, 1, '#AF93C1', 'black', 'Create an account', 1,  ('Arial', 13))
forgot_user = gui_design.button_design(627, 737, 17, 1, '#AF93C1', 'black', 'Forgot Username?', 1,  ('Arial', 13))
forgot_pass = gui_design.button_design(807, 737, 17, 1, '#AF93C1', 'black', 'Forgot Password?', 1,  ('Arial', 13))
cant_login = gui_design.button_design(627, 783, 17, 1, '#AF93C1', 'black', "Can't log in?", 1,  ('Arial', 13))
login = gui_design.button_design(627, 620, 15, 1, '#AF93C1', 'black', "Log in", 2,  ('Arial', 15, 'bold'))

#combobox
country = gui_design.combo_box(1720, 30, 15, 'Filipino', 'English', 'Japanese', ('Arial', 12))

#tickboxes
gui_design.tick_box(627, 540, 'Keep me logged in', ('Arial', 13, 'bold'))

window.mainloop()