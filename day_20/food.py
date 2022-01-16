from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_position = random.randint(-230, 230)
        y_position = random.randint(-230, 230)
        self.goto(x_position, y_position)
