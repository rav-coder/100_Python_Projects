from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    segments = []

    def __init__(self, length):
        self.create_snake(length)
        self.head = self.segments[0]
        self.tail = self.segments[-1]
        self.head.color('red')

    def create_snake(self, length):
        x = 0
        for _ in range(length):
            tim = Turtle()
            tim.penup()
            tim.shape('square')
            tim.color('white')
            tim.setposition(x=x, y=0)
            x -= 20
            self.segments.append(tim)

    def extend_snake(self):
        tim = Turtle()
        tim.penup()
        tim.shape('square')
        tim.color('white')
        x = self.tail.xcor()
        y = self.tail.ycor()
        tim.setposition(x=x, y=y)
        self.segments.append(tim)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
