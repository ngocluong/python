from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.updatescore()

    def i_l_score(self):
        self.l_score += 1
        self.updatescore()

    def i_r_score(self):
        self.r_score += 1
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 24, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 24, "bold"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

