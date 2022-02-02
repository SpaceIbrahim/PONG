from turtle import Turtle
MOVE_DIST = 30

class Paddle(Turtle):

    def __init__(self, p):
        super().__init__()
        self.create()
        self.goHome(p)

    def create(self):
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)

    def goHome(self, home):
        self.goto(home)

    def moveUp(self):
        new_y = self.ycor()+MOVE_DIST
        self.goto(x=self.xcor(), y=new_y)
        
    def moveDown(self):
        new_y = self.ycor() - MOVE_DIST
        self.goto(x=self.xcor(), y=new_y)