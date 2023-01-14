import tkinter as tk
from PIL import Image,ImageTk
root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')
i=0
def flash():
    global i,a
    if a.get() == '0':
        aa = Image.open('.\image\A1.png')
        i = 1
    else:
        aa = Image.open('.\image\A2.png')
        i = 0
    #aa = Image.open('.\image\A2.png')
    img=ImageTk.PhotoImage(aa)
    l1.config(image=img)
    l1.image=img #keep a reference
    root.after(100,flash)
a = tk.StringVar()   # 建立文字變數
a.set('0')

entry = tk.Entry(root,textvariable=a)  # 放入單行輸入框
entry.pack()

l1=tk.Label(root)
l1.pack()
flash()
root.mainloop()