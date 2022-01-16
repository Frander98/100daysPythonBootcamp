import turtle
from turtle import Turtle, Screen
import pandas as pd


screen = Screen()
screen.setup(width=750, height=510)
screen.title("US States guessing Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)


data = pd.read_csv("50_states.csv")
states_data = pd.DataFrame(data)


flag = True
hits = 0
while flag:
    answer_state = screen.textinput(title=f"State guess {hits}/50", prompt="Write an state:")
    state_column = states_data.state
    state_column_list = state_column.to_list()
    state_row = states_data[states_data.state == answer_state]
    if answer_state in state_column_list:
        state_x_cor = int(state_row.x)
        state_y_cor = int(state_row.y)
        text = Turtle()
        text.hideturtle()
        text.penup()
        text.goto(state_x_cor, state_y_cor)
        text.write(answer_state)
        hits += 1
    if hits == 50:
        flag = False


turtle.mainloop()