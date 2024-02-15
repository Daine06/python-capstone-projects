from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align='center', font=('Arial', 20, 'normal'))
        
    def next_level(self):
        self.level += 1
        self.update_level()
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! Your score is: {self.level}", align='center', font=('Arial', 30, 'normal'))
        
        