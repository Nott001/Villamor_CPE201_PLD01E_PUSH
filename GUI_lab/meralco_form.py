import gui
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

window = tk.Tk()
window.title("Meralco Assessment Page")
window.geometry('1920x1080')

gui_design = gui.GUIdesign(window)

#header of the page
gui_design.frames(0, 0, 1920, 1080, 'white')
employee_image = gui_design.image_design(r'C:\Users\karlr\OneDrive\Documents\GitHub\Villamor_CPE201_PLD01E_PUSH\GUI_lab\pictures of microsoft\Meralco_Logo.png', 72, 16, 170, 156)
gui_design.label_design(870, 40, 'MERALCO','white', ('Inter', 30, 'bold'))
gui_design.label_design(780, 100, 'APPLICATION FORM','white', ('Inter', 30, 'bold'))
gui_design.frames(0, 189, 1920, 4, '#CD6D00')

#1st section
gui_design.label_design(96, 210, 'Service Type          :','white', ('Inter', 13, 'bold'))
gui_design.label_design(96, 243, 'Service Bundle       :','white', ('Inter', 13, 'bold'))
gui_design.label_design(96, 276, 'Application Type     :','white', ('Inter', 13, 'bold'))
gui_design.label_design(1052, 210, 'Service Purpose         :','white', ('Inter', 13, 'bold'))
gui_design.label_design(1052, 243, 'Applied Load (kW)      :','white', ('Inter', 13, 'bold'))
service_type_box = gui_design.textbox_design(319, 208, 40, 1, 'black', 'white', ('inter', 11))
service_bundle_box = gui_design.textbox_design(319, 241, 40, 1, 'black', 'white', ('inter', 11))
app_type_box = gui_design.textbox_design(319, 274, 40, 1, 'black', 'white', ('inter', 11))
service_purpose_box = gui_design.textbox_design(1314, 208, 40, 1, 'black', 'white', ('inter', 11))
applied_load_box = gui_design.textbox_design(1314, 241, 40, 1, 'black', 'white', ('inter', 11))
gui_design.label_design_with_color(0, 299, '-'*1000,'white', '#CD6D00', ('Inter', 13, 'bold'))

#2nd section sub labels
gui_design.label_design(96, 379, 'I am applying as','white', ('Inter', 13, ''))
gui_design.label_design(96, 457, 'First Name                      :','white', ('Inter', 13, ''))
gui_design.label_design(96, 490, 'Middle Name                   :','white', ('Inter', 13, ''))
gui_design.label_design(96, 523, 'Last Name                      :','white', ('Inter', 13, ''))
gui_design.label_design(96, 556, 'Date of Birth                   :','white', ('Inter', 13, ''))
gui_design.label_design(96, 589, 'Primary Mobile               :','white', ('Inter', 13, ''))
gui_design.label_design(96, 622, 'Phone Number               :','white', ('Inter', 13, ''))
gui_design.label_design(96, 655, 'Email Address                :','white', ('Inter', 13, ''))
gui_design.label_design(96, 688, 'Notification Channel        :','white', ('Inter', 13, ''))
gui_design.label_design(96, 774, 'Province                        :','white', ('Inter', 13, ''))
gui_design.label_design(96, 814, 'City / Municipality           :','white', ('Inter', 13, ''))
gui_design.label_design(96, 854, 'Barangay                       :','white', ('Inter', 13, ''))
gui_design.label_design(96, 894, 'House/Bldg. No.              :','white', ('Inter', 13, ''))
gui_design.label_design(96, 934, 'Landmark                       :','white', ('Inter', 13, ''))

#2nd section labels
gui_design.label_design(72, 333, 'Customer Information','white', ('Inter', 18, 'bold'))
gui_design.label_design(72, 422, 'Customer Details','white', ('Inter', 18, 'bold'))
gui_design.label_design(72, 731, 'Customer Location','white', ('Inter', 18, 'bold'))

