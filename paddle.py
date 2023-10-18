from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 6)
        self.color("white")
        self.penup()
        self.goto(0, -350)

    def go_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + 20, self.ycor())
