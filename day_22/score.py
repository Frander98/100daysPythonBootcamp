from turtle import Turtle

FONT_STYLE = ("Courier", 40, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(self.score, font=FONT_STYLE)

    def update_score(self):
        self.clear()
        self.write(self.score, font=FONT_STYLE )

    def increase_score(self):
        self.score += 1
        self.update_score()
