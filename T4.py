from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
root = Tk()
root.title('oxxo.studio')
root.geometry('200x200')
i=0
def flash():
    global i
    if i == 0:
        aa = Image.open('.\image\A1.png')
        i = 1
    else:
        aa = Image.open('.\image\A2.png')
        i = 0
    img=ImageTk.PhotoImage(aa)
    l1.config(image=img)
    l1.image=img #keep a reference
    root.after(1000,flash)



l1=Label(root)
l1.pack()
flash()
root.mainloop()