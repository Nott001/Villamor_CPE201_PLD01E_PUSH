import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import ttk

class GUIdesign:
    def __init__(self, window):
        self.window = window
        self.frame1 = ''
        self.textbox = ''
        self.text_value = ''
        self.lbl = ''
        self.upload_button = ''
        self.length = ''
        self.width = ''
        self.image_location = ''
        self.image = ''
        self.bck_pic = ''
        self.calendar = ''
        self.combo_field = ''
        self.checkbox = ''

    def frames(self, x, y, width, height, bg):
        self.frame1 = tk.Frame(self.window, width=width, height=height, border=300, bg=bg)
        self.frame1.place(x=x, y=y)

    def textbox_design(self, x, y, width, height, fg, bg, font):
        self.textbox = tk.Text(width=width, height= height, fg=fg, bg=bg,font=font, border=2, pady=3)
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value, bg, font):
        self.text_value = text_value
        self.lbl = tk.Label(text=text_value, bg=bg, font=font)
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, width, height, bg, fg, text, bd, font):
        self.upload_button = tk.Button(width=width, height=height, text=text,
                                    bg=bg, fg=fg, cursor='hand2', border=bd, font=font)
        self.upload_button.place(x=x, y=y)

    def date_entry(self, x, y, width, font):
        self.calendar = DateEntry(self.window, width=width, bg='darkblue', fg='white', borderwidth=2, font=font)
        self.calendar.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = tk.Label(self.window, image=self.bck_pic, bg='white')
        self.lbl.place(x=x, y=y)

    def combo_box(self, x, y, width, a, b, c, font):
        self.combo_field = ttk.Combobox(self.window, width=width, values=[a, b, c], font=font)
        self.combo_field.place(x=x, y=y)

    def tick_box(self, x, y, text, font):
        self.checkbox = Checkbutton(self.window, text=text, font=font, bg='#B5BBCC', fg='black')
        self.checkbox.place(x=x, y=y)