from tkinter import *
import math

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=15, pady=15)
# e.pack()

e.get()


def click(val):
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(val))
    
def clear():
    e.delete(0, END)
    
def add():
    first_no = e.get()
    global num1
    global operator
    operator = 'addition'
    num1 = int(first_no)
    e.delete(0, END)

def subtract():
    first_no = e.get()
    global num1
    global operator
    operator = 'subtraction'
    num1 = int(first_no)
    e.delete(0, END)

def multiply():
    first_no = e.get()
    global num1
    global operator
    operator = 'multiplication'
    num1 = int(first_no)
    e.delete(0, END)

def divide():
    first_no = e.get()
    global num1
    global operator
    operator = 'division'
    num1 = int(first_no)
    e.delete(0, END)

def equal():
    second_no = e.get()
    e.delete(0, END)
    
    if operator == "addition":
        e.insert(0, num1 + int(second_no))
    if operator == "subtraction":
        e.insert(0, num1 - int(second_no))
    if operator == "multiplication":
        e.insert(0, num1 * int(second_no))
    if operator == "division":
        e.insert(0, num1 / int(second_no))
    

# 
#row_one
no_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7)).grid(row=1,column=0)
no_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8)).grid(row=1,column=1)
no_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9)).grid(row=1,column=2)
mul_but = Button(root, text="*", padx=40, pady=20, command=multiply).grid(row=1,column=3)
#row_two
no_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4)).grid(row=2,column=0)
no_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5)).grid(row=2,column=1)
no_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6)).grid(row=2,column=2)
sub_but = Button(root, text="-", padx=40, pady=20, command=subtract).grid(row=2,column=3)
#row_three
no_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1)).grid(row=3,column=0)
no_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2)).grid(row=3,column=1)
no_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3)).grid(row=3,column=2)
add_but = Button(root, text="+", padx=40, pady=20, command=add).grid(row=3,column=3)
#row_four
no_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0)).grid(row=4,column=0)
clear_but = Button(root, text='C', padx=39, pady=20, command=clear).grid(row=4, column=1)
equal_but = Button(root, text="=", padx=39, pady=20, command=equal).grid(row=4,column=2)
div_but = Button(root, text="/", padx=40, pady=20, command=divide).grid(row=4,column=3)





# no_1.pack()

root.mainloop()