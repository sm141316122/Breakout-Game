from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-500, 350)
        self.refresh()

    def refresh(self):
        self.write(f"Level: {self.level}", font=('Arial', 24, 'bold'))
