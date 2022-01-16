from turtle import Turtle, Screen
import random

greg = Turtle()
greg.shape("turtle")
greg.color("dark sea green")
screen = Screen()


colors = ["gray39", "gold4", "azure2", "brown", "AliceBlue", "aquamarine", "black", "IndianRed", "NavyBlue", "orange"]

def draw_poligon(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        greg.forward(100)
        greg.right(angle)

for n_sides in range(3,11):
    greg.color(random.choice(colors))
    draw_poligon(n_sides)

screen.exitonclick()

