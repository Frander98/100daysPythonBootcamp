from tkinter import *
import pandas as pd
import random

# --------UI--------#
# Data
dataFrame = pd.read_csv("data/english_words.csv")
data_dict = dataFrame.to_dict(orient="records")
random_values = None


# Funciones
def display_new_word():
    random_values = random.choice(data_dict)
    random_word = random_values['source_lang']

    translated_word.config(text=random_word)


def flip_card():
    global random_values
    source_word_title.config(text="Español")




# Window
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
window.after(3000, func=flip_card)

# Lectura de imagenes
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
check_image = PhotoImage(file="images/right.png")
x_image = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=500, height=330)
canvas.create_image(250, 165, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
source_word_title = Label(text="English", font=("Arial", "31", "italic"))
source_word_title.place(x=180, y=75)
translated_word = Label(text="", font=("Arial", "50", "bold"))
translated_word.place(x=145, y=160)

# Buttons
right_button = Button(image=check_image, highlightthickness=0, command=display_new_word)
right_button.grid(row=1, column=0)
wrong_button = Button(image=x_image, highlightthickness=0, command=display_new_word)
wrong_button.grid(row=1, column=1)

# MainLoop
window.mainloop()
