from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(15)

def move_backward():
    tim.backward(15)

def move_counter_clockwise():
    angle = tim.heading() + 15
    tim.setheading(angle)

def move_clockwise():
    angle = tim.heading() - 15
    tim.setheading(angle)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()



## Higher Order Functions
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def calculator(n1, n2, func):  ## taking another function as an input
    return func(n1, n2)

print(calculator(1, 4, add))
print(calculator(1, 4, sub))
