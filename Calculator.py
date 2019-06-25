from tkinter import *
import parser

root = Tk()
root.title("Calculator")
# display text field
text_field = Entry(root)
text_field.grid(row=0, columnspan=8, sticky=W+E)
# Getting input from user
i = 0


def send_num(val):
    global i
    text_field.insert(i, val)
    i += 1


# Getting operator
def send_operator(operator):
    global i
    length = len(operator)
    text_field.insert(i, operator)
    i += length
    
    
    

# Backspace function
def clear_last_val():
    global i
    entire_string = text_field.get()
    new_string = entire_string[0:-1]
    len_new_string = len(entire_string)
    if len_new_string > 0:
        clear_all()
        text_field.insert(0, new_string)
    else:
        text_field.insert(0, "Error")


# Clear All
def clear_all():
    text_field.delete(0, END)


# Calculate Data
def calculate():
    to_calculate = text_field.get()
    try:
        a = parser.expr(to_calculate).compile()
        result = eval(a)
        clear_all()
        text_field.insert(0, result)
    except:
        clear_all()
        text_field.insert(0, "Error")


# Adding Buttons to the Calculator
Button(root, text="1", command=lambda: send_num(1)).grid(row=1, column=0)
Button(root, text="2", command=lambda: send_num(2)).grid(row=1, column=1)
Button(root, text="3", command=lambda: send_num(3)).grid(row=1, column=2)
Button(root, text="4", command=lambda: send_num(4)).grid(row=2, column=0)
Button(root, text="5", command=lambda: send_num(5)).grid(row=2, column=1)
Button(root, text="6", command=lambda: send_num(6)).grid(row=2, column=2)
Button(root, text="7", command=lambda: send_num(7)).grid(row=3, column=0)
Button(root, text="8", command=lambda: send_num(8)).grid(row=3, column=1)
Button(root, text="9", command=lambda: send_num(9)).grid(row=3, column=2)
Button(root, text="0", command=lambda: send_num(0)).grid(row=4, column=1)
Button(root, text=".", command=lambda: send_operator(".")).grid(row=4, column=0)
Button(root, text="=", command=lambda: calculate()).grid(row=4, column=2)
Button(root, text="C", command=lambda: clear_last_val()).grid(row=1, column=3)
Button(root, text="AC", command=lambda: clear_all()).grid(row=1, column=4)
Button(root, text="+", command=lambda: send_operator("+")).grid(row=2, column=3)
Button(root, text=" -  ", command=lambda: send_operator("-")).grid(row=2, column=4)
Button(root, text="x ", command=lambda: send_operator("*")).grid(row=3, column=3)
Button(root, text=" ÷ ", command=lambda: send_operator("/")).grid(row=3, column=4)
Button(root, text="%", command=lambda: send_operator("%")).grid(row=4, column=3)
Button(root, text=" √ ", command=lambda: send_operator("√")).grid(row=4, column=4)
Button(root, text="x^y", command=lambda: send_operator("**")).grid(row=1, column=5)
Button(root, text="  x!  ").grid(row=2, column=5)
Button(root, text="  π  ", command=lambda: send_operator("*3.14")).grid(row=3, column=5)
Button(root, text="   (   ", command=lambda: send_operator("(")).grid(row=4, column=5)
Button(root, text="Log", command=lambda: send_operator("log")).grid(row=1, column=6)
Button(root, text=" Sin", command=lambda: send_operator("sin")).grid(row=2, column=6)
Button(root, text="Cos", command=lambda: send_operator("cos")).grid(row=3, column=6)
Button(root, text="   )  ", command=lambda: send_operator(")")).grid(row=4, column=6)


root.mainloop()

