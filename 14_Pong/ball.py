from turtle import Turtle


class Ball(Turtle):

    x_move = 5
    y_move = 5
    move_speed = 0.025

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.circle(radius=2)

    def move(self):
        x_ = self.xcor() + self.x_move
        y_ = self.ycor() + self.y_move
        self.setposition(x=x_, y=y_)

    def switch_y(self):
        self.y_move *= -1
        self.move_speed *= 0.85

    def switch_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.setposition(x=0, y=0)
        self.move_speed = 0.025
        self.switch_x()


