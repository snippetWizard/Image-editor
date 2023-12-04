from email.mime import image
import tkinter as tk
from tkinter import filedialog, colorchooser
from tkinter import ttk
from turtle import width
from PIL import Image, ImageOps, ImageTk, ImageFilter

pen_color = "black"
pen_size = 5
file_path = ""


def add_image():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="C:/Users/pauls/Downloads")
    image = Image.open(file_path)
    width, height = int(image.width / 2) , int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

def draw(mouseEvent):
    x1, y1 = (mouseEvent.x - pen_size), (mouseEvent.y - pen_size)
    x2, y2 = (mouseEvent.x - pen_size), (mouseEvent.y - pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]

def change_size(size):
    global pen_size
    pen_size = size

def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0,0, image=canvas.image, anchor="nw")

def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0,0, image=image, anchor="nw")
    


root = tk.Tk()


screen_width = root.winfo_screenwidth()  # gettingg the current screen windows size to enter it to full screen
screen_height = root.winfo_screenheight()

# Setting the Root Resolution by width and height
# root.geometry(f"{screen_width}x{screen_height}")
root.geometry("1000x600")

# title of the Window
root.title("Basic Image Editing Tool")

# Setting the Background theme
root.config(bg="white")

left_frame = tk.Frame(root, width=200, height=600, bg="white")
left_frame.pack(side="left", fill="y")


canvas = tk.Canvas(root, width=750, height=600)
canvas.pack()

image_button = tk.Button(left_frame, text="Add Image", bg="white", command=add_image)
image_button.pack(pady=15)

color_button = tk.Button(
    left_frame, text="Change Pen Color", command=change_color, bg="white"
)
color_button.pack(pady=5)

pen_size_frame = tk.Frame(left_frame, bg="white")
pen_size_frame.pack(pady=5)

pen_size_1 = tk.Radiobutton(pen_size_frame, text="Small", value=3, bg="white", command=lambda: change_size(5))
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(pen_size_frame, text="Medium", value=5, bg="white", command=lambda: change_size(10))
pen_size_2.pack(side="left")
pen_size_2.select()

pen_size_3 = tk.Radiobutton(pen_size_frame, text="Large", value=7, bg="white", command=lambda: change_size(15))
pen_size_3.pack(side="left")

clear_button = tk.Button(left_frame, text="Clear", command=clear_canvas, bg="#FF9797")
clear_button.pack(pady=10)

filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
filter_label.pack()

filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur", "Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()
filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))






canvas.bind("<B1-Motion>", draw)

root.mainloop()