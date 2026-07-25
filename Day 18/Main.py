import turtle 
from turtle import *
import random
rgb_colours = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170)]
tim = Turtle()
colormode(255)
tim.teleport(-200,-200)
working = 0
y = -200
def draw_a_dot():
    color = random.choice(rgb_colours)
    tim.dot(20, color[0],color[1],color[2])
    tim.penup()
    tim.fd(50)
    tim.pendown()    
while working<10:
    for front in range(10):
        draw_a_dot()
    y+=50
    tim.teleport(-200,y)
    working+=1
tim.hideturtle()
exitonclick()
screensize(720,720)
