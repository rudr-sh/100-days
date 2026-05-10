from tkinter import *

window= Tk()
window.title("Tkinter")
window.minsize(500,300)
my_label= Label(text="I am a label",font=("Arial",24,"italic"))
my_label.grid(column=0,row=0)
my_label["text"] = "NEW TEXT"  
my_label.config(text="New Text")

def button_clicked():
    my_label.config(text=input_lelo.get())
    button.config(text="I got clicked")

button = Button(text="Click Me",anchor="n",command=button_clicked)
button.grid(column=3,row=0)
input_lelo=Entry()
input_lelo.grid(column=3,row=4)

window.mainloop()