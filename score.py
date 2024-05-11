from turtle import Turtle
from ball import Ball

ALLIGN = "center"
FONT = ("Aerial", 40, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-50,240)
        self.write(self.l_score,align=ALLIGN,font=FONT)
        self.goto(50,240)
        self.write(self.r_score, align=ALLIGN, font=FONT)

    def update(self):
        self.clear()
        self.goto(-50, 240)
        self.write(self.l_score, align=ALLIGN, font=FONT)
        self.goto(50, 240)
        self.write(self.r_score, align=ALLIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update()

    def r_point(self):
        self.r_score += 1
        self.update()




