from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.pack()

e.get()


def add():
    return

no_1 = Button(root, text="1", padx=40, pady=20, command=add)
no_2 = Button(root, text="2", padx=40, pady=20, command=add)
no_3 = Button(root, text="3", padx=40, pady=20, command=add)
no_4 = Button(root, text="4", padx=40, pady=20, command=add)
no_5 = Button(root, text="5", padx=40, pady=20, command=add)
no_6 = Button(root, text="6", padx=40, pady=20, command=add)
no_7 = Button(root, text="7", padx=40, pady=20, command=add)
no_8 = Button(root, text="8", padx=40, pady=20, command=add)
no_9 = Button(root, text="9", padx=40, pady=20, command=add)
no_0 = Button(root, text="0", padx=40, pady=20, command=add)



no_1.pack()

root.mainloop()