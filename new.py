import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.geometry("800x550")
window.config(background="#cfdd10")
label1=tk.Label(text="This is nothing",font=('italian',30),bg='yellow')
label1.place(x=300,y=20)
entry1=tk.Entry(window,font=('bold',15),bg="#d3770f")
entry1.place(x=300,y=200)
entry2=tk.Entry(window,font=('bold',15),bg="#d3770f")
entry2.place(x=300,y=250)
def display():
    print(vars.get())
vars=tk.StringVar()



radio1=tk.Radiobutton(window,text="male",variable=vars,value='male',font=('bold',15),fg="#141413",bg="#0DE9DE",command=display)
radio1.pack(side='left')
radio2=tk.Radiobutton(window,text="female",variable=vars,value='female',font=('bold',15),fg="#141413",bg="#0DE9DE",command=display)
radio2.pack(side='left')

def name():
    print(option1.get())
    print(option2.get())

option1=tk.BooleanVar()
option2=tk.BooleanVar()
check1=tk.Checkbutton(window,text='indore',variable=option1,font=('bold',15),command=name)
check1.pack(side='bottom')
check2=tk.Checkbutton(window,text='delhi',variable=option2,font=('bold',15),command=name)
check2.pack(side='bottom'  )

def action2():
    n1 = int(entry1.get())
    n2 = int(entry2.get())
    result = n1+n2
    label2=tk.Label(text=f"yoour result is:{result}",bg="#F4EFEF",fg="#141413",font=('bold',25))
    label2.place(x=300,y=300)
    
button=tk.Button(text='calculate',font=('bold',25),command=action2,background="#0f88d3")
button.place(x=300,y=350)
window.mainloop()