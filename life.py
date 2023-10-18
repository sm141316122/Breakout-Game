from turtle import Turtle


POSITION = [(400, 350), (430, 350), (460, 350)]


class Life:

    def __init__(self):
        self.all_life = []
        self.create_life(POSITION)

    def create_life(self, position):
        for pos in position:
            life = Turtle("square")
            life.color("red")
            life.penup()
            life.goto(pos)
            self.all_life.append(life)

    def increase_life(self):
        self.all_life[0].color("black")
        self.all_life = self.all_life[1:]
