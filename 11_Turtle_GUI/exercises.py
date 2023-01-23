import turtle
from turtle import Turtle, Screen
import random

tr = Turtle()
tr.shape("arrow")
turtle.colormode(255)
# turtle.fillcolor("cyan")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


for move in range(10, 361,5):
    tr.color(random_color())
    tr.speed(15)
    tr.circle(100)
    tr.right(5)
# tr.right(20)
# tr.circle(100)


# turtle.colormode(255)
# colors = ["black", "blue", "brown", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"]
# lengths = [length for length in range(40, 80)]
# headings = [0, 90, 180, 270]
#
# hex_range = [hexV for hexV in range(0, 256)]
#
# for _ in range(200):
#     tr.speed(8)
#     tr.pensize(20)
#     hex_code = (random.choice(hex_range), random.choice(hex_range), random.choice(hex_range))
#     tr.color(hex_code)
#     # turtle.color(random.choice(colors))
#     tr.forward(random.choice(lengths))
#     tr.setheading(random.choice(headings))


# ANGLE = 360
# for shape in range(3, 11):
#     turtle.color(random.choice(colors))
#     for _ in range(shape):
#         turtle.forward(100)
#         turtle.right(ANGLE/shape)


# for _ in range(25):
#     turtle.pencolor('black')
#     turtle.forward(10)
#     turtle.pencolor('white')
#     turtle.forward(10)

# for _ in range(25):
#     turtle.pendown()
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)


# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

screen = Screen()
screen.exitonclick()
