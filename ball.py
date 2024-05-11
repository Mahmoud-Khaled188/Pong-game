from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.025

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)

    def change_y_direction(self):
        self.move_y *= -1

    def change_x_direction(self):
        self.move_x *= -1

        #self.move_speed
