from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.separation()

    def move_up(self):
        y = self.ycor() + 30
        self.sety(y)

    def move_down(self):
        y = self.ycor() - 30
        self.sety(y)

    def separation(self):
        y = -400
        x = 0
        while y != 400:
            object = Turtle()
            object.color("white")
            object.hideturtle()
            object.pensize(5)
            object.penup()
            y += 20
            object.goto(x, y)
            object.pendown()
            y += 20
            object.goto(x, y)

    def move_upward1(self):
        self.list1[4].setheading(90)
        self.move1_up()

    def move_upward2(self):
        self.list2[4].setheading(90)
        self.move2_up()

    def down1(self):
        self.list1[0].setheading(270)
        self.move1_down()

    def down2(self):
        self.list2[0].setheading(270)
        self.move2_down()
