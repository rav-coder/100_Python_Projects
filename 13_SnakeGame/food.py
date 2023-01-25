from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.speed('fastest')
        self.new_food()

    def new_food(self):
        self.setposition(x=random.randint(-290, 290), y=random.randint(-290, 290))
