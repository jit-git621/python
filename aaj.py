# print("longest substring without repeating characters ")
# data='che nemad jccbc cujgge bejc'
# new=[]
# for i in range(len(data)):
#     a=''
#     for j in range(i,len(data)-1):
#         a+=data[j]
#         if ord(data[i])+1 ==ord(data[i+1]):
#             print('yes')
#     new.append(a)
# print(new)
# data='abcxfghpqrssd'
# new=[]
# a=''
# a=a+data[0]
# for i in range(1,len(data)):
#     if ord(data[i])-1==ord(data[i-1]):
#         a+=data[i]
#     else:
#         new.append(a)
#         a=data[i]
# new.append(a)
# print(new)  
# data=int(input("enter no"))
# def summ(n):
#     if n==0:
#         return 0
#     a=n%10
#     return a+summ(n//10)
# print(summ(data))
# data=157
# sum=0
# while data>0:
#     last=data%10
#     sum+=last 
#     data=data//10   
    
# print(sum)
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.geometry("1500x700")
window.config(background="#cfdd10")
label1=tk.Label(text="i am meena",font=('italian',30),bg='yellow')
label1.place(x=50,y=50)
entry1=tk.Entry(window,font=('bold',25),bg="#d3770f")
entry1.place(x=200,y=100)
entry2=tk.Entry(window,font=('bold',25),bg="#d3770f")
entry2.place(x=200,y=200)


def action2():
    n1=entry1.get()
    n2=entry2.get()
    print(n1+n2)
    

button=tk.Button(text='calculate',font=('bold',25),command=action2(),background="#0f88d3")
button.place(x=500,y=250)
window.mainloop()