
from turtle import Screen
from slider import Slider
from ball import Ball
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()

slider_right = Slider(380, 0)
slider_left = Slider(-390, 0)
ball = Ball()
score = Score()

screen.onkey(fun=slider_right.move_up, key='Up')
screen.onkey(fun=slider_right.move_down, key='Down')
screen.onkey(fun=slider_left.move_up, key='w')
screen.onkey(fun=slider_left.move_down, key='s')

running = True
while running:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -280:
        ball.switch_y()

    # detect collision with right slider
    if ball.xcor() > 375 and ball.distance(slider_right) < 50:
        ball.switch_x()

    # detect collision with left slider
    if ball.xcor() < -375 and ball.distance(slider_left) < 50:
        ball.switch_x()

    # update score of the right or left player
    if ball.xcor() < -400:
        score.increase_score("right")
        ball.reset_ball()

    if ball.xcor() > 400:
        score.increase_score("left")
        ball.reset_ball()

screen.exitonclick()
