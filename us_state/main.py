IMG = "blank_states_img.gif"
import turtle
import pandas
screen = turtle.Screen()

screen.bgpic(IMG)
screen.addshape(IMG)
turtle = turtle.Turtle()
turtle.penup()
game_on = True
data = pandas.read_csv('50_states.csv')
guess_states = []
all_states = data.state.tolist()

while game_on:
    state = screen.textinput("Enter State's Name: ", prompt="Enter State's Name: ")
    result = data[data.state == state]
    if state == "Exit":
        game_on = False
        print(f"Game Over. Missing {list(set(all_states) - set(guess_states))}.")
    if len(result) > 0:
        guess_states.append(result.state.values[0])
        turtle.goto(result.iloc[0].x, result.iloc[0].y)
        turtle.write(result.iloc[0].state, align="center", font=("Arial", 12, "normal"))
    if len(guess_states) >= 50:
        game_on = False
        print(f"YOU GOT ALL STATES")