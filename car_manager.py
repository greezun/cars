from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 2)
        self.pu()
        self.color(random.choice(COLORS))
        self.goto(300, random.randrange(-250, 250, 20))
        self.setheading(180)
        self.run_speed = STARTING_MOVE_DISTANCE



    def run_car(self, distance):
        self.fd(distance)

    def speed_increment(self):
        self.run_speed += MOVE_INCREMENT


