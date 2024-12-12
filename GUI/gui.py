import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from PIL import Image, ImageFilter, ImageEnhance
from tkinter import ttk

class design_gui_interface:
    def __init__(self, window):
        self.window = window
        self.frame1 = ''

    def frames(self, x, y, width, height, bg):
        self.frame1 = Frame(self.window, width=width, height=height, border=20, bg=bg)
        self.frame1.place(x=x, y=y)

    def textbox_design(self, x, y, width, height, fg, bg, font):
        self.textbox = Text (width=width, height= height, fg=fg, bg=bg,font=font)
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value, bg, font):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg=bg, font=font)
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, width, bg):
        self.upload_button = Button(width=width, pady=7, text='Choose File',
                                    bg=bg, fg='white', cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = Label(self.window, image=self.bck_pic)
        self.lbl.place(x=x, y=y)





