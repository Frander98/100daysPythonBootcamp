import time
from turtle import Screen
from cars import Car
from crossing_turtle import CrossingTurtle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
crossing_turtle = CrossingTurtle()


cars = []
coordenates = [(-33, -110), (-79, 3), (94, 119), (123, 156), (173, 147), (-188, 137), (-96, -10), (-12, 69), (10, -20), (90, -40), (150, -110)]
for position in coordenates:
    new_car = Car()
    new_car.goto(position)
    cars.append(new_car)


game_on = True
while game_on:
    screen.update()
    for car in cars:
        car.goto(car.xcor() - 15, car.ycor())
    time.sleep(0.5)

screen.exitonclick()
