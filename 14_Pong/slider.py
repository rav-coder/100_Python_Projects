from turtle import Turtle
MOVE_DISTANCE = 25


class Slider(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setposition(x=xcor, y=ycor)

    def move_up(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.setposition(x=self.xcor() , y=y_cor)

    def move_down(self):
        y_cor = self.ycor() - MOVE_DISTANCE
        self.setposition(x=self.xcor(), y=y_cor)
