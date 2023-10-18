from turtle import Turtle


class Result(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)

    def lose(self):
        self.write(f"Game Over", align="center",  font=('Arial', 36, 'bold'))

    def win(self):
        self.write(f"You Win", align="center",  font=('Arial', 36, 'bold'))
