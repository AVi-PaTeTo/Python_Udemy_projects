from turtle import Turtle

#screen size = height = 1000, width=600
class Ball(Turtle):
    
    
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.pu()
        self.setpos(0,0)
        self.color("white")
        self.x_velocity = 10
        self.y_velocity = 10

    def bounce_x(self): #when the ball hits paddle
        self.x_velocity*=-1
    
    def bounce_y(self): #when the ball hits the ceiling or the floor
        self.y_velocity *= -1
    
    def reset(self):
        self.setpos(0,0)
