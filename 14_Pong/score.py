from turtle import Turtle
FONT = ('Arial', 15, 'normal')


class Score(Turtle):
    score_left = 0
    score_right = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(x=0, y=275)
        self.color('white')
        self.hideturtle()

    def increase_score(self, player):
        self.clear()
        self.setposition(x=0, y=275)
        if player == 'left':
            self.score_left += 1
        elif player == 'right':
            self.score_right += 1
        text = f"{self.score_left} -- {self.score_right}"
        self.write(text, True, align="center", font=FONT)
