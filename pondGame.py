from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pond Game")
screen.tracer(0)

s1_paddle = Paddle((360, 0))
s2_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(s1_paddle.move_up, "A")
screen.onkey(s1_paddle.move_down, "L")
screen.onkey(s2_paddle.move_up, "Z")
screen.onkey(s2_paddle.move_down, "M")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(s1_paddle) < 50 and ball.xcor() > 320 or ball.distance(s2_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.s2_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.s1_point()

    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()
