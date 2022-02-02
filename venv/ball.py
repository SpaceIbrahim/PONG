from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.p = False
        self.speedX = 0.175
        self.speedY = 0.175

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):

        new_x = self.xcor() + self.speedX
        new_y = self.ycor() + self.speedY

        self.goto(x=new_x, y=new_y)

    def bounce(self):

        self.speedY *= -1

    def bop(self):
        self.speedX *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bop()