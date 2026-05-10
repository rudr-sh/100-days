from tkinter import *

window=Tk()
window.minsize(400,300)
window.title("Miles to Km converter")
def convert():
    num=float(miles.get())
    km=num*1.609
    font2.config(text=f"is equal to  {km}  KM",font={50})
miles=Entry()
miles.place(x=145,y=90)

font1=Label(text="Miles",font={50})
font1.place(x=260,y=90)
convert = Button(text="Convert",command=convert)
convert.place(x=145,y=160)
font2=Label(text=f"is equal to  ___  KM",font={50})
font2.place(x=145,y=130)






window.mainloop()
