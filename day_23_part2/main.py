import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
screen.onkey(player.up, "Up")
score = Scoreboard((-250, 250))

game_is_on = True
while game_is_on:
    car_manager.create_cars()
    car_manager.move_cars()
    screen.update()
    time.sleep(0.1)
    # Reset turtle's pos and increment cars speed
    if player.ycor() > 260:
        player.reset_position()
        car_manager.increment_speed()
        score.increase_score()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            car_manager.stop_cars()
            game_is_on = False
            score.game_over()

screen.exitonclick()
