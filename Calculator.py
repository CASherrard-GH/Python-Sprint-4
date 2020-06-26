#c|/|x|-|
#7|8|9|+|
#4|5|6|+|
#1|2|3|e|
#0|0|.|e|
import math
from tkinter import *


root = Tk()
memory=0
user_input=input("""Please enter usernaem:
>""")
root.title(f"{user_input}'s Calculator")

e = Entry(root, width=35, borderwidth=5 )
e.grid(row=0, column = 0, columnspan=4,  padx=10, pady = 10)
memory=0
def button_click(number):
    memory = e.get()
    e.delete(0,END)
    e.insert(0, str(memory) +str(number))   
    
def clear_screen(num_one):
    e.delete(0,END) 
    
def add():
    num_one = e.get()
    global check
    global number_one_a
    number_one_a = int(num_one)
    check = "add"
    e.delete(0,END)

    
def subtract():
    num_one = e.get()
    global check
    global number_one_s
    number_one_s = int(num_one)
    check = "subtract"
    e.delete(0,END)

def divide():
    num_one = e.get()
    global check
    global number_one_d
    number_one_d = int(num_one)
    check = "divide"
    e.delete(0,END)

def multiply():

    num_one = e.get()
    global check
    global number_one_m
    number_one_m = int(num_one)
    check = "multiply"
    global asd 
    asd = e.get
    e.delete(0,END)

def up():
    f = asd
    e.insert(0,f)
    
def equal():
    if check == "subtract":
        next_nums = e.get()
        e.delete(0, END)
        e.insert(0, number_one_s - int(next_nums))
    
    
    if check == "add":
        next_num = e.get()
        e.delete(0, END)
        e.insert(0, number_one_a + int(next_num))


 
    if check == "divide":
        next_num = e.get()
        e.delete(0, END)
        e.insert(0, number_one_d / float(next_num))
 
    if check == "multiply":
        next_num = e.get()
        e.delete(0, END)
        e.insert(0, number_one_m * float(next_num))
 
 
    
button_up = Button(root, text = "^",padx=28, pady=20, bg = "white", fg = "black", command = up).grid(row=5, column = 1)
button_0 = Button(root, text = "0", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(0)).grid(row=5, column = 0)
button_1 = Button(root, text = "1", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(1)).grid(row=4, column = 0)
button_2 = Button(root, text = "2", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(2)).grid(row=4, column = 1)
button_3 = Button(root, text = "3", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(3)).grid(row=4, column = 2)
button_4 = Button(root, text = "4", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(4)).grid(row=3, column = 0)
button_5 = Button(root, text = "5", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(5)).grid(row=3, column = 1)
button_6 = Button(root, text = "6", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(6)).grid(row=3, column = 2)
button_7 = Button(root, text = "7", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(7)).grid(row=2, column = 0)
button_8 = Button(root, text = "8", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(8)).grid(row=2, column = 1)    
button_9 = Button(root, text = "9", padx=28, pady = 20, bg = "white", fg = "black", command = lambda : button_click(9)).grid(row=2, column = 2)
button_Enter = Button(root, text = "=", padx=65, pady=20, bg = "white", fg = "black", command = equal).grid(row=5, column = 2, columnspan = 100)
button_Multiply = Button(root, text = "x",padx=28, pady=20, bg = "white", fg = "black", command = multiply).grid(row=1, column = 2)
button_Divide = Button(root, text = "%",padx=28, pady=20, bg = "white", fg = "black", command = divide).grid(row=1, column = 1)
button_Plus = Button(root, text = "+", padx=26, pady=55, bg = "white", fg = "black", command = add).grid(row=3, column = 3, rowspan = 2)
button_Minus = Button(root, text = "-", padx=26, pady=55, bg = "white", fg = "black", command = subtract).grid(row=1, column = 3, rowspan = 2)
button_Clear = Button(root, text = "C",padx=28, pady=20, bg = "white", fg = "black", command =  clear_screen).grid(row=1, column = 0)




   
root.mainloop()

