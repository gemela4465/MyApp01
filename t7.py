from email.policy import default
import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('300x300')

a = tk.StringVar()   # 定義文字變數
a.set('50,50')
b= tk.StringVar()
b.set('50')

# 定義顯示函式，注意一定要有一個參數
def show(e):
    a.set(f'{scale_v.get()}')
    #b.set(f'{scale_h.get()}')
    #print(a.get())
    b.set(a.get())
    #scale_h.config(variable=int(a.get()))
    



scale_h = tk.Scale(root, from_=0, to=100, orient='horizontal',variable= b, showvalue=0 ,sliderlength=10 ,troughcolor = 'green' ,width= 20 ,length = 200 ,bg ='blue' ,bd = 0 )  # 改變時執行 show
scale_h.place(x = 10 ,y=10)
label = tk.Label(root, textvariable=a)
label.place(x = 10 ,y=10)
scale_v = tk.Scale(root, from_=0, to=100, orient='vertical', command=show)  # 改變時執行 show
scale_v.place(x = 10 ,y=50)
root.mainloop()