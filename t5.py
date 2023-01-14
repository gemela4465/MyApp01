from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
  
def choosepic():
  path_=askopenfilename()
  path.set(path_)
  img_open = Image.open(e1.get())
  img=ImageTk.PhotoImage(file='.\image\A2.gif')
  l1.config(image=img)
  
root=Tk()
root.title('oxxo.studio')
root.geometry('400x400')

path=StringVar()
Button(root,text='选择图片',command=choosepic).pack()
e1=Entry(root,state='readonly',text=path)
e1.pack()
l1=Label(root,text= 'AAA')
l1.pack()
root.mainloop()