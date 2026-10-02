import sys
import os
from tkinter import *

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Path when running inside compiled executable folder
        base_path = os.path.dirname(sys.executable)
    else:
        # Path when running regular .py script
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

root = Tk()
root.title("Simple Calculator")
icon_path = get_resource_path("calculator maths icon.png")

if os.path.exists(icon_path):
    icon_img = PhotoImage(file=icon_path)
    root.iconphoto(True, icon_img)

num1 = 0
num2 = 0
Answer = None
sign = ""

InputBox = Entry(root, width=35, borderwidth=5)
InputBox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_number(number):
    Result = (InputBox.get() + str(number))
    InputBox.delete(0,END)
    InputBox.insert(0,Result)
    return

def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def button_clear():
    InputBox.delete(0,END)
    return

def button_CE():
    current = InputBox.get()
    current = current[0:len(current)-1]
    InputBox.delete(0,END)
    InputBox.insert(0,current)
    return

def button_add():
    global sign
    global num1
    sign = "+"
    num1 = InputBox.get()
    InputBox.delete(0,END)
    return

def button_sub():
    global sign
    global num1
    sign = "-"
    num1 = InputBox.get()
    InputBox.delete(0,END)
    return

def button_mul():
    global sign
    global num1
    sign = "*"
    num1 = InputBox.get()
    InputBox.delete(0,END)
    return

def button_div():
    global sign
    global num1
    sign = "/"
    num1 = InputBox.get()
    InputBox.delete(0, END)
    return

def button_equal():
    global sign
    global num1
    global num2
    global Answer
    previousnum2 = num2
    num2 = InputBox.get()
    InputBox.delete(0, END)
    if isfloat(num1) == True and isfloat(num2) == True:
        if float(num2) == Answer:
            num1 = Answer
            num2 = previousnum2

        if sign == "+":
            Answer= float(num1) + float(num2)
            if round(Answer) == Answer:
                Answer = round(Answer)
            InputBox.insert(0, Answer)
        elif sign == "-":
            Answer = float(num1) - float(num2)
            if round(Answer) == Answer:
                Answer = round(Answer)
            InputBox.insert(0, Answer)
        elif sign == "*":
            Answer = float(num1) * float(num2)
            if round(Answer) == Answer:
                Answer = round(Answer)
            InputBox.insert(0, Answer)
        elif sign == "/":
            if float(num2) != 0:
                Answer = float(num1) / float(num2)
                if round(Answer) == Answer:
                    Answer = round(Answer)
                InputBox.insert(0, Answer)
            else:
                InputBox.insert(0, "ERROR")
        else:
            InputBox.insert(0, "ERROR")
    else:
        InputBox.insert(0,"ERROR")
    return

#number buttons
Button7= Button(root, text="7", padx=20, pady=10, command=lambda: button_number(7))
Button7.grid(row=1,column=0)

Button8= Button(root, text="8", padx=20, pady=10, command=lambda: button_number(8))
Button8.grid(row=1,column=1)

Button9= Button(root, text="9", padx=20, pady=10, command=lambda: button_number(9))
Button9.grid(row=1,column=2)

Button4= Button(root, text="4", padx=20, pady=10, command=lambda: button_number(4))
Button4.grid(row=2,column=0)

Button5= Button(root, text="5", padx=20, pady=10, command=lambda: button_number(5))
Button5.grid(row=2,column=1)

Button6= Button(root, text="6", padx=20, pady=10, command=lambda: button_number(6))
Button6.grid(row=2,column=2)

Button1= Button(root, text="1", padx=20, pady=10, command=lambda: button_number(1))
Button1.grid(row=3,column=0)

Button2= Button(root, text="2", padx=20, pady=10, command=lambda: button_number(2))
Button2.grid(row=3,column=1)

Button3= Button(root, text="3", padx=20, pady=10, command=lambda: button_number(3))
Button3.grid(row=3,column=2)

Button0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_number(0))
Button0.grid(row=4,column=1)

#Other buttons
ButtonCr = Button(root, text="C",padx=19, pady=10, command=button_clear)
ButtonCr.grid(row=4,column=0)

ButtonCE = Button(root, text="CE", padx=16, pady=10, command=button_CE)
ButtonCE.grid(row=5, column=0)

ButtonEqual = Button(root, text="=", padx=80, pady=10, command=button_equal)
ButtonEqual.grid(row=5,column=1, columnspan=3,sticky="ew")

ButtonDecimal = Button(root, text=".", padx=20.5, pady=10, command=lambda: button_number("."))
ButtonDecimal.grid(row=4, column=2)

#Calc buttons
ButtonAdd = Button(root, text="+", padx=18, pady=10, command=button_add)
ButtonAdd.grid(row=1,column=3, sticky="ew")

ButtonSub = Button(root, text="-", padx=19, pady=10, command=button_sub)
ButtonSub.grid(row=2, column=3, sticky="ew")

ButtonMul = Button(root, text="x", padx=19, pady=10, command=button_mul)
ButtonMul.grid(row=3, column=3, sticky="ew")

ButtonDiv = Button(root, text="/", padx=19, pady=10, command=button_div)
ButtonDiv.grid(row=4, column=3, sticky="ew")


root.mainloop()