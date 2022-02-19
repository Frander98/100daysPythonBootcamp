from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)
current_date = datetime.now()


@app.route("/")
def homepage():
    random_number = randint(1, 10)
    current_year = current_date.year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<user_name>")
def apis_display_info(user_name):
    genderize_response = requests.get(f"https://api.genderize.io?name={user_name}").json()
    agify_response = requests.get(f"https://api.agify.io?name={user_name}").json()
    gender = genderize_response["gender"]
    age = agify_response["age"]
    return render_template("apis_practice.html", name=user_name, age=age, gender=gender)


@app.route("/blog")
def blog():
    posts = requests.get(" https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
