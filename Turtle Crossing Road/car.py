from turtle import Turtle, Screen
import colorgram
import random

LEFT = 180

STARTING_DRIVE_DISTANCE = 5
DRIVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color_list = []
        self.car_list = []
        self.penup()
        self.car_speed = STARTING_DRIVE_DISTANCE
        
    def create_car(self):
        random_num = random.randint(1,6)
        if random_num == 3:
            new_car = Car()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(self.random_color())
            new_car.goto(x= 300, y=random.randint(-240, 240))
            self.car_list.append(new_car)
        
    def random_color(self):
        colors = colorgram.extract(f='image.jpg', number_of_colors=5)
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            self.color_list.append(new_color)
              
        random_color = random.choice(self.color_list)
        return random_color
    
    def move_cars(self):
        for car in self.car_list:    
            if car.xcor() == 300:
                car.setheading(LEFT)   
            car.forward(STARTING_DRIVE_DISTANCE)
            
    def level_up(self):
        self.car_speed += DRIVE_INCREMENT
        
    
                
        