import tkinter as tk
from tkinter import ttk, messagebox
import math

# Create the main window
root = tk.Tk()
root.title("Triangle Area Calculator")

# Define the canvas size
canvas_width = 400
canvas_height = 300

# Create the canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# Define the circle properties
circle_radius = 10
circle_fill = ''
circle_outline = 'black'

# Define the starting positions for the circles
circle1_x = 50
circle1_y = 50
circle2_x = 200
circle2_y = 100
circle3_x = 150
circle3_y = 200

# Create the circles on the canvas
circle1 = canvas.create_oval(circle1_x-circle_radius, circle1_y-circle_radius,
                             circle1_x+circle_radius, circle1_y+circle_radius,
                             fill=circle_fill, outline=circle_outline, tags='circle')
circle2 = canvas.create_oval(circle2_x-circle_radius, circle2_y-circle_radius,
                             circle2_x+circle_radius, circle2_y+circle_radius,
                             fill=circle_fill, outline=circle_outline, tags='circle')
circle3 = canvas.create_oval(circle3_x-circle_radius, circle3_y-circle_radius,
                             circle3_x+circle_radius, circle3_y+circle_radius,
                             fill=circle_fill, outline=circle_outline, tags='circle')

# Define the line properties
line_width = 1
line_fill = 'black'

# Connect the circles to create a triangle using lines
line1 = canvas.create_line(circle1_x, circle1_y, circle2_x, circle2_y,
                           width=line_width, fill=line_fill, tags='line')
line2 = canvas.create_line(circle2_x, circle2_y, circle3_x, circle3_y,
                           width=line_width, fill=line_fill, tags='line')
line3 = canvas.create_line(circle3_x, circle3_y, circle1_x, circle1_y,
                           width=line_width, fill=line_fill, tags='line')

# Define the text box properties
textbox_width = 10

# Create the text boxes for entering the circle positions
circle1_x_textbox = ttk.Entry(root, width=textbox_width)
circle1_x_textbox.insert(0, str(circle1_x))
circle1_x_textbox.pack()
circle1_y_textbox = ttk.Entry(root, width=textbox_width)
circle1_y_textbox.insert(0, str(circle1_y))
circle1_y_textbox.pack()
circle2_x_textbox = ttk.Entry(root, width=textbox_width)
circle2_x_textbox.insert(0, str(circle2_x))
circle2_x_textbox.pack()
circle2_y_textbox = ttk.Entry(root, width=textbox_width)
circle2_y_textbox.insert(0, str(circle2_y))
circle2_y_textbox.pack()
circle3_x_textbox = ttk.Entry(root, width=textbox_width)
circle3_x_textbox.insert(0, str(circle3_x))
circle3_x_textbox.pack()
circle3_y_textbox = ttk.Entry(root, width=textbox_width)
circle3_y_textbox.insert(0, str(circle3_y))
circle3_y_textbox.pack()

# Define the button function for calculating the area of the triangle
def calculate_area():
    # Get the circle positions from the text boxes or canvas
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

    # Update the circle positions on the canvas
    canvas.coords(circle1, circle1_x-circle_radius, circle1_y-circle_radius,
                  circle1_x+circle_radius, circle1_y+circle_radius)
    canvas.coords(circle2, circle2_x-circle_radius, circle2_y-circle_radius,
                  circle2_x+circle_radius, circle2_y+circle_radius)
    canvas.coords(circle3, circle3_x-circle_radius, circle3_y-circle_radius,
                  circle3_x+circle_radius, circle3_y+circle_radius)
    canvas.coords(line1, circle1_x, circle1_y, circle2_x, circle2_y)
    canvas.coords(line2, circle2_x, circle2_y, circle3_x, circle3_y)
    canvas.coords(line3, circle3_x, circle3_y, circle1_x, circle1_y)

    # Calculate the length of each side of the triangle
    side1 = math.sqrt((circle2_x-circle1_x)**2 + (circle2_y-circle1_y)**2)
    side2 = math.sqrt((circle3_x-circle2_x)**2 + (circle3_y-circle2_y)**2)
    side3 = math.sqrt((circle1_x-circle3_x)**2 + (circle1_y-circle3_y)**2)

    # Calculate the semiperimeter of the triangle
    semiperimeter = (side1 + side2 + side3) / 2

    # Calculate the area of the triangle using Heron's formula
    area = math.sqrt(semiperimeter * (semiperimeter - side1) *
                     (semiperimeter - side2) * (semiperimeter - side3))

    # Get the selected measurement unit from the combobox
    selected_unit = unit_combobox.get()

    # Convert the area to the selected unit
    if selected_unit == 'Square meters':
        area = area / 10000
    elif selected_unit == 'Square feet':
        area = area * 0.092903

    # Update the area label
    area_label.config(text="Area: {:.2f} {}".format(area, selected_unit))

# Create the frame for the text boxes and button
input_frame = ttk.Frame(root)
input_frame.pack(side=tk.TOP, padx=10, pady=10)

# Create the button for calculating the area of the triangle
calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate_area)
calculate_button.pack(side=tk.LEFT)

# Create the combobox for selecting the measurement unit
unit_combobox = ttk.Combobox(input_frame, values=('Square meters', 'Square feet'))
unit_combobox.current(0)
unit_combobox.pack(side=tk.LEFT)

# Create the label for displaying the area of the triangle
area_label = ttk.Label(root, text="Area: 0")
area_label.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()
