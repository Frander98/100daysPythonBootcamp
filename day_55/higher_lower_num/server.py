from flask import Flask
from decorators import *
from random_num_gen import new_random_number
from random import choice

app = Flask(__name__)
# check the random number
random_number = new_random_number()
# gif_list
gif_links = ['https://media.giphy.com/media/yy6hXyy2DsM5W/giphy-downsized-large.gif', 'https://media.giphy.com/media/qPuhFBQt8xLEY/giphy.gif', 'https://media.giphy.com/media/qPuhFBQt8xLEY/giphy.gif'
             'https://media.giphy.com/media/8rFNes6jllJQRnHTsF/giphy.gif', 'https://media.giphy.com/media/NmGbJwLl7Y4lG/giphy.gif', 'https://media.giphy.com/media/7K3p2z8Hh9QOI/giphy.gif'
             'https://media.giphy.com/media/8rFNes6jllJQRnHTsF/giphy.gif', 'https://media.giphy.com/media/8rFNes6jllJQRnHTsF/giphy.gif', 'https://media.giphy.com/media/dH16CNQJRwPsY/giphy-downsized-large.gif'
             ]


@app.route("/")
def index_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:number>")
def correct_number(number):
    if number == random_number:
        return f"<h1>Correct! The number is {number}!</h1>" \
               f"<img src='https://media.giphy.com/media/gcXcSRYZ9cGWY/giphy-downsized-large.gif'>"
    else:
        return f"<h1>Sorry! That's not the number, keep trying!</h1>" \
               f"<img src={choice(gif_links)}>"


# Run script
if __name__ == '__main__':
    app.run(debug=True)
