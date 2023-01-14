import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

frame1 = tk.Frame(root, pady=10, padx=10, bg='#f90')   # 第一個 Frame 元件
frame2 = tk.Frame(root, pady=10, padx=10, bg='#09c')   # 第二個 Frame 元件

label1 = tk.Label(frame1, text='hello', width=10)      # 放到 frame1 裡的 label
label11 = tk.Label(frame1, text='hello1', width=10)      # 放到 frame1 裡的 label
label1.pack()
label11.pack()

label2 = tk.Label(frame2, text='world', width=10)      # 放到 frame2 裡的 label
label2.pack()

frame2.place(x=20,y=10)   # 先放 frame2
frame1.place(x=20,y=60)   # 再放 frame1

root.mainloop()