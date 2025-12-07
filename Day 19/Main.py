from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Turtle Race",prompt="Choose your turtle")
colors = ["red","orange","yellow","green","blue","purple"]
y_posn = [-100,-60,-20,20,60,100]
for n in range(0,5):
    tim1 = Turtle("turtle")
    tim1.penup()
    tim1.goto(x=-240,y=y_posn[n])
    tim1.color(colors[n])



screen.exitonclick()    
