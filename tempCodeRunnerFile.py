uare':
        e.insert(0, num1**2)
    if operator == 'square_root':
        e.insert(0, math.sqrt(int(second_no)))
    if operator == 'factorial':
        e.insert(0, math.factorial(num1))
    

#row_one
sin_but = Button(root, text="sin", padx=30, pady=15, command=sin).grid(row=1,column=0)
cos_but = Button(root, text=