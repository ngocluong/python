from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "which one win???")
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
all_t = []
is_race_on = False
win = ""
print(user_bet)
for index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[index])
    y = index * 30
    tim.goto(-230, 90 - y)
    all_t.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for tur in all_t:
        if tur.xcor() > 230:
            win = tur.pencolor()
            if win == user_bet:
                print("win")
            else:
                print(f"lose, win is {win}")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        tur.forward(rand_distance)

screen.exitonclick()