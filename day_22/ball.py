from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_initial_position = (0, 0)
        self.speed(0.00000000000000000000000001)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 3
        self.y_move = 3

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(self.ball_initial_position)
        self.x_move *= -1
        self.y_move *= -1



