from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

SCREEN_SIZE = 600
SCREEN_EDGE = 300 

class Snake_Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(SCREEN_SIZE,SCREEN_SIZE)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.food = Food()
        self.snake = Snake()
        self.scoreboard = Scoreboard()

    def run_game(self):
        self.screen.listen()
        self.screen.onkey(self.snake.up,"Up")
        self.screen.onkey(self.snake.down,"Down")
        self.screen.onkey(self.snake.left,"Left")
        self.screen.onkey(self.snake.right,"Right")

        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.17)
            self.snake.forward()
            if self.snake.hit_wall(SCREEN_EDGE):
                game_is_on = False
            if self.snake.bit_yourself():
                game_is_on = False
            if self.food.get_state(self.snake.snake_pos()):
                self.snake.grow()
                self.scoreboard.update_score(self.food.eaten)
        self.scoreboard.game_over()
        self.screen.exitonclick()


s = Snake_Game()
s.run_game()