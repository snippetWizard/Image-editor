import tkinter as tk
from tkinter import filedialog, colorchooser
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


root.mainloop()