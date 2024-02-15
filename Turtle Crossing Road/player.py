from turtle import Turtle

UP = 90

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.reset_pos()
        self.setheading(UP)
        
    def up(self):
        self.forward(MOVE_DISTANCE)
        
    def reset_pos(self):
        self.goto(STARTING_POSITION)