from tkinter import *
from datetime import date

root =  Tk()
root.title('Getting Started with Wigdets')
root.geometry('400x300')

ibl = Label(text = "hey there!", fg = "white", bg = "#072F5F", height = 1, width = 300)
name_ibl = Label(text = "Full Name", bg = "#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()

    global Message
    message = "Welcome to the Application!\nToday's date is: "
    greet = "Hello"+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="begin", command = display, height = 1, bg = "#1261A0", fg = 'white')

ibl.pack()
name_ibl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()