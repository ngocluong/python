from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
scoreboard = ScoreBoard()

screen.title("Pong")
screen.tracer(0)
paddle_a = Paddle(-350, 0)
paddle_b = Paddle(350, 0)

screen.listen()
screen.onkey(paddle_b.up, "Up")
screen.onkey(paddle_b.down, "Down")
screen.onkey(paddle_a.up, "w")
screen.onkey(paddle_a.down, "s")

ball = Ball()
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.moving()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
    if ball.distance(paddle_a) < 50 and ball.xcor() < -345 or ball.distance(paddle_b) < 50 and ball.xcor() > 345:
        ball.xbounce()
    if ball.xcor() > 400:
        scoreboard.i_l_score()
        # game_on = False
        # scoreboard.gameover()
        ball.reset()
    if ball.xcor() < -400:
        scoreboard.i_r_score()
        ball.reset()

screen.exitonclick()
