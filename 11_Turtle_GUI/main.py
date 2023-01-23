import turtle

import colorgram, random
from turtle import Turtle, Screen

turtle.colormode(255)
colors = colorgram.extract('damien-hirst-1994-controlled-substance-key-painting.jpg', 36)
color_list = []


def random_rgb():
    for color in colors:
        color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

    return random.choice(color_list)


tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(15):
    for _ in range(15):
        tim.dot(25, random_rgb())
        tim.forward(45)
    tim.setheading(90)
    tim.forward(45)
    tim.setheading(180)
    tim.forward(45*15)
    tim.setheading(0)


screen = Screen()
screen.exitonclick()





