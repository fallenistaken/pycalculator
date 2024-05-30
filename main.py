from tkinter import *
from tkinter import font
import tkinter as tk
import math

# Functions
def exitbutton(event=None):
    root.destroy()

def button_click(event):
    current_text = entry_var.get()
    button_text = event.widget.cget("text")
    
    if button_text == "C":
        entry_var.set("")
    elif button_text == "π":
        entry_var.set("(math.pi)*")
    elif button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    else:
        new_text = current_text + button_text
        entry_var.set(new_text)


root = Tk()
root.geometry("480x600")
root.title("Calculator")
icon = PhotoImage(file='assets/icon.png')
smallicon = PhotoImage(file='assets/smallicon.png')

root.iconphoto(True, icon)

logo = Label(root, text="Calculator", font=('Arial', 10, "bold"),
             bg='#E4E4E4', image=smallicon, compound="left")
logo.grid(row=0, column=0, columnspan=4)

entry_var = tk.StringVar()
entry = Entry(root, font='Arial 25', bd=5, relief=SUNKEN, justify=RIGHT, textvariable=entry_var)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Calculator buttons
buttons = [
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('π', 3, 4),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3), ('**', 4, 4),
    ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('/', 5, 3)
]

for (text, row, column) in buttons:
    btn = Button(root, text=text, font=('Arial', 25))
    btn.grid(row=row, column=column, padx=5, pady=5)
    btn.bind('<Button-1>', button_click)

# Keyboard Shortcuts
root.bind('<Control-Key-q>', exitbutton)
root.bind('<Control-Key-Q>', exitbutton)

root.resizable(False, False)
root.mainloop()
