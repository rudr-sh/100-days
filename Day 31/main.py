import pandas
from tkinter import *
from random import *
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
#getting data to work with
data=pandas.read_csv("C:/Users/Rudraksh Sharma/Documents/100-days/Day 31/data/french_words.csv")
#functionalities
repeat=False
timer=None
random_row=None
def next_card():
    global random_row,repeat,data,timer
    if timer:
        window.after_cancel(timer)
    if repeat == False and random_row is not None:
        data = data[data["French"] != random_row["French"]]
    try:
        random_row=data.sample().iloc[0]
    except:
        messagebox.showinfo(title="Game Over",message="You've completed the whole game.")
    else:
        show_french()
        timer =window.after(3000,show_english)
        repeat=False
def forgot():
    global repeat
    repeat = True   
    next_card()
def show_french():
    canvas.itemconfig(card_image,image=backgrnd_image2)
    canvas.itemconfig(card_text1,text="French",font=("Georgia",30,"bold italic"))
    canvas.itemconfig(card_text2,text=random_row["French"],font=("Georgia",30,"bold italic"))
def show_english():
    canvas.itemconfig(card_image,image=backgrnd_image1)
    canvas.itemconfig(card_text1,text="English",font=("Georgia",30,"bold italic"))
    canvas.itemconfig(card_text2,text=random_row["English"],font=("Georgia",30,"bold italic"))
    
#GUI
window=Tk()
window.title("Flash Card Game (French v1)")
window.minsize(1000,700)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#cards
canvas=Canvas(height=540,width=830)
backgrnd_image1=PhotoImage(file="C:/Users/Rudraksh Sharma/Documents/100-days/Day 31/images/card_back.png")
backgrnd_image2=PhotoImage(file="C:/Users/Rudraksh Sharma/Documents/100-days/Day 31/images/card_front.png")
card_image=canvas.create_image(430,270,image=backgrnd_image2)
card_text1=canvas.create_text(420,130,text="Click right button to start.",font=("Georgia",30,"bold italic"))
card_text2=canvas.create_text(420,320,text="Learn French",font=("Georgia",30,"bold italic"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=1,padx=10,pady=(0,80),sticky='n')


#Buttons
right_image=PhotoImage(file="C:/Users/Rudraksh Sharma/Documents/100-days/Day 31/images/right.png")
right=Button(image=right_image,command=next_card,height=100,width=100,bg=BACKGROUND_COLOR,highlightthickness=0,bd=0)
right.grid(row=1,column=1,sticky="e",padx=(0,120))

wrong_image=PhotoImage(file="C:/Users/Rudraksh Sharma/Documents/100-days/Day 31/images/wrong.png")
wrong=Button(image=wrong_image,command=forgot,height=100,width=100,bg=BACKGROUND_COLOR,highlightthickness=0,bd=0)
wrong.grid(row=1,column=1,sticky="w",padx=(140,0))
window.mainloop()
