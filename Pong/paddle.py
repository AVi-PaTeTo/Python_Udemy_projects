from turtle import Turtle,colormode

RED = (255,28,28)
BLUE = (0,255,255)
class Paddle(Turtle):

    def __init__(self, player_no):
        super().__init__()
        self.shape("square")
        self.shapesize(4,1)
        self.pu()
        colormode(255)
        if player_no == 1:
            self.color(RED)
            self.setpos(-460,0)
        elif player_no == 2:
            self.color(BLUE)
            self.setpos(450,0)

    def up(self):
        if self.ycor() < 220:
            self.goto(self.xcor(),self.ycor()+20)


    def down(self):
        if self.ycor() >-241:
            self.goto(self.xcor(),self.ycor()-20)
