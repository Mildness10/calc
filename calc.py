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

def sin():
    sign = e.get()
    global val
    global operator
    operator = 'sin'
    val = sign
    e.delete(0, END)

def cos():
    sign = e.get()
    global val
    global operator
    operator = 'cos'
    val = sign
    e.delete(0, END)

def tan():
    sign = e.get()
    global val
    global operator
    operator = 'tan'
    val = sign
    e.delete(0, END)

def log():
    sign = e.get()
    global val
    global operator
    operator = 'log'
    val = sign
    e.delete(0, END)

def square():
    first_no = e.get()
    global num1
    global operator
    operator = 'square'
    num1 = int(first_no)
    e.delete(0, END)

def square_root():
    sign = e.get()
    global val
    global operator
    operator = 'square_root'
    val = sign
    e.delete(0, END)

def factorial():
    first_no = e.get()
    global num1
    global operator
    operator = 'factorial'
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
    if operator == 'sin':
        e.insert(0, math.sin(math.radians(int(second_no))))
    if operator == 'cos':
        e.insert(0, math.cos(math.radians(int(second_no))))
    if operator == 'tan':
        e.insert(0, math.tan(math.radians(int(second_no)))) 
    if operator == 'log':
        e.insert(0, math.log10(int(second_no)))
    if operator == 'square':
        e.insert(0, num1**2)
    if operator == 'square_root':
        e.insert(0, math.sqrt(int(second_no)))
    if operator == 'factorial':
        e.insert(0, math.factorial(num1))
    

#row_one
sin_but = Button(root, text="sin", padx=30, pady=15, command=sin).grid(row=1,column=0)
cos_but = Button(root, text="cos", padx=29, pady=15, command=cos).grid(row=1,column=1)
tan_but = Button(root, text="tan", padx=29, pady=15, command=tan).grid(row=1,column=2)
log = Button(root, text="log", padx=30, pady=15, command=log).grid(row=1,column=3)
#row_two
xy = Button(root, text="√", padx=33.5, pady=15, command=square_root).grid(row=2,column=0)
xx_but = Button(root, text="x^2", padx=28, pady=15, command=square).grid(row=2,column=1)
x_fac = Button(root, text="x!", padx=33, pady=15, command=factorial).grid(row=2,column=2)
div_but = Button(root, text="/", padx=36, pady=15, command=divide).grid(row=2,column=3)
#row_three
no_7 = Button(root, text="7", padx=35, pady=15, command=lambda: click(7)).grid(row=3,column=0)
no_8 = Button(root, text="8", padx=35, pady=15, command=lambda: click(8)).grid(row=3,column=1)
no_9 = Button(root, text="9", padx=35, pady=15, command=lambda: click(9)).grid(row=3,column=2)
mul_but = Button(root, text="*", padx=35, pady=15, command=multiply).grid(row=3,column=3)
#row_four
no_4 = Button(root, text="4", padx=35, pady=15, command=lambda: click(4)).grid(row=4,column=0)
no_5 = Button(root, text="5", padx=35, pady=15, command=lambda: click(5)).grid(row=4,column=1)
no_6 = Button(root, text="6", padx=35, pady=15, command=lambda: click(6)).grid(row=4,column=2)
sub_but = Button(root, text="-", padx=35, pady=15, command=subtract).grid(row=4,column=3)
#row_five
no_1 = Button(root, text="1", padx=35, pady=15, command=lambda: click(1)).grid(row=5,column=0)
no_2 = Button(root, text="2", padx=35, pady=15, command=lambda: click(2)).grid(row=5,column=1)
no_3 = Button(root, text="3", padx=35, pady=15, command=lambda: click(3)).grid(row=5,column=2)
add_but = Button(root, text="+", padx=35, pady=15, command=add).grid(row=5,column=3)
#row_six
no_0 = Button(root, text="0", padx=35, pady=15, command=lambda: click(0)).grid(row=6,column=0)
clear_but = Button(root, text='C', padx=34, pady=15, command=clear).grid(row=6, column=1)
equal_but = Button(root, text="=", padx=80, pady=15, bg='#1260cc', command=equal).grid(row=6,column=2, columnspan=2)
# div_but = Button(root, text="/", padx=35, pady=15, command=divide).grid(row=6,column=3)





# no_1.pack()

root.mainloop()