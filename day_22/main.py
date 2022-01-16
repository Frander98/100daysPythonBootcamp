from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from score import Score
import time

screen = Screen()
screen.colormode(255)
screen.bgcolor((39, 40, 46))
screen.setup(width=800, height=600)
screen.title("Pong Game")
line = Turtle()
line.hideturtle()
line.penup()
line.color("white")
line.goto(0, -398)
line.setheading(90)
screen.tracer(0)
for _ in range(100):
    line.pendown()
    line.forward(20)

ball = Ball()
r_paddle = Paddle((350, 0))
r_score = Score((30, 230))
l_paddle = Paddle((-350, 0))
l_score = Score((-55, 230))

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(0.000000001)

    # Detect collision with up and down walls -->
    if ball.ycor() > 287 or ball.ycor() < -250:
        ball.bounce_y()

    # Detect collision with paddles:
    if ball.distance(r_paddle) < 60 and ball.xcor() > 330:
        ball.bounce_x()
    if ball.distance(l_paddle) < 60 and ball.xcor() < -330:
        ball.bounce_x()
    # Detect when ball has gone beyond boundaries on the x cor
    # right paddle
    if ball.xcor() > 375:
        ball.reset_ball()
        l_score.increase_score()
        time.sleep(0.06)
    # left paddle
    if ball.xcor() < -375:
        ball.reset_ball()
        r_score.increase_score()
        time.sleep(0.06)

screen.exitonclick()
