from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Welcome to the turtle race. ")
screen.setup(width=1085, height=530, startx=0, starty=0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
goal_line_drawing_turtle = Turtle(shape="turtle")
goal_line_drawing_turtle.penup()
goal_line_drawing_turtle.goto(528, -100)
goal_line_drawing_turtle.left(90)
goal_line_drawing_turtle.pendown()
goal_line_drawing_turtle.forward(250)
goal_line_drawing_turtle.hideturtle()


y_position = -70
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-530, y=y_position)
    y_position += 35
    all_turtles.append(new_turtle)


user_bet = screen.textinput(title="User's bet.", prompt="Which turtle do you think is gonna win?, enter a color: ")


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 530:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You´ve won! The winner is {winning_color} turtle.")
                screen.textinput(title="Result" ,prompt=f"You´ve won! The winner is {winning_color} turtle.")
            else:
                print(f"You´ve lost! The winner is {winning_color} turtle.")
                screen.textinput(title="Result" ,prompt=f"You´ve lost! The winner is {winning_color} turtle.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
