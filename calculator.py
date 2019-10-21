from tkinter import *
import sqlite3

root = Tk()
root.title("Kim's Calculator")
root.geometry("400x200")

# Defining the math for iem X quantity
def sub():
    num_1 = total_1.get()
    num_1 = int(num_1)
    qt_1 = quantity_1.get()
    qt_1 = float(qt_1)
    sum_1 = num_1 * qt_1 # label 1
    #output label 1
    quantity_1_l = Label(root, text=round(sum_1,2))
    quantity_1_l.grid(row=0, column=5)

    num_2 = total_2.get()
    num_2 = int(num_2)
    qt_2 = quantity_2.get()
    qt_2 = float(qt_2)
    sum_2 = num_2 * qt_2 # label 2
    show = sum_1 +sum_2 # label 3
    
    # Output label 2
    quantity_2_l = Label(root, text=round(sum_2,2))
    quantity_2_l.grid(row=1, column=5)
    # Output label 3
    sub_label = Label(root, text=show)
    sub_label.grid(row=4, column=5)

    
def total():
    num_1 = total_1.get()
    num_1 = int(num_1)
    qt_1 = quantity_1.get()
    qt_1 = float(qt_1)
    
    num_2 = total_2.get()
    num_2 = int(num_2)
    qt_2 = quantity_2.get()
    qt_2 = float(qt_2)
    
    sum_1 = num_1 * qt_1
    sum_2 = num_2 * qt_2
    tax = .07
    tax2 = sum_1 + sum_2
    pretax = ((sum_1 + sum_2) * tax) + tax2 # Grand Total
    
    # Output Grand Total
    total_l = Label(root, text=round(pretax,2))
    total_l.grid(row=5, column=5)

# entry boxes
total_1 = Entry(root, width=15)
total_1.grid(row=0, column=1)
total_2 = Entry(root, width=15)
total_2.grid(row=1, column=1)


# #labels
total_1_l = Label(root, text="   One")
total_1_l.grid(row=0, column=0)
total_2_l = Label(root, text="   Two")
total_2_l.grid(row=1, column=0)


quantity_1 = Entry(root, width=15)
quantity_1.grid(row=0, column=3)
quantity_2 = Entry(root, width=15)
quantity_2.grid(row=1, column=3)

# basically for aesthetics
query_label = Label(root, text="   X   ")
query_label.grid(row=0, column=2,)
query_label = Label(root, text="   X   ")
query_label.grid(row=1, column=2)


# Buttons
sub_btn = Button(root, text="Show Sub Total", command=sub)
sub_btn.grid(row=4, column=2, columnspan=2, padx=10, pady=10, ipadx=25)
tot_btn = Button(root, text="Show Total", command=total)
tot_btn.grid(row=5, column=2, columnspan=2, padx=10, pady=10, ipadx=25)




root.mainloop()