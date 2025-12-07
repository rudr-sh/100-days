from turtle import Screen, Turtle
import time
from Snake import Snake
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
snake=Snake()

game_is_on = True
while game_is_on:
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.update()
    time.sleep(0.1)
    snake.move()           
        
screen.exitonclick()
