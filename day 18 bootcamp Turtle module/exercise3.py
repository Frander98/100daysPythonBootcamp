#error in line 5 "t.colormode(255)" not finded yet.
import turtle as t 
import random

greg = t.Turtle()
t.colormode(255)
greg.shape("turtle")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color


greg.speed("fastest")
greg.pensize(6)
angles = [0, 90, 180, 270]


for _ in range(300):
    greg.color(random_color())
    greg.setheading(random.choice(angles))
    greg.forward(10)

