from turtle import Turtle

class Scoreboard():

    def __init__(self) -> None:
        self.score1 = -1   #since the update score method adds 1pt everytime it is called
        self.score2 = -1
        self.brush1 = Turtle(visible=False)
        self.brush1.color("white")
        self.brush1.pu()
        self.brush1.setpos(-450,280)
        self.brush2 = Turtle(visible=False)
        self.brush2.color("white")
        self.brush2.pu()
        self.brush2.setpos(450,280)
        self.line_brush = Turtle("square", visible=False)
        self.draw_kill_zone()
        self.draw_top_bottom()
        self.draw_divider()
        self.update_score(1)
        self.update_score(2)

    def update_score(self, brush_num):
        if brush_num == 1:
            self.score1 +=1
            text = f"P1: {self.score1}"
            self.brush1.clear()
            self.brush1.write(text, False, "center",font=("ariel", 20, "bold"))
        
        elif brush_num == 2:
            self.score2+=1
            text = f"P2: {self.score2}"
            self.brush2.clear()
            self.brush2.write(text, False, "center",font=("ariel", 20, "bold"))

            
    def draw_kill_zone(self):                #side borders / dead zones
        self.line_brush.color("red")
        self.line_brush.pensize(4)
        self.line_brush.pu()

        self.line_brush.goto(-498,262)      
        self.line_brush.pd()
        self.line_brush.goto(-498,-300)
        self.line_brush.pu()
        self.line_brush.goto(492,262)
        self.line_brush.pd()
        self.line_brush.goto(492,-300)
        self.line_brush.pu()
        
    def draw_top_bottom(self):
        self.line_brush.color("white")       #top and bottom border
        self.line_brush.goto(-520,262)
        self.line_brush.pd()
        self.line_brush.goto(520,262 )
        self.line_brush.pu()
        self.line_brush.pensize(10)
        self.line_brush.goto(-520,-307)
        self.line_brush.pd()
        self.line_brush.goto(520,-307)
        self.line_brush.pu()                 
        
    def draw_divider(self):
        self.line_brush.pensize(6)
        self.line_brush.goto(0,262)
        self.line_brush.setheading(270)
        for _ in range(10):
            self.line_brush.pd()
            self.line_brush.forward(30)
            self.line_brush.pu()
            self.line_brush.forward(30)