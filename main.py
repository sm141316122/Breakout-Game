from turtle import Screen, Turtle
from paddle import Paddle
from brick import Brick
from ball import Ball
from level import Level
from life import Life
from result import Result
import time


screen = Screen()
screen.setup(width=1100, height=800)
screen.title("Break Game")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
bricks = Brick()
ball = Ball()
level = Level()
life = Life()
result = Result()

screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_on = True
x_distance, y_distance = 2, 2
while game_on:
    if ball.xcor() > 540 or ball.xcor() < -540:
        x_distance *= -1

    elif -332 <= ball.ycor() < -330 and ball.distance(paddle) < 69:
        y_distance *= -1

    elif ball.ycor() < -400:
        life.increase_life()
        paddle.goto(0, -350)
        ball.goto(0, -330)
        x_distance, y_distance = 2, 2
        if len(life.all_life) == 0:
            result.lose()
            game_on = False
        else:
            time.sleep(1)

    elif ball.ycor() > 246:
        y_distance *= -1

    for brick in bricks.all_bricks:
        if y_distance > 0:
            if brick.ycor() - 20 <= ball.ycor() and ball.distance(brick) < 61:
                y_distance *= -1
                bricks.brick_hit(brick)
                print(len(bricks.all_bricks))
                break

        elif ball.ycor() > brick.ycor() - 18 and ball.distance(brick) < 58:
            x_distance *= -1
            bricks.brick_hit(brick)
            print(len(bricks.all_bricks))
            break
    if len(bricks.all_bricks) == 0:
        result.win()
        game_on = False

    ball.move(x_distance, y_distance)

    screen.update()

screen.exitonclick()
