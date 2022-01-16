from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -220)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.setposition(STARTING_POSITION)
