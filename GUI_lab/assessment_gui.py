import gui
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Student Assessment Page")
window.geometry('1920x1080')

# Load the image with Pillow
image = Image.open(r'C:\Users\karlr\OneDrive\Documents\GitHub\Villamor_CPE201_PLD01E_PUSH\GUI_lab\pictures of microsoft\lpu_cover.jpg')
bck_pic = ImageTk.PhotoImage(image.resize((1920, 1080)))
lbl = tk.Label(window, image=bck_pic)
lbl.place(x=0, y=0)

gui_design = gui.GUIdesign(window)

#header for the page
gui_design.frames(0, 0, 240, 119, 'white')
gui_design.frames(240, 0, 1680, 119, '#A70000')
logo_image = gui_design.image_design(r'C:\Users\karlr\OneDrive\Documents\GitHub\Villamor_CPE201_PLD01E_PUSH\GUI_lab\pictures of microsoft\LPU_CAVITE-removebg-preview.png', 60, 0, 110, 115)
title_text = gui_design.label_design(575, 35, 'LYCEUM OF THE PHILIPPINES UNIVERSITY - CAVITE','#A70000', ('Times New Roman', 25))

#assessment first part texts
gui_design.label_design(850, 130, '1st Semester, AY 2024-2025','white', ('HedvigLettersSerif.ttf', 10))
gui_design.label_design(825, 170, 'ENROLLMENT ASSESSMENT FORM','white', ('HedvigLettersSerif.ttf', 10))

gui_design.frames(44, 210, 1800, 90, 'white')
gui_design.label_design(59, 212, 'Student Name                                                      :','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 232, 'Programs                                                             :','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 253, 'Status                                                                  :','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 274, 'Academic Year                                                   :','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(1080, 211, 'Student No.                                                       :','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(1080, 231, 'Year Level                                                        :','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(1080, 252, 'Section                                                              :','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(1080, 272, 'Semester                                                           :','white', ('HedvigLettersSerif.ttf', 8))

#assessment first part text box
student_name_box = gui_design.textbox_design(360, 212, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
programs_box = gui_design.textbox_design(360, 233, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
status_box = gui_design.textbox_design(360, 254, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
acad_year_box = gui_design.textbox_design(360, 275, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
stud_no_box = gui_design.textbox_design(1375, 212, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
year_lvl_box = gui_design.textbox_design(1375, 233, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
section_box = gui_design.textbox_design(1375, 254, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
semester_box = gui_design.textbox_design(1375, 275, 40, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))

#table creation for academic year
columns = [ "#", "Course Code", "Description", "Section", "Lec Units", "Lab Units", "Tuition Units", "Professor", "Schedule"]
gui_design.table_design(x=44, y=305, width=1800, height=500, columns=columns)
rows_1 = [ "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
rows_2 = [ "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
rows_3 = [ "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
rows_4 = [ "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
rows_5 = [ "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
rows_6 = [ "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
gui_design.add_row_to_table(rows_1)
gui_design.add_row_to_table(rows_2)
gui_design.add_row_to_table(rows_3)
gui_design.add_row_to_table(rows_4)
gui_design.add_row_to_table(rows_5)
gui_design.add_row_to_table(rows_6)

#displaying total
gui_design.frames(44, 550, 1800, 35, 'white')
gui_design.label_design(44, 557, 'TOTAL:','white', ('HedvigLettersSerif.ttf', 10))

#tuition assessment
gui_design.frames(44, 600, 1800, 390, 'white')
gui_design.frames(543, 945, 445, 1, 'black')
gui_design.label_design(59, 600, 'Total Tuition Fee','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 621, 'Miscellaneous Fees','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 642, 'Other Fees','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(76, 664, 'LMS Fee                                                                                                                :','white', ('HedvigLettersSerif.ttf', 7))
gui_design.label_design(76, 682, 'Computer Laboratory Fee                                                                                        :','white', ('HedvigLettersSerif.ttf', 7))
gui_design.label_design(76, 700, 'Computer Laboratory Fee2                                                                                       :','white', ('HedvigLettersSerif.ttf', 7))
gui_design.label_design(76, 718, 'Professional Engineering Laboratory Fee                                                                    :','white', ('HedvigLettersSerif.ttf', 7))
gui_design.label_design(76, 736, 'Exam Booklet                                                                                                          :','white', ('HedvigLettersSerif.ttf', 7))
gui_design.label_design(59, 758, 'Installment Charge','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 779, 'TOTAL TUITION & FEES','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 814, 'Add:','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 831, 'Less:','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(76, 850, 'Downpayment','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(76, 870, 'Payment 1','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(76, 890, 'Payment 2','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(76, 910, 'Payment 3','white', ('HedvigLettersSerif.ttf', 8))
gui_design.label_design(59, 953, 'Balance / ( Refund )','white', ('HedvigLettersSerif.ttf', 8))

#tuition assessment textbox
gui_design.textbox_design(525, 659, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(525, 679, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(525, 699, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(525, 719, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(525, 739, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 601, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 622, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 759, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 780, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 848, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 869, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 890, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 911, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(770, 955, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))

#tuition assessment textbox due date
gui_design.label_design(1200, 600, 'Due Date','white', ('HedvigLettersSerif.ttf', 8))
gui_design.textbox_design(1120, 848, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(1120, 869, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(1120, 890, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))
gui_design.textbox_design(1120, 911, 30, 1, 'black', 'white', ('HedvigLettersSerif.ttf', 10))

gui_design.frames(0, 990, 1920, 25, '#A70000')

window.mainloop()