#second section text boxes
applying_as_box = gui_design.textbox_design(319, 382, 40, 1, 'black', 'white', ('inter', 11))
first_name_box = gui_design.textbox_design(369, 455, 40, 1, 'black', 'white', ('inter', 11))
middle_name_box = gui_design.textbox_design(369, 488, 40, 1, 'black', 'white', ('inter', 11))
last_name_box = gui_design.textbox_design(369, 521, 40, 1, 'black', 'white', ('inter', 11))
birth_box = gui_design.textbox_design(369, 554, 40, 1, 'black', 'white', ('inter', 11))
mobile_num_box = gui_design.textbox_design(369, 587, 40, 1, 'black', 'white', ('inter', 11))
phone_num_box = gui_design.textbox_design(369, 620, 40, 1, 'black', 'white', ('inter', 11))
email_box = gui_design.textbox_design(369, 653, 40, 1, 'black', 'white', ('inter', 11))
notif_box = gui_design.textbox_design(369, 686, 40, 1, 'black', 'white', ('inter', 11))
province_box = gui_design.textbox_design(369, 774, 40, 1, 'black', 'white', ('inter', 11))
municipality_box = gui_design.textbox_design(369, 814, 40, 1, 'black', 'white', ('inter', 11))
barangay_box = gui_design.textbox_design(369, 854, 40, 1, 'black', 'white', ('inter', 11))
house_building_box = gui_design.textbox_design(369, 894, 40, 1, 'black', 'white', ('inter', 11))
landmark_box = gui_design.textbox_design(369, 934, 40, 2, 'black', 'white', ('inter', 11))

#3rd section frames
gui_design.frames(958, 334, 850, 3, 'black')
gui_design.frames(955, 334, 3, 413, 'black')
gui_design.frames(1805, 334, 3, 413, 'black')
gui_design.frames(958, 744, 850, 3, 'black')
gui_design.frames(958, 401, 847, 2, '#CD6D00')
gui_design.label_design(1212, 348, 'DOCUMENTARY REQUIREMENTS','white', ('Inter', 18, 'bold'))
gui_design.label_design(1314, 378, '( Tick the box if applies )','white', ('Inter', 10))

#3rd section tick boxes
gui_design.tick_box(988, 425, 'Reference BIll', ('Inter', 14))
gui_design.tick_box(988, 460, 'Electrical Permit', ('Inter', 14))
gui_design.tick_box(988, 493, 'Certificate of Electrical Inspection', ('Inter', 14))
gui_design.tick_box(988, 526, 'Deed of Sale', ('Inter', 14))
gui_design.tick_box(988, 559, 'Barangay Certification', ('Inter', 14))
gui_design.tick_box(988, 592, 'LGU Certification', ('Inter', 14))
gui_design.tick_box(988, 625, 'Certificate from HOA', ('Inter', 14))
gui_design.tick_box(988, 658, 'Declaration of Real Property', ('Inter', 14))
gui_design.tick_box(988, 691, 'Contract of Lease', ('Inter', 14))
gui_design.tick_box(1416, 430, 'DTI Permit', ('Inter', 14))
gui_design.tick_box(1416, 460, 'Special Power of Attorney', ('Inter', 14))
gui_design.tick_box(1416, 493, 'Affidavit', ('Inter', 14))
gui_design.tick_box(1416, 526, 'Birth / Marriage Certificate', ('Inter', 14))
gui_design.tick_box(1416, 559, 'TIN (Tax Identification Number)', ('Inter', 14))
gui_design.tick_box(1416, 592, 'Valid ID of Registered Customer', ('Inter', 14))
gui_design.tick_box(1416, 625, 'Valid ID of Representative', ('Inter', 14))
gui_design.tick_box(1416, 658, 'Valid ID of Property Owner', ('Inter', 14))

gui_design.label_design(1416, 696, 'Others:','white', ('Inter', 14))
others_type_box = gui_design.textbox_design(1498, 693, 25, 1, 'black', 'white', ('inter', 11))

#4th section
gui_design.frames(960, 783, 853, 3, 'black')
gui_design.frames(960, 985, 853, 3, 'black')
gui_design.frames(960, 783, 3, 205, 'black')
gui_design.frames(1810, 783, 3, 205, 'black')
gui_design.frames(963, 853, 847, 2, '#CD6D00')
gui_design.label_design(1266, 806, 'LIST OF VALID ID’S','white', ('Inter', 18, 'bold'))

gui_design.label_design(1113, 870, 'Note: Tax Identification Card, Philhealth ID, PRC License, NBI Clearance, '
                                   'Pag-ibig ID, \nSenior Citizen ID, Postal ID.','white', ('Inter', 11))
gui_design.label_design(1113, 935, 'Note: At least 1 valid document from the requirement list.','white', ('Inter', 11))
gui_design.button_design(988, 875, 10, 1, '#6C6C6C', 'UPLOAD')
gui_design.button_design(988, 929, 10, 1, '#6C6C6C', 'UPLOAD')

window.mainloop()
