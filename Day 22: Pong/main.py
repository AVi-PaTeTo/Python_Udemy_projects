from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time


def move_ball():
    global paused
    if ball.xcor() in range(430,440) and paddle2.distance(ball) <= 50:
        ball.bounce_x()
    if ball.xcor() in range(-451,-434) and paddle1.distance(ball) <= 40:
        ball.bounce_x()
    if ball.ycor() >= 250 or ball.ycor() <= -285:
        ball.bounce_y()
    if ball.xcor() >= 480:
        scoreboard.update_score(1)
        ball.reset()
        paused = True
        return
    if ball.xcor() <= -480:
        scoreboard.update_score(2)
        ball.reset()
        paused = True
        return
    ball.goto(ball.xcor()+ball.x_velocity, ball.ycor()+ball.y_velocity)


def pause():
    global paused
    if paused == False:
        paused = True
    else:
        paused = False
    screen.update()

screen = Screen()
screen.setup(height=640,width=1000)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
ball=Ball()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
screen.update()

screen.listen()
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")
screen.onkey(pause, "space")

game_is_on = True
paused = True

while game_is_on:
    if not paused:
        move_ball()
    time.sleep(0.1)
    screen.update()
screen.exitonclick()