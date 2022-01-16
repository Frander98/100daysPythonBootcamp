from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 7
RANDOM_Y_POSITIONS = list(range(-190, 240))


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.all_cars = []

    def create_cars(self):
        random_chance = randint(1, 8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, choice(RANDOM_Y_POSITIONS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def stop_cars(self):
        for car in self.all_cars:
            car.goto(self.xcor(), self.ycor())

    def increment_speed(self):
        self.car_speed += MOVE_INCREMENT
