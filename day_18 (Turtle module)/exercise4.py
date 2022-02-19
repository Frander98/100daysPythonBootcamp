import turtle 
import random


greg = turtle.Turtle()
greg.shape("turtle")
greg.pensize(1)
greg.speed("fastest")
turtle.colormode(255)
screen = turtle.Screen()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


for _ in range(75):
    greg.color(random_color())
    greg.circle(100)
    greg.left(5)
screen.exitonclick()