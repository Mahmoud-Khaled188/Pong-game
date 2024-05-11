from turtle import Screen
from paddle import Paddle
from score import Score
import time
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()
ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_down, "s")

score = Score()

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_y_direction()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.change_x_direction()

    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
