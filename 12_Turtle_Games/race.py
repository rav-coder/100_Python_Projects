from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=550, height=500)
user_choice = screen.textinput(title='Make your bet', prompt="Enter the color of the turtle that will win? ")

colors = ['red', 'green', 'yellow', 'black', 'blue']
y = -100
turtles = []
turtle = {}
winner = False

jim = Turtle()
jim.penup()
jim.setposition(x=250, y=235)
jim.pendown()
jim.setheading(270)
jim.forward(235*2)

for color in colors:
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.color(color)
    tim.setposition(x=-250, y=y)
    y += 50
    turtles.append({'turtle': tim, 'color': color})


while not winner:
    for dict_turtle in turtles:
        if dict_turtle['turtle'].xcor() >= 250:
            turtle = dict_turtle
            winner = True
            break
        pace = random.randint(10, 20)
        dict_turtle['turtle'].forward(pace)


if turtle['color'] == user_choice.lower():
    print(f" {turtle['color'].title()} Turtle finished first. You win!")
else:
    print(f" {turtle['color'].title()} Turtle finished first. You lost!")

screen.exitonclick()
