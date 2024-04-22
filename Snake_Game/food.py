import random
from turtle import Turtle

WINDOW_SIZE = 600        #from the left edge to the right it is 600
C_RANGE = WINDOW_SIZE/2  #thus to spawn food within the window, this is cord range

class Food():

    def __init__(self) -> None:
        self.food = Turtle("circle")
        self.food.setpos(200,200)
        self.food.color("red")
        self.food.pu()

    #this method spawns a food item
    def spawn(self, cord_list): #input a list of cords
        cord = random.randrange
        cord_for_food = (cord(-C_RANGE, C_RANGE, 20),cord(-C_RANGE, C_RANGE,20))
        if  cord_for_food not in cord_list:
            self.food.setpos(cord_for_food)
        else:
            self.spawn(cord_list)
    
    #check the pos of snake head and food, and returns if the food has been eaten
    def get_state(self, cord_list):
        tolerance = 0.01
        food_pos = self.food.pos()
        snake_head = cord_list[0]
        distance = ((food_pos[0] - snake_head[0])**2 + (food_pos[1] - snake_head[1])**2)**0.5
        if distance < tolerance:  # Check if distance is less than a tolerance value
            self.spawn(cord_list)
            return True    
        return False