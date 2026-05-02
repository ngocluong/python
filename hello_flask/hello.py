from flask import Flask
import random

r_number = random.randint(1, 9)
print(r_number)
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return '<p>Guess number!</p>' \
           '<img class="giphy-gif-img " src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="200px" height="200px" alt="Police Call 911 GIF by Adult Swim" style="background: rgba(0, 0, 0, 0);">")'

@app.route("/<int:number>")
def guessing(number):
    if number > r_number:
        return f'<p>{number}: too high try again</p> <img class="giphy-gif-img " src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'
    elif number < r_number:
        return f'<p>{number}: to low try again</p> <img class="giphy-gif-img " src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    else:
        return f'<p>{number} is correct</p> <img class="giphy-gif-img " src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'


if __name__ == "__main__":
    app.run(debug=True)