import tkinter as tk
from tkinter import ttk, messagebox
import math
import customtkinter as ctk

root = ctk.CTk()
root.title("Triangle Area Calculator")
root.resizable(False, False)

canvas_width = 400
canvas_height = 300

canvas = ctk.CTkCanvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(side=tk.LEFT, padx=10, pady=10)

circle_radius = 10
circle_fill = ''
circle_outline = 'black'

circle1_x = 50
circle1_y = 50
circle2_x = 200
circle2_y = 100
circle3_x = 150
circle3_y = 200

circle1 = canvas.create_oval(circle1_x-circle_radius, circle1_y-circle_radius,
                             circle1_x+circle_radius, circle1_y+circle_radius,
                             fill=circle_fill, outline=circle_outline, tags='circle')
circle2 = canvas.create_oval(circle2_x-circle_radius, circle2_y-circle_radius,
                             circle2_x+circle_radius, circle2_y+circle_radius,
                             fill=circle_fill, outline=circle_outline, tags='circle')
circle3 = canvas.create_oval(circle3_x-circle_radius, circle3_y-circle_radius,
                             circle3_x+circle_radius, circle3_y+circle_radius,
                             fill=circle_fill, outline=circle_outline, tags='circle')

line_width = 1
line_fill = 'black'

line1 = canvas.create_line(circle1_x, circle1_y, circle2_x, circle2_y,
                           width=line_width, fill=line_fill, tags='line')
line2 = canvas.create_line(circle2_x, circle2_y, circle3_x, circle3_y,
                           width=line_width, fill=line_fill, tags='line')
line3 = canvas.create_line(circle3_x, circle3_y, circle1_x, circle1_y,
                           width=line_width, fill=line_fill, tags='line')

textbox_width = 200

circle1_x_textbox = ctk.CTkEntry(root, width=textbox_width)
circle1_x_textbox.insert(0, str(circle1_x))
circle1_x_textbox.pack(pady=(25, 0))
circle1_y_textbox = ctk.CTkEntry(root, width=textbox_width)
circle1_y_textbox.insert(0, str(circle1_y))
circle1_y_textbox.pack()
circle2_x_textbox = ctk.CTkEntry(root, width=textbox_width)
circle2_x_textbox.insert(0, str(circle2_x))
circle2_x_textbox.pack()
circle2_y_textbox = ctk.CTkEntry(root, width=textbox_width)
circle2_y_textbox.insert(0, str(circle2_y))
circle2_y_textbox.pack()
circle3_x_textbox = ctk.CTkEntry(root, width=textbox_width)
circle3_x_textbox.insert(0, str(circle3_x))
circle3_x_textbox.pack()
circle3_y_textbox = ctk.CTkEntry(root, width=textbox_width)
circle3_y_textbox.insert(0, str(circle3_y))
circle3_y_textbox.pack()

def calculate_area():
    try:
        circle1_x = int(circle1_x_textbox.get())
        circle1_y = int(circle1_y_textbox.get())
        circle2_x = int(circle2_x_textbox.get())
        circle2_y = int(circle2_y_textbox.get())
        circle3_x = int(circle3_x_textbox.get())
        circle3_y = int(circle3_y_textbox.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input for circle positions!")
        return

    canvas.coords(circle1, circle1_x-circle_radius, circle1_y-circle_radius,
                  circle1_x+circle_radius, circle1_y+circle_radius)
    canvas.coords(circle2, circle2_x-circle_radius, circle2_y-circle_radius,
                  circle2_x+circle_radius, circle2_y+circle_radius)
    canvas.coords(circle3, circle3_x-circle_radius, circle3_y-circle_radius,
                  circle3_x+circle_radius, circle3_y+circle_radius)
    canvas.coords(line1, circle1_x, circle1_y, circle2_x, circle2_y)
    canvas.coords(line2, circle2_x, circle2_y, circle3_x, circle3_y)
    canvas.coords(line3, circle3_x, circle3_y, circle1_x, circle1_y)

    side1 = math.sqrt((circle2_x-circle1_x)**2 + (circle2_y-circle1_y)**2)
    side2 = math.sqrt((circle3_x-circle2_x)**2 + (circle3_y-circle2_y)**2)
    side3 = math.sqrt((circle1_x-circle3_x)**2 + (circle1_y-circle3_y)**2)

    semiperimeter = (side1 + side2 + side3) / 2

    area = math.sqrt(semiperimeter * (semiperimeter - side1) *
                     (semiperimeter - side2) * (semiperimeter - side3))

    selected_unit = unit_combobox.get()

    if selected_unit == 'Square meters':
        area = area / 10000
    elif selected_unit == 'Square kilometers':
        area = area / 1000000
    elif selected_unit == 'Square centimeters':
        area = area * 10000
    elif selected_unit == 'Acres':
        area = area * 0.000247105
    elif selected_unit == 'Hectares':
        area = area * 0.0001
    elif selected_unit == 'Square feet':
        area = area * 0.092903
    elif selected_unit == 'Square inches':
        area = area * 144
    elif selected_unit == 'Square yards':
        area = area * 0.111111
    elif selected_unit == 'Square miles':
        area = area / 2589988.11
    elif selected_unit == 'Square millimeters':
        area = area * 1000000

    area_label.configure(text="Area: {:.2f} {}".format(area, selected_unit))

input_frame = ctk.CTkFrame(root)
input_frame.pack(side=tk.TOP, padx=10, pady=25)

calculate_button = ctk.CTkButton(input_frame, width=10, text="Calculate", fg_color="#50cc55", command=calculate_area)
calculate_button.pack(side=tk.LEFT)

unit_combobox = ctk.CTkOptionMenu(input_frame, fg_color="#50cc55", button_color="#5ab85e", values=('Square meters', 'Square kilometers', 'Square centimeters',
                                                  'Acres', 'Hectares', 'Square feet', 'Square inches',
                                                  'Square yards', 'Square miles', 'Square millimeters'))
unit_combobox.set("Square meters")
unit_combobox.pack(side=tk.LEFT)

area_label = ctk.CTkLabel(root, text="Area: 0")
area_label.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()
