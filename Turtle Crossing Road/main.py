from turtle import Screen
from car import Car
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.colormode(255)
car = Car()
car.hideturtle()
player = Player()
scoreboard = ScoreBoard()

screen.tracer(0)

screen.listen()
screen.onkey(key="w", fun=player.up)

game_is_on = True
while game_is_on == True:
    time.sleep(0.1)
    screen.update()
     
    car.create_car() 
    car.move_cars()
        
    for cars in car.car_list:
        if cars.distance(player) < 20:
            game_is_on = False 
            scoreboard.game_over()
            
    if player.ycor() > 280:
        scoreboard.next_level()
        player.reset_pos()
        car.level_up()
        
        
screen.exitonclick()