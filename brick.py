from turtle import Turtle


POSITION = []
X = -500
Y = 246
for _ in range(5):
    for num in range(11):
        p = (X + (num*100), Y)
        POSITION.append(p)

    Y -= 24


class Brick:

    def __init__(self):
        self.all_bricks = []
        self.create_bricks(POSITION)

    def create_bricks(self, position):
        for pos in position:
            brick = Turtle("square")
            brick.shapesize(1, 4.8)
            brick.color("white")
            brick.penup()
            brick.goto(pos)
            self.all_bricks.append(brick)

    def brick_hit(self, turtle):
        turtle.color("black")
        turtle.clear()
        self.all_bricks.remove(turtle)
