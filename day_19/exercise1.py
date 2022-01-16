#Using key events
from turtle import Turtle, Screen


greg = Turtle()
greg.shape("turtle")
screen = Screen()
screen.textinput("Instructions", "Use W to move fordward, S to move backward, A to move left, D to move right or C to clear the screen.")


def move_forward():
    greg.fd(15)
def move_backward():
    greg.bk(15)
def move_counter_clockwise():
    greg.lt(10)
def move_clockwise():
    greg.rt(10)
def reset():
    screen.reset()

screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=move_counter_clockwise)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="C", fun=reset)
screen.exitonclick()