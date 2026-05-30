import tkinter as ti
from time import strftime

root=ti.Tk()
root.title("DIgital Clock")

def time():
    string=strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time)

label=ti.Label(root,font=('arial',50,'bold'),background='black',foreground='yellow')
label.pack(anchor='centre')

time()

root.mainloop()