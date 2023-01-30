from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.write_score()

    def write_score(self):
        self.clear()
        self.penup()
        self.setposition(x=-200, y=275)
        self.color('black')
        text = f"Score = {self.score}"
        self.write(text, True, align="center", font=FONT)
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        text = f"GAME OVER!"
        self.setposition(x=0, y=0)
        self.write(text, True, align="center", font=FONT)
