from turtle import Turtle

SCREEN_SIZE = 600


class Scoreboard:
    def __init__(self):
        self.create_border()
        self.brush = Turtle(visible=False)
        self.brush.speed("fastest")
        self.brush.setpos(0,260)
        self.brush.color("black")
        self.update_score(0)

    def create_border(self):
        self.border = Turtle("square",visible=False)
        self.border.pensize(50)
        self.border.color("white")
        self.border.speed("fastest")
        self.border.pu()
        self.border.setpos(300,275)
        self.border.pd()
        self.border.setpos(-300,275)
        self.border.pu()
    
    def update_score(self, score):
        text = f"Score: {score}"
        self.brush.clear()
        self.increase_score(text)

    def increase_score(self, text):
        self.brush.write(text, False, align="center", font=("ariel", 20, "bold"))

    def game_over(self):
        self.brush.pu()
        self.brush.color("red")
        self.brush.setpos(0,0)
        self.brush.write("GAME OVER", False, align="center", font=("ariel", 30, "bold"))