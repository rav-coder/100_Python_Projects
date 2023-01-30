from turtle import Turtle
import random, time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5


class CarManager:
    starting_move_distance = 5

    def __init__(self):
        self.cars = []

    def generate_new_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape('square')
        car.shapesize(stretch_len=2.5, stretch_wid=1.2)
        car.setposition(x=random.randrange(320, 600, 50), y=random.randrange(-240, 260, 40))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT

