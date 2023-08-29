from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1.5)
        self.penup()
        self.goto(position)

    def move_up(self):
        y = self.ycor() + 30
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 30
        self.goto(self.xcor(), y)
