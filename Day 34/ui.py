from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.minsize(500,600)
        self.window.configure(padx=20,pady=20,background=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250)
        self.canvas.create_text(200/2,250/2,text="Testing Testin Testing this application")
        self.canvas.grid(row=0,column=1)
        
        self.window.mainloop()