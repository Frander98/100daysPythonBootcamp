from turtle import Turtle, Screen, ycor
import random

screen = Screen()
screen.setup (width=1366, height=760, startx=0, starty=0)
screen.colormode(255) #para cambiar a RGB
colors = [(225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (102, 34, 57), (52, 34, 57), (215, 124, 57),(215, 239, 57), (255, 28, 49) ]
greg = Turtle()


for _ in range(8):
    initial_greg_y_position = greg.ycor() #(0,0)
    for _ in range(8):
        greg.dot(13, random.choice(colors) )
        greg.penup()
        greg.forward(50)
    greg.goto(0,initial_greg_y_position + 50)


screen.exitonclick()