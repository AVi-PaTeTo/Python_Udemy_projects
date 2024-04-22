from turtle import Turtle, Screen
from food import Food
import time

class Snake:
    def __init__(self):
        self.snake = []
        x_cords = [0,-20,-40]
        for x in range(3):
            s = Turtle("square")
            s.pu()
            s.color("white")
            s.setpos(x_cords[x],0)
            self.snake.append(s)

    def grow(self):
        tail = self.snake[-1].pos()
        segment = Turtle("square")
        segment.pu()        
        segment.color("white")
        segment.setpos(tail[0],tail[1])
        self.snake.append(segment)

    def up(self):                               #0 = east, 90 = north, 180 = west, 270 = south
        snake_head = self.snake[0]
        if snake_head.heading() in [0.0,180.0]:
            snake_head.seth(90)

    def down(self):
        snake_head = self.snake[0]                            
        if snake_head.heading() in [0,180]:                      
            snake_head.seth(270)
    
    def left(self):
        snake_head = self.snake[0]
        if snake_head.heading() in [90.0,270.0]:
            snake_head.seth(180)

    def right(self):
        snake_head = self.snake[0]
        if snake_head.heading() in [90,270]:
            snake_head.seth(0)
    
    def forward(self):
        snake_head = self.snake[0]
        old_pos = snake_head.pos()
        snake_head.forward(20)
        for x in range(1, len(self.snake)):
            temp_pos = self.snake[x].pos()
            self.snake[x].setpos(old_pos[0],old_pos[1])
            old_pos = temp_pos

    def snake_pos(self):
        return [x.pos() for x in self.snake]   


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
