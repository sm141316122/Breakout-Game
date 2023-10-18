from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -330)

    def move(self, x_distance, y_distance):
        x = self.xcor() + x_distance
        y = self.ycor() + y_distance
        self.goto(x, y)
