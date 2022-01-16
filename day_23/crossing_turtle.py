from turtle import Turtle


class CrossingTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("turtle")
        self.setheading(90)
        self.goto(0, -220)

