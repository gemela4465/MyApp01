import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()

canvas = tk.Canvas(root, width = 500, height = 500)
canvas.pack()
img = Image.open('.\image\A1.png')
tk_img = ImageTk.PhotoImage(img)
a1 = canvas.create_image(0, 0, anchor='nw', image=tk_img)


def move_oval(tt):
    canvas.delete(tt)
    img = Image.open('.\image\A2.png')
    tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor='nw', image=tk_img)
    canvas.after(3000, move_oval)

# Start moving!
move_oval(a1)

root.mainloop()