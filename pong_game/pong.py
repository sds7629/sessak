import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("퐁게임")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_ison = True
while game_ison:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
