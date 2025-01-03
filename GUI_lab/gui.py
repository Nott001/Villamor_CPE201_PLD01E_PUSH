import tkinter as tk
from tkinter import *
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
        self.frame_with_text = ''
        self.checkbox = ''
        self.table_frame = ''
        self.table = ''

    def frames(self, x, y, width, height, bg):
        self.frame1 = tk.Frame(self.window, width=width, height=height, border=300, bg=bg)
        self.frame1.place(x=x, y=y)

    def textbox_design(self, x, y, width, height, fg, bg, font):
        self.textbox = tk.Text (width=width, height= height, fg=fg, bg=bg,font=font, border=2, pady=3)
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value, bg, font):
        self.text_value = text_value
        self.lbl = tk.Label(text=text_value, bg=bg, font=font)
        self.lbl.place(x=x, y=y)

    def label_design_with_color(self, x, y, text_value, bg, fg, font):
        self.text_value = text_value
        self.lbl = tk.Label(text=text_value, bg=bg, font=font, fg=fg)
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, width, height, bg, text):
        self.upload_button = tk.Button(width=width, height=height, pady=2, text=text,
                                    bg=bg, fg='white', cursor='hand2', border=1)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
        self.lbl = tk.Label(self.window, image=self.bck_pic, bg='white')
        self.lbl.place(x=x, y=y)

    def table_design(self, x, y, width, height, columns):
        """Create a table with specified columns and 'N/A' placeholders."""
        # Create a frame to hold the table
        self.table_frame = tk.Frame(self.window, width=width, height=height)
        self.table_frame.place(x=x, y=y)

        # Define custom style for the Treeview header
        style = ttk.Style()
        style.theme_use("clam")

        # Create and configure a custom style for the header
        style.configure(
            "Custom.Treeview.Heading",  # Header style name
            background="#A70000",  # Header background color
            foreground="white",  # Header text color
            font=("Arial", 10, "bold")  # Font for the header
        )

        # Create the Treeview widget
        self.table = ttk.Treeview(
            self.table_frame,
            columns=columns,
            show="headings",  # To show only headings
            height=10,
            style="Custom.Treeview",  # Apply custom style to Treeview
        )

        # Define the column headers and widths
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=int(width / len(columns)))  # Distribute the width evenly

        # Add a scrollbar for the table
        scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the table into the frame
        self.table.pack(side="left", fill="both", expand=True)

    def add_row_to_table(self, row_data):
        """Add a new row of data to the table."""
        current_index = len(self.table.get_children()) + 1  # Calculate new row's index
        new_row = [current_index] + row_data  # Include the index as the first column value
        self.table.insert("", tk.END, values=new_row)

    def tick_box(self, x, y, text, font):
        self.checkbox = Checkbutton(self.window, text=text, font=font, bg='white', fg='black')
        self.checkbox.place(x=x, y=y)

