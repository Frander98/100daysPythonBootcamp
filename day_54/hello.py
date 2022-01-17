# Flask Web App
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "Bye, bye"


if __name__ == "__main__":
    app.run()

# Instructtions: go to terminal, type "set FLASK_APP=hello.py" then type "flask run" to start the server.
