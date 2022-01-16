from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(f"Level:  {self.score}", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Level:  {self.score}", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(-90, 0)
        self.write("GAME OVER", font=FONT)
