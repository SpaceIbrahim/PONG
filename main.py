from turtle import Screen
import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=1000)
screen.title("PONG")
screen.listen()
screen.tracer(0)

score = Score()
ball = Ball()
rp = Paddle.Paddle((450, 0))
lp = Paddle.Paddle((-450, 0))

screen.onkeypress(rp.moveUp, "Up")
screen.onkeypress(rp.moveDown, "Down")

screen.onkeypress(lp.moveUp, "w")
screen.onkeypress(lp.moveDown, "s")

run = True
while run:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 440 and ball.distance(rp) < 60:
        ball.bop()

    if ball.xcor() < -440 and ball.distance(lp) < 60:
        ball.bop()

    if ball.xcor() > 500:
        score.Lscore()
        ball.reset_pos()

    if ball.xcor() < -500:
        ball.reset_pos()
        score.Rscore()
