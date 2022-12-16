from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.pack()

e.get()


def click(val):
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(val))

#row_one
no_1 = Button(root, text="1", padx=40, pady=20, command=lambda: click(1)).grid(row=3,column=0)
no_2 = Button(root, text="2", padx=40, pady=20, command=lambda: click(2)).grid(row=3,column=1)
no_3 = Button(root, text="3", padx=40, pady=20, command=lambda: click(3)).grid(row=3,column=2)
#row_two
no_4 = Button(root, text="4", padx=40, pady=20, command=lambda: click(4)).grid(row=2,column=0)
no_5 = Button(root, text="5", padx=40, pady=20, command=lambda: click(5)).grid(row=2,column=1)
no_6 = Button(root, text="6", padx=40, pady=20, command=lambda: click(6)).grid(row=2,column=2)
#row_three
no_7 = Button(root, text="7", padx=40, pady=20, command=lambda: click(7)).grid(row=1,column=0)
no_8 = Button(root, text="8", padx=40, pady=20, command=lambda: click(8)).grid(row=1,column=1)
no_9 = Button(root, text="9", padx=40, pady=20, command=lambda: click(9)).grid(row=1,column=2)
#row_four
no_0 = Button(root, text="0", padx=40, pady=20, command=lambda: click(0)).grid(row=4,column=0)
clear = Button(root, text='C', padx=39, pady=20, command=lambda: click()).grid(row=4, column=1)
equal = Button(root, text="=", padx=39, pady=20, command=lambda: click()).grid(row=4,column=2)










# no_1.pack()

root.mainloop()