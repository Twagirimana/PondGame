from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.s1_score = 0
        self.s2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.s1_score, align="center", font=("courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.s2_score, align="center", font=("courier", 60, "normal"))

    def s1_point(self):
        self.s1_score += 1
        self.update_scoreboard()

    def s2_point(self):
        self.s2_score += 1
        self.update_scoreboard()
