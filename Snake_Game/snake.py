from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        cords = [0,-20,-40]
        for x in range(3):
            s = Turtle("square")
            s.pu()
            s.color("white")
            s.setpos(cords[x],0)
            self.snake.append(s)
        self.snake_head = self.snake[0]

    def grow(self):
        tail = self.snake[-1].pos()
        segment = Turtle("square")
        segment.pu()        
        segment.color("white")
        segment.setpos(tail[0],tail[1])
        self.snake.append(segment)

    def up(self):                               #0 = east, 90 = north, 180 = west, 270 = south
        if self.snake_head.heading() in [0.0,180.0]:
            self.snake_head.seth(90)

    def down(self):                           
        if self.snake_head.heading() in [0,180]:                      
            self.snake_head.seth(270)
    
    def left(self):
        if self.snake_head.heading() in [90.0,270.0]:
            self.snake_head.seth(180)

    def right(self):
        if self.snake_head.heading() in [90,270]:
            self.snake_head.seth(0)
    
    def forward(self):
        old_pos = self.snake_head.pos()
        self.snake_head.forward(20)
        for x in range(1, len(self.snake)):
            temp_pos = self.snake[x].pos()
            self.snake[x].setpos(old_pos[0],old_pos[1])
            old_pos = temp_pos

    def snake_pos(self):
        return [x.pos() for x in self.snake]   

    def bit_yourself(self):
        if self.snake_head.pos() in self.snake_pos()[1:]:
            return True
        return False

    def hit_wall(self, edge):
        if self.snake_head.xcor() >= edge or self.snake_head.xcor() <= -edge:
            return True
        if self.snake_head.ycor() >= edge-40 or self.snake_head.ycor() <= -edge:
            return True
        return False
