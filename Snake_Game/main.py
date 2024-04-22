from turtle import Turtle, Screen
from food import Food
from snake import Snake
import time

SCREEN_SIZE = 600
SCREEN_EDGE = 300 

screen = Screen()
screen.setup(SCREEN_SIZE,SCREEN_SIZE)
screen.bgcolor("black")
screen.tracer(0)

food = Food()
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.17)
    snake.forward()
    if snake.hit_wall(SCREEN_EDGE):
        game_is_on = False
    if snake.bit_yourself():
        game_is_on = False
    if food.get_state(snake.snake_pos()):
        snake.grow()
print("GAME OVER")
screen.exitonclick()