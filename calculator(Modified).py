import math
import numpy as np
import cmath
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
def process1():
    try:
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)
        number1=int(number1)
        number2=int(number2)
        if operator =="+":
            answer=number1+number2
        if operator =="-":
            answer=number1-number2
        if operator=="*":
            answer=number1*number2
        if operator=="/":
            answer=number1/number2
        if operator == "//":
            answer=number1//number2
        if operator == "^":
            answer=number1**number2
        L4=Label(tool, text="Answer",).grid(row=6,column=0)
        E4=Entry(tool, bd = 5)
        E4.grid(row=6,column=1)
        Entry.insert(E4,0,answer)
        #print(answer)
    except ValueError:
        messagebox.showinfo("Warning","Please enter the value in integer")
def process2():
    try:
        #Degrees biyochh
        #Radian
        comm=str(Entry.get(E5))
        if comm== 'sine':
            integer1=float(Entry.get(E4))
            integer1=integer1*(3.14/180)
            ans=math.sin(integer1)
        if comm== 'cosine':
            integer1=float(Entry.get(E4))
            integer1=integer1*(3.14/180)
            ans=math.cos(integer1)
        if comm == 'tan':
            integer1=float(Entry.get(E4))
            integer1=integer1*(3.14/180)
            ans=math.sin(integer1)/math.cos(integer1)
        if comm=='binary':
            integer1=int(Entry.get(E4))
            ans=bin(integer1)[2:]
        if comm=='absolute':
            integer1=int(Entry.get(E4))
            ans=abs(integer1)
        if comm == 'decimal':
            integer1=Entry.get(E4)
            ans=int(integer1,2)
        L6=Label(tool,text="Answer",).grid(row=5,column=2)
        E6=Entry(tool,bd=5)
        E6.grid(row=5,column=3)
        Entry.insert(E6,0,ans)
    except ValueError:
        messagebox.showinfo("Warning","Invalid Input")
def process3():
    try:
        r1=int(Entry.get(E6))
        i1=int(Entry.get(E7))
        r2=int(Entry.get(E8))
        i2=int(Entry.get(E9))
        op=Entry.get(E10)
        z1=complex(r1,i1)
        z2=complex(r2,i2)
        if op=='+':
            ans=z1+z2
        if op=='-':
            ans=z1-z2
        if op=='*':
            ans=z1*z2
        if op=='/':
            ans=z1/z2
        L11=Label(tool,text="Answer",).grid(row=8,column=4)
        E11=Entry(tool,bd=5)
        E11.grid(row=8,column=5)
        Entry.insert(E11,0,ans)
    except ValueError:
        messagebox.showinfo("Warning","Fuck Off Bitch it's easy cmon man!!")
tool=Tk()
tool.title("DPS Special Calculator")
k1=Label(tool,text="My Calculator",).grid(row=0,column=3)
k2=Label(tool,text="Select the Type of Operation",).grid(row=1,column=3)
k3=Label(tool,text="Arithmetic",).grid(row=2,column=1)
k4=Label(tool, text ="System Converter/Trigonometric",).grid(row=2,column=3)
k5=Label(tool, text ="Complex",).grid(row=2,column=5)

#For Arithematic
L1=Label(tool,text="Operand1",).grid(row=3,column=0)
L2=Label(tool,text="Operand2",).grid(row=4,column=0)
L3=Label(tool,text="Operator",).grid(row=5,column=0)
E1=Entry(tool,bd=5)
E1.grid(row=3,column=1)
E2=Entry(tool,bd=5)
E2.grid(row=4,column=1)
E3=Entry(tool,bd=5)
E3.grid(row=5,column=1)

#For Log/Trigonometry
L1=Label(tool,text="Operand",).grid(row=3,column=2)
L2=Label(tool,text="Operation",).grid(row=4,column=2)
E4=Entry(tool,bd=5)
E4.grid(row=3,column=3)
E5=Entry(tool,bd=5)
E5.grid(row=4,column=3)

#For Complex
L1=Label(tool,text=" Real1 ",).grid(row=3,column=4)
L2=Label(tool,text=" Imaginary1 ",).grid(row=4,column=4)
L3=Label(tool,text=" Real2 ",).grid(row=5,column=4)
L4=Label(tool,text=" Imaginary2 ",).grid(row=6,column=4)
L5=Label(tool,text=" Operation ",).grid(row=7,column=4)
E6=Entry(tool,bd=5)
E6.grid(row=3,column=5)
E7=Entry(tool,bd=5)
E7.grid(row=4,column=5)
E8=Entry(tool,bd=5)
E8.grid(row=5,column=5)
E9=Entry(tool,bd=5)
E9.grid(row=6,column=5)
E10=Entry(tool,bd=5)
E10.grid(row=7,column=5)

#Buttons
B1=Button(tool, text ="Submit",command = process1).grid(row=6,column=1)
B2=Button(tool, text ="Submit",command = process2).grid(row=5,column=3)
B3=Button(tool, text ="Submit",command = process3).grid(row=8,column=5)
tool.mainloop()