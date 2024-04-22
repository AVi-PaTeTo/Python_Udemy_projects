from turtle import Turtle, Screen
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

f = Food()
sn = Snake()

screen.listen()
screen.onkey(sn.up,"Up")
screen.onkey(sn.down,"Down")
screen.onkey(sn.left,"Left")
screen.onkey(sn.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.17)
    sn.forward()
    if f.get_state(sn.snake_pos()):
        sn.grow()
screen.exitonclick()