from turtle import Turtle
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(x=0, y=275)
        self.color('white')
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.setposition(x=0, y=275)
        self.score += 1
        text = f"Score = {self.score}"
        self.write(text, True, align="center", font=FONT)

    def game_over(self):
        text = f"GAME OVER!"
        self.setposition(x=0, y=0)
        self.write(text, True, align="center", font=FONT)
